import metro_card


class Customer:
    money_in_cash = 30
    card_pin_number = '123456789'
    

    def __init__(self):
        self.ticket_amount = None



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


        print(input('Press enter to print recipet'))
        print('Please hold while your recipet is printed...')
        print('\n----------------------------\n')
        print('One way ticket to: {destination}\n'.format(destination = title_location))
        print('Purchased on: ####')
        print('Valid till: ####')
        print('Amount paid: #### using ####')
        print('----------------------------')




        #add time
        #add 2way
        #add card fee
        #add wrong number of tickets
        # print multiple recipets for multiple tickets selected
