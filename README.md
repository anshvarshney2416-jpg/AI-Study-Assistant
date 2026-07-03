# 🤖 AI Study Assistant

An AI-powered Study Assistant built using **Python**, **Flask**, and **Google Gemini AI**. This application helps students ask questions, upload study notes in PDF format, generate AI-powered notes, quizzes, and flashcards through a simple and user-friendly web interface.

---

## 📌 Features

- 🤖 Ask questions using Google Gemini AI
- 📄 Upload PDF study notes
- 📝 Generate AI-powered study notes
- ❓ Generate multiple-choice quizzes
- 💡 Generate flashcards for revision
- 📚 Subject selection
- 🎯 Difficulty level selection
- 🗑️ Clear chat history
- 🎨 Clean and responsive user interface

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI
- Google Gemini API

### Frontend
- HTML5
- CSS3
- JavaScript

### Libraries
- PyPDF2
- python-dotenv
- google-generativeai
- Werkzeug

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
AI-Study-Assistant/
│
├── services/
│   ├── gemini_service.py
│   ├── pdf_service.py
│   ├── notes_service.py
│   ├── quiz_service.py
│   └── flashcard_service.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anshvarshney2416-jpg/AI-Study-Assistant.git
```

### 2. Move into the project folder

```bash
cd AI-Study-Assistant
```

### 3. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

### 🏠 Home Page

> Add a screenshot here

---

### 📄 PDF Upload

> Add a screenshot here

---

### 🤖 AI Response

> Add a screenshot here

---

### 📝 Generated Notes

> Add a screenshot here

---

### ❓ Generated Quiz

> Add a screenshot here

---

### 💡 Flashcards

> Add a screenshot here

---

## 🎯 Future Improvements

- User Authentication
- Download Notes as PDF
- Dark Mode
- Voice Assistant
- Database Integration
- Chat History Storage
- AI Revision Planner
- AI Mind Maps
- Multi-language Support
- Mobile Responsive Design

---

## 📚 What I Learned

Through this project I learned:

- Flask Web Development
- RESTful Application Structure
- Google Gemini AI Integration
- Prompt Engineering
- PDF Text Extraction
- Python Project Structure
- HTML, CSS and JavaScript Integration
- Git and GitHub Workflow

---

## 👨‍💻 Author

**Ansh Varshney**

- GitHub: https://github.com/anshvarshney2416-jpg
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It motivates me to build more open-source AI projects.

Ansh Varshney
