from flight import search_flights, get_cheapest, get_expensive
from email_service import send_email
import random


def extract_details(user_input):
    user_input = user_input.lower()

    source = "Hyderabad"

    if "delhi" in user_input:
        destination = "Delhi"
    elif "mumbai" in user_input:
        destination = "Mumbai"
    elif "bangalore" in user_input:
        destination = "Bangalore"
    else:
        destination = "Unknown"

    if "tomorrow" in user_input:
        date = "tomorrow"
    elif "monday" in user_input:
        date = "next monday"
    else:
        date = "next day"

    return {
        "source": source,
        "destination": destination,
        "date": date
    }


def book_ticket(flight):
    return {
        "airline": flight["airline"],
        "price": flight["price"],
        "status": "CONFIRMED",
        "pnr": "AI" + str(random.randint(10000, 99999))
    }


def ai_agent_llm(user_input, email):

    details = extract_details(user_input)

    from_city = details["source"]
    to_city = details["destination"]
    date = details["date"]

    print("\nExtracted Details:", details)

    flights = search_flights(from_city, to_city, date)

    # 🔹 Decision logic
    if "expensive" in user_input.lower() or "costly" in user_input.lower():
        selected_flight = get_expensive(flights)
        print("🔼 Selecting most expensive flight")
    else:
        selected_flight = get_cheapest(flights)
        print("🔽 Selecting cheapest flight")

    # 🔹 Booking
    ticket = book_ticket(selected_flight)

    # 🔹 Email
    send_email(email, ticket["airline"], ticket["price"])

    return ticket