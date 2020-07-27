my_dict = {"T-shirt": {"size": ["Small", "Medium", "Large"], "Colour": ["Red", "Blue", "Green"]},
           "Shirt": {"size": ["Small", "Medium", "Large"], "Colour": ["Red", "Blue", "Green"]},
           "Jacket": {"size": ["Small", "Medium", "Large"], "Colour": ["Red", "Blue", "Green"]}}
for key in my_dict:
    chioce = input("ENTER THE TYPE:")
    print(f"in {key} there are three sizes and three colours ")
    print(my_dict[key])

print(my_dict)
