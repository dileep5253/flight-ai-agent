from flight import search_flights, get_cheapest
from email_service import send_email
import random


def book_ticket(flight):
    pnr = "AI" + str(random.randint(10000, 99999))
    
    return {
        "airline": flight["airline"],
        "price": flight["price"],
        "status": "CONFIRMED",
        "pnr": pnr
    }


def ai_agent(user_input, email):

    user_input = user_input.lower()

    if "delhi" in user_input:
        to_city = "Delhi"
    elif "mumbai" in user_input:
        to_city = "Mumbai"
    elif "bangalore" in user_input:
        to_city = "Bangalore"
    else:
        print("❌ Please mention destination city clearly")
        return

    from_city = "Hyderabad"
    date = "tomorrow"

    flights = search_flights(from_city, to_city, date)
    cheapest = get_cheapest(flights)

    ticket = book_ticket(cheapest)

    send_email(email, ticket["airline"], ticket["price"])

    return ticket