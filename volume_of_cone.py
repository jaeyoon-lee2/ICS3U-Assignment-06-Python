#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program calculates the volume of cone


import math


def calculate_volume(radius, height):
    # this function calculate the volume of cone

    # process
    volume = 1/3 * math.pi * (radius**2) * height

    return volume


def main():
    # this function gets radius and height

    # input
    radius = input("Enter the radius of cone (metre): ")
    height = input("Enter the height of cone (metre): ")

    try:
        radius_as_int = int(radius)
        height_as_int = int(height)
        if radius_as_int > 0 and height_as_int > 0:
            volume = calculate_volume(height=height_as_int,
                                      radius=radius_as_int)
            print("The volume of cone is {} m³".format(volume))
        else:
            print("Those numbers are minus")
    except Exception:
        print("Those are not integers")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
