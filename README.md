EduGPT - AI Instructor

EduGPT is an AI-powered instructor platform that generates personalized learning syllabi and answers questions interactively using Google Gemini Flash API. This project demonstrates a full-stack AI application built with Flask.


Features

Interactive Syllabus Generation: Enter any topic, and EduGPT generates a structured syllabus using AI.

Dynamic Instructor: Ask questions based on the syllabus and get detailed AI-generated answers.

Single-page Responsive Interface: Minimal, clean, and mobile-friendly UI using Bootstrap.

Premium AI Integration: Uses Google Gemini Flash for fast and high-quality responses.






Installation

Clone the repository

git clone https://github.com/ajayduraisamy/AI-Agent-integration.git
cd AI-Agent-integration

🛠 Tech Stack

Backend: Python, Flask

Frontend: HTML, Bootstrap 5

AI: Google Gemini Flash via LangChain

Environment: python-dotenv for API key management

Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Setup environment variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key
GOOGLE_PROJECT_ID=your_google_project_id

Usage

Start the Flask server:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


License

This project is open source and available under the MIT License.