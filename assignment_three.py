import turtle

def get_side_length():
    side = input("How big do you want the side of the hexagon")
    return float(side)

def get_center_color():
    center_color = input("What color do you want the center hexagon?")
    return  str(center_color)

def get_petal_color():
    petal_color = input("What color do you want the petals")
    return str(petal_color)

def draw_hexagon(side, color):
    for x in range(6):
        turtle.forward(side)
        turtle.left(60)



def main():
    length = get_side_length()
    center_color = get_center_color()
    petal_color = get_petal_color()
    draw_hexagon(length, center_color)


main()
