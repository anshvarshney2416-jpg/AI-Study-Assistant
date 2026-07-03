from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from services.gemini_service import ask_gemini
from services.pdf_service import extract_text
from services.notes_service import generate_notes
from services.quiz_service import generate_quiz
from services.flashcard_service import generate_flashcards

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Global Variables
# -----------------------------

chat_history = []

pdf_text = ""

# -----------------------------
# Home Route
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    global pdf_text

    if request.method == "POST":

        subject = request.form["subject"]

        difficulty = request.form["difficulty"]

        question = request.form["question"]

        action = request.form.get("action", "ask")

        # -----------------------------
        # Upload PDF
        # -----------------------------

        pdf = request.files.get("pdf_file")

        if pdf and pdf.filename != "":

            filename = secure_filename(pdf.filename)

            pdf_path = os.path.join(

                app.config["UPLOAD_FOLDER"],

                filename

            )

            pdf.save(pdf_path)

            pdf_text = extract_text(pdf_path)

        # -----------------------------
        # Decide which feature to use
        # -----------------------------

        try:

            if action == "ask":

                prompt = f"""
You are an expert {subject} teacher.

Explain at a {difficulty} level.

If the uploaded PDF contains the answer,
use the PDF first.

Otherwise use your own knowledge.

PDF Content:

{pdf_text}

Question:

{question}
"""

                answer = ask_gemini(prompt)

            elif action == "notes":

                answer = generate_notes(
                    pdf_text,
                    subject
                )

            elif action == "quiz":

                answer = generate_quiz(
                    pdf_text,
                    subject
                )

            elif action == "flashcards":

                answer = generate_flashcards(
                    pdf_text,
                    subject
                )

            else:

                answer = "Invalid Action"

        except Exception as e:

            answer = f"Error: {e}"

        if action == "ask":

            display_question = question

        elif action == "notes":

            display_question = "📝 Generate Notes"

        elif action == "quiz":

            display_question = "❓ Generate Quiz"

        else:

            display_question = "💡 Generate Flashcards"

        chat_history.append({

            "question": display_question,

            "answer": answer

        })

    return render_template(

        "index.html",

        chat_history=chat_history,

        pdf_uploaded=(pdf_text != "")

    )


@app.route("/clear")
def clear():

    global pdf_text

    chat_history.clear()

    pdf_text = ""

    return render_template(

        "index.html",

        chat_history=chat_history,

        pdf_uploaded=False

    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)