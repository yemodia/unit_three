def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area

def main():
    height = 9
    radius = 12

    volume_of_cylinder = area_of_circle(radius) * height
    print(" The volume of the cylinder is", volume_of_cylinder)

main()