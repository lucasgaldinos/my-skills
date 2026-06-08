# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai",
#     "python-dotenv",
# ]
# ///
import os
import sys
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~/.agents/.env"))
if not os.environ.get("GEMINI_API_KEY"):
    print("Warning: no api key found for test")
    sys.exit(0)

client = genai.Client()

# Create dummy file
with open("dummy.txt", "w") as f:
    f.write("Hello World")

print("Uploading dummy file...")
uploaded_file = client.files.upload(file="dummy.txt")
while uploaded_file.state.name == "PROCESSING":
    time.sleep(1)
    uploaded_file = client.files.get(name=uploaded_file.name)

query = "Summarize this file."

print("Testing with input=types.Content")
try:
    content = types.Content(role="user", parts=[query, uploaded_file])
    res = client.interactions.create(agent="deep-research-preview-04-2026", input=content)
    print("Success with types.Content")
except Exception as e:
    print(f"Error types.Content: {e}")
    try:
        print("Testing with manual parts")
        parts = []
        parts.append(types.Part.from_text(text=query))
        parts.append(types.Part.from_uri(uri=uploaded_file.uri, mime_type=uploaded_file.mime_type))
        content2 = types.Content(role="user", parts=parts)
        res2 = client.interactions.create(agent="deep-research-preview-04-2026", input=content2)
        print("Success with manual parts")
    except Exception as e2:
        print(f"Error manual parts: {e2}")

