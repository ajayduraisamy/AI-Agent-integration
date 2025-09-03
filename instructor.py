from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

class InstructorAgent:
    def __init__(self, syllabus):
        self.syllabus = syllabus
        self.chat_history = []

    def teach(self, user_question):
        self.chat_history.append({"author": "user", "content": user_question})
        conversation_text = f"Syllabus:\n{self.syllabus}\n"
        for msg in self.chat_history:
            conversation_text += f"{msg['author']}: {msg['content']}\n"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation_text,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)  
            )
        )
        answer = response.text
        self.chat_history.append({"author": "ai", "content": answer})
        return answer
