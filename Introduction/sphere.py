"""
A reusable module that provides functions for computing
properties of a sphere: diameter, circumference, surface area, and volume.
By taking the radius as input
"""

import math


def diameter(r: float):
    """Return the diameter of a sphere."""
    return 2 * r


def circumference(r: float):
    """Return the great-circle circumference of a sphere."""
    return 2 * math.pi * r


def surface_area(r: float):
    """Return the surface area of a sphere."""
    return 4 * math.pi * r**2


def volume(r: float):
    """Return the volume of a sphere."""
    return (4/3) * math.pi * r**3


# Enforce input must be float: (optional)
"""
def diameter(r: float) -> float:
    if not isinstance(r, (float, int)):
        raise TypeError("r must be a number")

    return 2 * float(r)
"""

# Standalone usage
if __name__ == "__main__":
    r = float(input("Enter the radius of the sphere: "))

    print(f"Diameter: {diameter(r):.4f}")
    print(f"Circumference: {circumference(r):.4f}")
    print(f"Surface Area: {surface_area(r):.4f}")
    print(f"Volume: {volume(r):.4f}")

