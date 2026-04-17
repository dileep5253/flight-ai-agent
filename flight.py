def search_flights(from_city, to_city, date):
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

def get_expensive(flights):
    return max(flights, key=lambda x: x['price'])