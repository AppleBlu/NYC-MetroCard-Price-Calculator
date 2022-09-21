# creating a class for all things realated to the metro card machine
class MetroCard:
    tickets_for_destination = {'Midtown': 10, 'Central Park': 4, 'Metropolitan Museum of Art': 1}
    price_of_ticket = {'Midtown': 4.32, 'Central Park': 2.43, 'Metropolitan Museum of Art': 8.64}
    destinations = list(tickets_for_destination.keys())
    prices = list(price_of_ticket.values())
    card_fee = 1

# creating a function to print locations
    def print_locations():
        for key, value in MetroCard.price_of_ticket.items():
            print(f"{key}: £{value}")

# creating a function to un capatalise locations and add it to a new list
    def un_capatalise_destinations():
        destinations_lower = []
        for i in MetroCard.destinations:
            destinations_lower.append(i.lower())
        return destinations_lower

# creating a funtion to print how many tickets are avalible for that destination
    def print_destination_to_tickets():
        for key, value in MetroCard.tickets_for_destination.items():
            print(f"There are {value} tickets avalible for destination: {key}")
