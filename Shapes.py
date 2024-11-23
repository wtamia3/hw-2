import math

def rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """

    return length * width

def triangle_area(base, height):
    """Calculates the area of a triangle.

    Args:
        base: The base of the triangle.
        height: The height of the triangle.

    Returns:
        The area of the triangle.
    """

    return 0.5 * base * height

def circle_area(radius):
    """Calculates the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """

    return math.pi * radius**2
