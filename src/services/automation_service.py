class AutomationService:
    def __init__(self):
        self.process_status = {}

    def automate_process(self, user_input):
        # Implement automation logic based on user input
        # For example, trigger specific tasks or workflows
        self.process_status[user_input] = "In Progress"
        # Logic to perform the automation task
        # Update status once completed
        self.process_status[user_input] = "Completed"

    def get_status(self, user_input):
        # Retrieve the current status of the specified process
        return self.process_status.get(user_input, "Not Found")