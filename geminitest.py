from google import genai

client = genai.Client()

print("🤖 Gemini AI Chatbot ready! (Type 'exit' to stop)")
print("-" * 50)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    if not user_input.strip():
        continue

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )
    
    print(f"\nGemini: {response.text}")
    print("-" * 50)