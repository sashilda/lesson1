def format_price(price):
    int_price=int(price)
    result='price: {} rub.'.format(int_price)
    return result

display_price=format_price(56.24)
print(display_price)