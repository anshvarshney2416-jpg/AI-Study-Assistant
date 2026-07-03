from services.gemini_service import ask_gemini


def generate_notes(pdf_text, subject):

    prompt = f"""
You are an expert {subject} teacher.

Study the uploaded PDF carefully.

Prepare well-structured notes.

Include:

1. Important Concepts
2. Definitions
3. Formulae (if any)
4. Key Points
5. Summary

PDF Content:

{pdf_text}
"""

    return ask_gemini(prompt)