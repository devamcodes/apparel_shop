category = ["Tshirt", "Shirt", "Jacket"]
size_1 = ["Small"]
size_2 = ["Medium"]
size_3 = ["Large"]
size = list[input("ENTER THE SIZE:")]
size.append(size_1)
size.append(size_2)
size.append(size_3)
colour_1 = ["Red"]
colour_2 = ["Green"]
colour_3 = ["Blue"]
colour = list[input("ENTER THE COLOUR:")]
colour.append(colour_1)
colour.append(colour_2)
colour.append(colour_3)

user_input =[input("ENTER THE ITEM NAME:")]
Type=[]
user_input.append(Type)

apperel = {
    Type: category[i],
    size: size_1[i],
    size: size_2[i],
    size: size_3[i],
    colour: colour_1[i],
    colour: colour_2[i],
    colour: colour_3[i]
    for i in range(len(category and size and colour)):
        }
print(apperel)
