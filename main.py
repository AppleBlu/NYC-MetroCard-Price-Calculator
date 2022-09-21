# importing modules and files
import customer
import metro_card
import art

# checking if the machine is on
is_on = True

# creating a function to see if the user is finished or not
def user_choice2():
    global is_on
    user_option = input("Are you finished?(yes/no): ")
    if user_option == 'yes':
        print("Thank you and hope to see you soon!")
        exit()
    elif user_option == 'no':
        application()
    else:
        print('Sorry try again')

# creating a function to see if the user wants to continue or not
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
    
# creating the application with the menu that the user can interact with
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
