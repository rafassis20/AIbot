import openai

# Definindo a chave da API diretamente para teste (substitua pela sua chave real)
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)