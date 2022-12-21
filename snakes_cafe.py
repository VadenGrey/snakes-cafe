from textwrap import dedent

def show_menu():
    print(dedent('''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    
    ***********************************
    ** What would you like to order? **
    ***********************************'''))

    order_dict = {
        'Wings': 0,
        'Cookies': 0,
        'Spring Rolls': 0,
        'Salmon': 0,
        'Steak': 0,
        'Meat Tornado': 0,
        'A Literal Garden': 0,
        'Ice Cream': 0,
        'Cake': 0,
        'Pie': 0,
        'Coffee': 0,
        'Tea': 0,
        'Unicorn Tears': 0
    }

    while True:
        ordered_item = input('> ')
        if ordered_item in order_dict:
            order_dict[ordered_item] += 1
            if order_dict[ordered_item] > 1:
                print(f'** {order_dict[ordered_item]} orders of {ordered_item} have been added to your meal **')
            else:
                print(f'** 1 order of {ordered_item} have been added to your meal **')
        if ordered_item == 'quit':
            break
        if ordered_item not in order_dict:
            print("Sorry, that item isn't on the menu")


    for item in list(order_dict):
        if order_dict[item] == 0:
             del order_dict[item]

    print(f'Your order is {order_dict}')

show_menu()