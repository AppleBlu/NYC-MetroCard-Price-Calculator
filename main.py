import customer
import metro_card
import art
import os

is_on = True

def user_choice2():
    global is_on
    user_option = input("Are you finished?(yes/no): ")
    if user_option == 'yes':
        exit()
    elif user_option == 'no':
        application()
    else:
        print('Sorry try again')

def user_choice():
    global is_on
    user_option = input("Do you want to continue?(yes/no): ")
    if user_option == 'yes':
        application()
    elif user_option == 'no':
        print("Thank you and hope to see you soon!")
        exit()
    else:
        print('Sorry try again')
        


def application():
    while is_on:
        print(art.metro_menu)
        print(input('Press enter to start!'))
        print("-----------------------------------------------------------")
        print("Please, choose the option")
        print("1. See the amount of available tickets for each destination")
        print("2. See the available destinations")
        print("3. Make a ticket purchase")
        print("4. Exit")
        print("-----------------------------------------------------------")

        customer_option = input("Enter your option here: ")

        if customer_option == '1':
            metro_card.MetroCard.print_destination_to_tickets()
            user_choice()
        elif customer_option == '2':
            metro_card.MetroCard.print_locations()
            user_choice()
        elif customer_option == '3':
            customer.Customer.purchase_tickets()
            user_choice2()
        elif customer_option == '4':
            print("Thank you and hope to see you soon!")
            exit()
        else:
            print("Wrong input")
            print('Please restart the process \nProgram restarting...')
            exit()


application()
