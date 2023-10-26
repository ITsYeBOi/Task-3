# booking_utils.py

from datetime import datetime
import uuid

def calculate_ticket_price(ticket_quantity):
    # Implement the logic to calculate the total price based on the ticket quantity
    # For example, if a ticket costs $50 each, you can calculate the total price like this:
    ticket_price = 50  # Adjust the actual ticket price
    type_addon = 0 # ticktype addon
    total_price = ticket_price * ticket_quantity
    return total_price


def generate_booking_reference(event, user):
    unique_id = uuid.uuid4().hex[:8]  # Generate a unique ID
    booking_reference = f"{user.id}-{event.id}-{unique_id}"
    return booking_reference
