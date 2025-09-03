from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
import os
from agents import RolePlayingAgent
from syllabus_generator import generate_syllabus
from instructor import InstructorAgent

# Load API key from .env
load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize agents (will use Gemini Flash mode)
agent1 = RolePlayingAgent("Agent1", "Expert in AI and education")
agent2 = RolePlayingAgent("Agent2", "Expert in pedagogy and curriculum design")
instructor = None  # will be initialized after syllabus generation

@app.route("/", methods=["GET", "POST"])
def index():
    global instructor
    syllabus_content = None
    instructor_answer = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate_syllabus":
            topic = request.form.get("topic")
            if not topic:
                flash("Please enter a topic!", "warning")
            else:
                # Agents role-play to create a syllabus
                dialogue1 = agent1.send_message(f"Let's design a syllabus for learning {topic}.")
                dialogue2 = agent2.send_message(dialogue1)
                dialogue3 = agent1.send_message(dialogue2)

                combined_dialogue = "\n".join([dialogue1, dialogue2, dialogue3])
                syllabus_content = generate_syllabus(combined_dialogue)

                # Initialize instructor with generated syllabus
                instructor = InstructorAgent(syllabus_content)
                flash("Syllabus generated successfully!", "success")

        elif action == "ask_instructor":
            question = request.form.get("question")
            if instructor and question:
                instructor_answer = instructor.teach(question)
            else:
                flash("Generate a syllabus first and enter a question!", "warning")

    return render_template(
        "index.html",
        syllabus=syllabus_content,
        answer=instructor_answer
    )

if __name__ == "__main__":
    app.run(debug=True)
