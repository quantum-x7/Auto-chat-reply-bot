import google.generativeai as genai

# Try the first key or second key here
genai.configure(api_key="AIzaSyB5cfOTSD1qE-JZBahSGvTmzpqiZxsGiU8")

# List all models available to this key
models = genai.list_models()

print("Available models for this API key:")
for model in models:
    print(f"- {model.name}")
