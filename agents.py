from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

class RolePlayingAgent:
    def __init__(self, name, role_description):
        self.name = name
        self.role_description = role_description
        self.chat_history = []

    def send_message(self, message):
        # Add user message
        self.chat_history.append({"author": "user", "content": message})

        # Build prompt with system description
        conversation_text = f"{self.role_description}\n"
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
