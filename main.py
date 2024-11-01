import openai
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

openai.api_key = "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" 

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    if not user_input:
        return jsonify({"error": "Nenhuma mensagem recebida"}), 400
    response = chat_with_gpt(user_input)
    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)
