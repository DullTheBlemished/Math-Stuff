"""see how this docstring is ugly compared to the others? thats cuz I made this one,
the other ones are made by Gemini, so yeah this is some random maths thign for midpoint
and thats about it - Hung"""
import numpy

def MidPoint(cord1, cord2):
    """Calculates the exact middle point between two 2D coordinates.

    Args:
        cord1 (tuple or list): The first coordinate as (x, y).
        cord2 (tuple or list): The second coordinate as (x, y).

    Returns:
        tuple: The midpoint coordinate as (x, y).
    """
    return(((cord1[0] + cord2[0]) / 2), ((cord1[1] + cord2[1]) / 2))

def Distance(cord1, cord2):
    """Calculates the Euclidean distance between two 2D coordinates.

    Args:
        cord1 (tuple or list): The first coordinate as (x, y).
        cord2 (tuple or list): The second coordinate as (x, y).

    Returns:
        float: The straight-line distance between the two points.
    """
    return(float(numpy.sqrt(((cord2[0] - cord1[0]) ** 2) + ((cord2[1] - cord1[1]) ** 2))))

def FindPointFromMidPoint(cord1, cord2, reverse = False):
    """Calculates the missing endpoint of a line segment given one endpoint and the midpoint.

    Args:
        cord1 (tuple): The known endpoint coordinate as (x, y).
        cord2 (tuple): The midpoint coordinate as (x, y).
        reverse (bool, optional): Flips the calculation direction. Defaults to False.

    Returns:
        tuple: The calculated missing endpoint coordinate as (x, y).
    """
    if reverse == False:
        return((cord2[0] + (cord2[0] - cord1[0])), (cord2[1] + (cord2[1] - cord1[1])))
    else:
        return((cord2[0] - (cord1[0] - cord2[0])), (cord2[1] - (cord1[1] - cord2[1])))
    
print(MidPoint())