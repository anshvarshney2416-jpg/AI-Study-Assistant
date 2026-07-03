from services.gemini_service import ask_gemini


def generate_quiz(pdf_text, subject):

    prompt = f"""
You are an expert {subject} teacher.

Read the uploaded PDF.

Generate 10 multiple-choice questions.

Each question should have:

A)
B)
C)
D)

Also provide the correct answer.

PDF Content:

{pdf_text}
"""

    return ask_gemini(prompt)