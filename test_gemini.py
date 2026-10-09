
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env")
    raise SystemExit(1)

client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents="Explain AI chatbots in two simple sentences."
    )
    print("\nGemini response:")
    print(response.text)

except Exception as error:
    print("\nAPI request failed:")
    print(error)