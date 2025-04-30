from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start') 
def start(): 
    return render_template('start.html')

@app.route('/tool') 
def tool(): 
    return render_template('tool.html')

@app.route('/week') 
def week(): 
    return render_template('week.html')

@app.route('/chtbt') 
def chtbt(): 
    return render_template('chat.html')

@app.route('/doctor') 
def doctor(): 
    return render_template('doctor.html')

@app.route('/webhooks/rest/webhook', methods=['POST'])
def forward_request():
    response = requests.post(
        RASA_SERVER_URL,
        json=request.get_json(),
        headers={'Content-Type': 'application/json'}
    )
    print("res from POST------------",response.json())
    return jsonify(response.json())


@app.route('/get', methods=['GET'])
def get_bot_response():
    userText = request.args.get('msg')
    response = requests.post(
        RASA_SERVER_URL,
        json={"message": userText},
        headers={'Content-Type': 'application/json'}
    )
    #print response here
    print("res from GET------------",response.json())
    return jsonify(response.json())


# Function to generate response text with today's date
def generate_response(template_text):
    today_date = datetime.now().strftime("%d %B %Y")  # Format: Day Month Year
    return template_text.replace("[Today's Date]", today_date)

# Example usage
template_text = "Your appointment has been confirmed for today, [Today's Date], at [Appointment Time]."
response_text = generate_response(template_text)

# print("Time from app.py ---------", response_text)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000) # Run the server on a different port than Rasa's
