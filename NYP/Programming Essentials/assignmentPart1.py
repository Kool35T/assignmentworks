vendor = input('Are you a vendor (Y/N)? ').upper()
if vendor == 'N':
    print('Welcome to ABC Vending Machine.')
    print('Select from the following choices to continue:')
    print('IM. Iced Milo (S$1.5)')
    print('HM. Hot Milo (S$1.2)')
    print('IC. Iced Coffee (S$1.5)')
    print('HC. Hot Coffee (S$1.2)')
    print('1P. 100 Plus (S$1.1)')
    print('CC. Coca Cola (S$1.3)')
    print('0. Exit / Payment')
    price = 0
    noOfChoices = 0
    while True:
        choice = input('Enter Choice: ').upper()
        if choice == 'IM':
            price += 1.5
            noOfChoices += 1
        elif choice == 'HM':
            price += 1.2
            noOfChoices += 1
        elif choice == 'IC':
            price += 1.5
            noOfChoices += 1
        elif choice == 'HC':
            price += 1.1
            noOfChoices += 1
        elif choice == '1P':
            price += 1.1
            noOfChoices += 1
        elif choice == 'CC':
            price += 1.3
            noOfChoices += 1
        elif choice == '0':
            if price == 0:
                print('No drinks selected')
            else:
                print('Please pay: ${:.2f}'.format(price))
            break
        else:
            print("Invalid option")
        print('No of drinks selected = ', noOfChoices)
    if noOfChoices > 0:
        while True:
            payment = 0
            print('Indicate your payment: ')
            pay = int(input('Enter no. of $10 notes: '))
            payment += 10 * pay
            if payment < price:
                pay = int(input('Enter no. of $5 notes:'))
                payment += 5 * pay
                if payment < price:
                    pay = int(input('Enter no. of $2 notes:'))
                    payment += 2 * pay
                    if payment < price:
                        print('Not enough to pay for the drinks')
                        print('Take back your cash!')
                        cancel = input('Do you want to cancel the purchase? Y/N: ').upper()
                        if cancel == 'Y':
                            print('Purchase is cancelled. Thank you.')
                            break
                    elif payment >= price:
                        change = payment - price
                        print('Please collect your change: ${:.2f}'.format(change))
                        print('Drinks paid. Thank you.')
                        break
                elif payment >= price:
                    change = payment - price
                    print('Please collect your change: ${:.2f}'.format(change))
                    print('Drinks paid. Thank you.')
                    break
            elif payment >= price:
                change = payment - price
                print('Please collect your change: ${:.2f}'.format(change))
                print('Drinks paid. Thank you.')
                break
elif vendor == 'Y':
    print('Welcome to ABC Vending Machine.')
    print('Select from the following choices to continue:')
    print('1. Add Drink Type')
    print('2. Replenish Drink')
    print('0. Exit')
    while (True):
        choice = input('Enter Choice: ').upper()
