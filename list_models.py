"""List Gemini models that support generateContent."""

import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY", "").strip()
if not api_key or api_key == "PASTE_KEY_HERE":
    raise SystemExit("Missing required environment variable: GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)
for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print((model.name or "").removeprefix("models/"))
