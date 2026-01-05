import math


def main():
    # Input: radius of the sphere
    r = float(input("Enter the radius of the sphere: "))

    # Calculations
    diameter = 2 * r
    circumference = 2 * math.pi * r
    surface_area = 4 * math.pi * r**2
    volume = (4/3) * math.pi * r**3

    # Output
    print(f"Diameter: {diameter:.4f}")
    print(f"Circumference: {circumference:.4f}")
    print(f"Surface Area: {surface_area:.4f}")
    print(f"Volume: {volume:.4f}")


if __name__ == "__main__":
    main()

