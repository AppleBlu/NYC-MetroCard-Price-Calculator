# importing modules
from functools import total_ordering
import metro_card
from datetime import datetime

# creating a class for all things related to the customer
class Customer:
# creating class varibles for the customer
    money_in_cash = 30
    card_pin_number = '123456789'

# creating a function that runs through the process of purchasing a ticket    
    def purchase_tickets():
        
        ticket_amount = input("How many tickets do you want to buy?: ")
        ticket_location = input("Type your required destination below: ").lower()

        title_location = ticket_location.title()
        lower_location = ticket_location.lower()
        if lower_location in metro_card.MetroCard.un_capatalise_destinations():
            payment_method = input("Will you pay by card or cash?(card/cash): ")
            lower_payment = payment_method.lower()
            if lower_payment == 'card':
                pin = input('Please enter your pin below to proceed \n:')
                print('Checking...')
                if pin == Customer.card_pin_number:
                    print('PIN correct. Proceeding with payment...')
                else:
                    print("Incorrect PIN!")
                    print('Please restart the process \nProgram restarting...')
                    exit()

            elif payment_method == 'cash':
                print('Please enter coins.')
                if Customer.money_in_cash > int(metro_card.MetroCard.price_of_ticket.get(title_location)) * int(ticket_amount):
                    print('The correct amount has been entered')
                else:
                    print('You do not have enough cash')
        
        
        elif lower_location not in metro_card.MetroCard.destinations:
            print('Sorry we do not suply transport to that destination')
            print('Please restart the process \nProgram restarting...')
            exit()

# printing a recipet
        now = datetime.now()
        amount = metro_card.MetroCard.price_of_ticket.get(ticket_location.title())
        total_amount = amount * int(ticket_amount)
        print(input('Press enter to print recipet'))
        print('Please hold while your recipet is printed...')
        print('\n----------------------------\n')
        print('One way ticket to: {destination} x {tic}\n'.format(destination = title_location, tic = ticket_amount))
        print('Purchased: ' + str(now))
        print('Valid till: 24 hours after purchase')
        print('Amount paid: £{amount} using {pay}'. format(amount = total_amount, pay = payment_method))
        print('\n')
        print('----------------------------')
