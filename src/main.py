from connectors.whatsapp_connector import WhatsAppConnector
from services.automation_service import AutomationService
from insights.insights_generator import InsightsGenerator

def main():
    # Initialize the WhatsApp connector
    whatsapp_connector = WhatsAppConnector()
    whatsapp_connector.connect()

    # Initialize the automation service
    automation_service = AutomationService()

    # Initialize the insights generator
    insights_generator = InsightsGenerator()

    # Main loop to handle incoming messages
    while True:
        incoming_message = whatsapp_connector.receive_message()
        if incoming_message:
            # Process the incoming message
            response = automation_service.automate_process(incoming_message)
            whatsapp_connector.send_message(response)

            # Generate insights based on the interaction
            insights = insights_generator.generate_insight(incoming_message)
            print(insights)

if __name__ == "__main__":
    main()