category = ["Tshirt", "Shirt", "Jacket"]
size_1 = ["Small"]
size_2 = ["Medium"]
size_3 = ["Large"]
size = []
size_1.append(size)
size_2.append(size)
size_3.append(size)
colour_1 = ["Red"]
colour_2 = ["Green"]
colour_3 = ["Blue"]
colour = []
colour_1.append(colour)
colour_2.append(colour)
colour_3.append(colour)

user_input =list[input("ENTER THE ITEM NAME:")]
Type=[]
user_input.append(Type)

apperel = {
    Type: category[i],
    size: size_1[i],
    size: size_2[i],
    size: size_3[i],
    colour: colour_1[i],
    colour: colour_2[i],
    colour: colour_3[i],
    for i in category and size and colour:}
print(apperel)