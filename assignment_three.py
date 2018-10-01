# Yerim-Oumar Dia
# October 1,2018
# Introduction to Computer Science
# This program uses different functions and one main function
# The program draws a flower shape made out of hexagons.
# The center color is different from the petal colors.
# Depending on what the user inputs, the program will react accordingly.

import turtle


def get_side_length():
    """
    This function gets the desired side of the hexagon from the user
    :return: side of the hexagon as a float
    """
    side = input("How big do you want the side of the hexagon?")
    return float(side)


def get_center_color():
    """
    This function gets the color of the center hexagon from user. Assuming user inputs correct color.
    :return: returns the center color of the hexagon as a string
    """
    center_color = input("What color do you want the center hexagon?")
    return str(center_color)


def get_petal_color():
    """
    This function gets petal color from user as long as color is entered correctly
    :return: returns petal color of the hexagons as a string
    """
    petal_color = input("What color do you want the petals?")
    return str(petal_color)


def draw_hexagon(side, color):
    """
    This function defines the movement of turtle and how to fill in the colors of the hexagons
    :param side: length of hexagon
    :param color: filling the hexagon in
    :return: none
    """
    turtle.color(color)
    turtle.begin_fill()

    for x in range(6):
        turtle.forward(side)
        turtle.left(60)
    turtle.forward(side)
    turtle.end_fill()


def main():
    length = get_side_length()
    center_color = get_center_color()
    petal_color = get_petal_color()
    draw_hexagon(length, petal_color)
    for x in range(5):
        turtle.right(60)
        draw_hexagon(length, petal_color)
    turtle.right(180)
    draw_hexagon(length, center_color)


    turtle.exitonclick()


main()
