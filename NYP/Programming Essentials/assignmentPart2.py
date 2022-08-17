import sys

drinks = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 5},
          'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 13},
          'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 4},
          'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': '***out of stock***'},
          '1P': {'description': '100 plus', 'price': 1.1, 'quantity': 9},
          'CC': {'description': 'Coca cola', 'price': 1.3, 'quantity': 10}}

def add_drink_type(drink_id, description, price, quantity):
    drinks[drink_id]= {'description': description, 'price': price, 'quantity': quantity}

def replenish_drink(drink_id, quantity):
    if type(drinks[drink_id]['quantity']) == str:
        drinks[drink_id]['quantity'] = quantity
    else:
        drinks[drink_id]['quantity'] += quantity
    print('{} has been top up!'.format(drink_id))


while True:
    vendor = input('Are you a vendor (Y/N)? ').upper()
    if vendor == 'N':
        print('Welcome to ABC Vending Machine.')
        print('Select from the following choices to continue:')
        for i in drinks:
            if type(drinks[i]['quantity']) == str:
                print('{}. {} (${:.1f}) \t {}'.format(i, drinks[i]['description'], drinks[i]['price'], drinks[i]['quantity']))
            else:
                print('{}. {} (${:.1f}) \t QTY: {}'.format(i,drinks[i]['description'],drinks[i]['price'], drinks[i]['quantity']))
        print('0. Exit / Payment')
        price = 0
        noOfChoices = 0
        purchase = {}
        for i in drinks:
            purchase[i] = 0
        while True:
            choice = input('Enter Choice: ').upper()
            if choice in drinks or choice == '0':
                if choice == '0':
                    if price == 0:
                        print('No drinks selected')
                    else:
                        print('Please pay: ${:.2f}'.format(price))
                    break
                elif type(drinks[choice]['quantity']) == str:
                    print('{} is out of stock'.format(drinks[choice]['description']))
                    continue
                elif drinks[choice]['quantity'] == purchase[choice]:
                    print('{} is out of stock'.format(drinks[choice]['description']))
                    continue
                elif choice in drinks:
                    price += drinks[choice]['price']
                    noOfChoices += 1
                    purchase[choice] += 1
                print('No of drinks selected = ', noOfChoices)
            else:
                print('Invalid Option')
        if noOfChoices > 0:
            while True:
                payment = 0
                print('Indicate your payment: ')
                while True:
                    try:
                        pay = int(input('Enter no. of $10 notes: '))
                        break
                    except:
                        print('invalid input')
                        continue
                payment += 10*pay
                if payment < price:
                    while True:
                        try:
                            pay = int(input('Enter no. of $5 notes:'))
                            break
                        except:
                            print('invalid input')
                            continue
                    payment += 5*pay
                    if payment < price:
                        while True:
                            try:
                                pay = int(input('Enter no. of $2 notes:'))
                                break
                            except:
                                print('invalid input')
                                continue
                        payment += 2*pay
                        if payment < price:
                            print('Not enough to pay for the drinks')
                            print('Take back your cash!')
                            cancel = input('Do you want to cancel the purchase? Y/N: ').upper()
                            if cancel == 'Y':
                                print('Purchase is cancelled. Thank you.')
                                purchase = {}
                                break
                        elif payment >= price:
                            change = payment - price
                            print('Please collect your change: ${:.2f}'.format(change))
                            print('Drinks paid. Thank you.')
                            for i in drinks:
                                if drinks[i]['quantity'] == purchase[i]:
                                    drinks[i]['quantity'] = '***out of stock***'
                                elif str(drinks[i]['quantity']).isdigit():
                                    drinks[i]['quantity'] -= purchase[i]
                            print(drinks)
                            break
                    elif payment >= price:
                        change = payment - price
                        print('Please collect your change: ${:.2f}'.format(change))
                        print('Drinks paid. Thank you.')
                        for i in drinks:
                            if drinks[i]['quantity'] == purchase[i]:
                                drinks[i]['quantity'] = '***out of stock***'
                            elif str(drinks[i]['quantity']).isdigit():
                                drinks[i]['quantity'] -= purchase[i]
                        print(drinks)
                        break
                elif payment >= price:
                    change = payment - price
                    print('Please collect your change: ${:.2f}'.format(change))
                    print('Drinks paid. Thank you.')
                    for i in drinks:
                        if drinks[i]['quantity'] == purchase[i]:
                            drinks[i]['quantity'] = '***out of stock***'
                        elif str(drinks[i]['quantity']).isdigit():
                            drinks[i]['quantity'] -= purchase[i]
                    sys.exit()




    elif vendor == 'Y':
        print('Welcome to ABC Vending Machine.')
        print('Select from the following choices to continue:')
        print('1. Add Drink Type')
        print('2. Replenish Drink')
        print('0. Exit')
        while True:
            try:
                choice = int(input('Enter Choice: '))
            except ValueError:
                print('invalid input')
                continue
            if choice == 1:
                while True:
                    drink_id = input('Enter drink id: ').upper()
                    if drink_id in drinks:
                        print('Drink id exists!')
                    else:
                        description = input('Enter description of drink: ')
                        while True:
                            try:
                                price = float(input('Enter price: '))
                                break
                            except ValueError:
                                print('invalid input')
                                continue
                        while True:
                            try:
                                quantity = int(input('Enter quantity: '))
                                break
                            except ValueError:
                                print('invalid input')
                                continue
                        add_drink_type(drink_id, description, price, quantity)
                        break

            elif choice == 2:
                for i in drinks:
                    if type(drinks[i]['quantity']) == str:
                        print('{}. {} (${:.1f}) \t {}'.format(i, drinks[i]['description'], drinks[i]['price'], drinks[i]['quantity']))
                    else:
                        print('{}. {} (${:.1f}) \t QTY: {}'.format(i, drinks[i]['description'], drinks[i]['price'], drinks[i]['quantity']))
                while True:
                    drink_id = input('Enter drink id: ').upper()
                    if drink_id not in drinks:
                        print('No drink with this drink id. Try again.')
                    else:
                        if type(drinks[drink_id]['quantity']) == str or drinks[drink_id]['quantity'] <=5:
                            try:
                                quantity = int(input('Enter quantity: '))
                            except ValueError:
                                print('invalid input')
                                continue
                        else:
                            print('No need to replenish. Quantity is greater than 5.')
                            break
                        replenish_drink(drink_id, quantity)
                        break

            elif choice == 0:
                break
            else:
                print('Invalid input')

    else:
        print('Invalid input')




