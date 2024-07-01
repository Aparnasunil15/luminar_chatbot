from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Rasa server URL
RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']

    # Send user message to Rasa server
    response = requests.post(RASA_SERVER_URL, json={"message": user_message})

    if response.status_code == 200:
        # Extract and return bot response
        bot_response = response.json()[0]['text']
        return jsonify({'response': bot_response})
    else:
        return jsonify({'response': 'Failed to get response from Rasa server'})

if __name__ == '__main__':
    app.run(debug=True)
