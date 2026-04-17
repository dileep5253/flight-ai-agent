def search_flights(from_city, to_city, date):
    # still mock data (we'll improve later)
    return [
        {"airline": "IndiGo", "price": 4500},
        {"airline": "Air India", "price": 5200},
        {"airline": "Vistara", "price": 4800},
        {"airline": "SpiceJet", "price": 4300},
        {"airline": "Go First", "price": 4100},
        {"airline": "Akasa Air", "price": 4600},
        {"airline": "AirAsia", "price": 4400},
        {"airline": "Alliance Air", "price": 3900},
        {"airline": "Star Air", "price": 4200},
        {"airline": "TruJet", "price": 4700}
    ]


def get_cheapest(flights):
    return min(flights, key=lambda x: x['price'])


# 🔹 TAKE INPUT FROM USER
from_city = input("Enter From City: ")
to_city = input("Enter Destination City: ")
date = input("Enter Date: ")

# 🔹 PROCESS
flights = search_flights(from_city, to_city, date)
cheapest = get_cheapest(flights)

# 🔹 OUTPUT
print("\nSearching flights from", from_city, "to", to_city, "on", date)

print("\nCheapest Flight:")
print("Airline:", cheapest["airline"])
print("Price:", cheapest["price"])

from email_service import send_email

# after cheapest calculation
user_email = input("Enter your email: ")

send_email(user_email, cheapest["airline"], cheapest["price"])

print("\nTicket details sent to your email ✅")

from agent import ai_agent

user_input = input("Enter your request: ")
email = input("Enter your email: ")

result = ai_agent(user_input, email)

print("\nTicket Booked:")
print(result)

from ai_agent_llm import ai_agent_llm

user_input = input("Enter your request: ")
email = input("Enter your email: ")

result = ai_agent_llm(user_input, email)

print("\nTicket Booked:")
print(result)