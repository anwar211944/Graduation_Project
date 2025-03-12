import os
from flask import Flask, render_template, request, jsonify
from llama_cpp import Llama

# Initialize the Flask application
app = Flask(__name__)

# Load the GGUF model
MODEL_PATH = "MaziyarPanahi/BioMistral-7B-GGUF/BioMistral-7B.Q2_K.gguf"  # Replace with your actual model path
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,  # Adjust context length as needed
    n_batch=512,  # Batch size
    verbose=False  # Set to True for model loading info
)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat interactions"""
    try:
        # Get user input from the request
        user_message = request.json.get('message', '')
        
        # Generate response using the model
        response = llm(
            f"User: {user_message}\nAssistant:", 
            max_tokens=300,  # Adjust max response length
            stop=["User:", "\n"],
            echo=False
        )
        
        # Extract the generated text
        bot_response = response['choices'][0]['text'].strip()
        
        return jsonify({
            'status': 'success',
            'message': bot_response
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
