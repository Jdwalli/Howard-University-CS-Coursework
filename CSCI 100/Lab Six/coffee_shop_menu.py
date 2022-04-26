# create a function called make_menu that takes two lists

def make_menu(names, prices):
    menu_prices = []
    for i in range(0, len(names)):
        menu_prices.insert(i, f"{names[i]}: ${prices[i]}")
    return menu_prices
