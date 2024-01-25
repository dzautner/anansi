from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

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

# Route to handle Twilio delivery status callback
@app.route('/twilio/status', methods=['POST', 'GET'])
def twilio_delivery_status():
    # Extract the relevant information from the Twilio callback
    message_sid = request.form.get('MessageSid')
    status = request.form.get('MessageStatus')

    # Process the delivery status notification
    # You can log the message status or take other actions based on it

    # For example, you can log the information
    print(f"Message SID: {message_sid}, Status: {status}")

    # Respond with a 200 OK status to acknowledge receipt
    return '', 200

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
