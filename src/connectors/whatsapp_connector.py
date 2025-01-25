class WhatsAppConnector:
    def __init__(self, api_key, phone_number):
        self.api_key = api_key
        self.phone_number = phone_number
        self.connected = False

    def connect(self):
        # Logic to connect to WhatsApp API
        # For example, using a library like Twilio or WhatsApp Business API
        self.connected = True
        print("Connected to WhatsApp API")

    def send_message(self, recipient, message):
        if not self.connected:
            raise Exception("Connector is not connected. Please connect first.")
        # Logic to send a message to the recipient
        print(f"Message sent to {recipient}: {message}")

    def receive_message(self):
        if not self.connected:
            raise Exception("Connector is not connected. Please connect first.")
        # Logic to listen for incoming messages
        # This could be a blocking call or a webhook setup
        print("Listening for incoming messages...")