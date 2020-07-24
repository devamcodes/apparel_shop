"""
Project:
Author: Devam A

Discreption:

"""
"""
steps to be followed-
youare selling upper apperel
3 objects
3 sizes
3 colours
stock
dict(
     catagary-jacket(string)
     size-medium
     colur-yelllow
     )
stock-variable(starting=0)
functon -
add itemss
remove itmes
remove from stock (catagary)
operation
remaining stock
function-
display
warning for stock
"""
def add_items():#i dont think this is needed to be converted to dictionary
    add_option_catagery = input("ENTER THE NAME OF THE ITEM YOU WANT TO ADD IN THE STOCK:")
    add_option_size = input("ENTER THE SIZE OF THE APPEREL:")
    add_option_colour = input("ENTER THE COLOUR OF THE APPEREL:")
    dict(add_item())
    apperel_dict.add(add_item_dict)

def remove_item():#(continue)if this is for puchase purpose.
    remove_option_catagery = input("ENTER THE NAME OF THE ITEM YOU WANT TO REMOVE:")
    remove_option_size = input("ENTER THE SIZE OF THE APPEREL YOU WANT TO REMOVE")
    remove_option_colour = input("ENTER THE COLOUR OF THE APPEREL YOU WANT TO REMOVE:")
    dict(remove_item())

def remove_from_the_stock():#how to connect this with the stock dictionary
    if method == 1:
    remove_option_catagery = input("ENTER THE NAME OF THE ITEM YOU WANT TO REMOVE:")
    elif method == 2:
    remove_option_size = input("ENTER THE SIZE OF THE APPEREL YOU WANT TO REMOVE")
    elif method == 3:
    remove_option_colour = input("ENTER THE COLOUR OF THE APPEREL YOU WANT TO REMOVE:")
    else:
    print("INVALID INPUT.")

def display_stock():

    """
    call a function that return to the starting of this program.
    """
class Apperel_shop():
    def menu_options(self):
        add_items()
        remove_items()
        display_stock()
    print("WELCOME TO THE APPEREL SHOP!")
    print("WE HAVE THREE TYPES OF APPERELS IN HERE.")
"""use dictionary->
apperel = [{}]
print(apperel[input])"""
apperel_dict = [
        {"Type":["T-shirt", "Jacket", "Shirt"]},
        { "Size":["Small, Medium, Large"]},
        {"colour":["Red", "Blue", "Yellow"]}
                ]
print (list(apperel_dict))
input("THANK YOU COME AGAIN!!")
