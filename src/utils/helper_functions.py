def format_message(message):
    """Format the message for output."""
    return f"Message: {message}"

def log_event(event):
    """Log events for debugging purposes."""
    with open("event_log.txt", "a") as log_file:
        log_file.write(f"{event}\n")