COLOUR_TO_HEX = {'Absolute Zero': '#0048ba', 'Alice Blue': '#f0f8ff', 'Aqua': '#fbceb1', 'Baby Blue': '#89cff0', 'Banana Yellow': '#ffe135',
                'Black': '#000000', 'Brown1': '#ff4040', 'Burlywood1': '#ffd39b', 'Chartreuse1': '#7fff00', 'Cherry Blossom Pink': '#ffb7c5'}

colour_name = input('Enter Color: ').title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input('Enter Colour: ').title()

