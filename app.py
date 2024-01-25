from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle Twilio Request URL
@app.route('/twilio/webhook', methods=['POST'])
def twilio_webhook():
    # Process Twilio incoming message here
    # You can access the request data using request.form or request.json
    # For example, to access the message body:
    message_body = request.form.get('Body')
    
    # Your logic to handle the incoming message
    
    # Respond to Twilio request (optional)
    response = "Your response goes here"
    return jsonify({"message": response})

# Route to handle Twilio Fallback URL
@app.route('/twilio/fallback', methods=['POST'])
def twilio_fallback():
    # Process Twilio fallback request here if the Request URL fails to respond
    # You can access the request data using request.form or request.json
    # For example, to access the message body:
    message_body = request.form.get('Body')
    
    # Your logic to handle the fallback request
    
    # Respond to Twilio fallback request (optional)
    response = "Fallback response goes here"
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(debug=True)
