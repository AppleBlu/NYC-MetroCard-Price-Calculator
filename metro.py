class MetroCard():
    tickets_for_destination = {'Midtown': 10, 'Central Park': 4, 'Metropolitan Museum of Art': 1}
    price_of_ticket = {'Midtown': 4.32, 'Central Park': 2.43, 'Metropolitan Museum of Art': 8.64}

    def __init__(self):
        self.destination = 'Midtown'
        self.price = MetroCard.price_of_ticket.get(self.destination)
        self.tickets = MetroCard.tickets_for_destination.get(self.destination)

    def get_price():
        prices = MetroCard.price_of_ticket
        for key, value in prices.items():
            return value
    
    def get_destinations():
        for key, value in MetroCard.tickets_for_destination.items():
            return key

    def __repr__(self):
        
        return '''The price to travel to {destination} is {price}
There are {tickets} remaining tickets to travel to {destination}.
        '''.format(destination = self.destination, tickets = self.tickets, price = self.price)