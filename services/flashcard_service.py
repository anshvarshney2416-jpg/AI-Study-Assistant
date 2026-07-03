from services.gemini_service import ask_gemini


def generate_flashcards(pdf_text, subject):

    prompt = f"""
You are an expert {subject} teacher.

Read the uploaded PDF.

Create 10 flashcards.

Format:

Question:
Answer:

PDF Content:

{pdf_text}
"""

    return ask_gemini(prompt)