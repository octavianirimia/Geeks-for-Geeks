"""
Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates, top left and bottom right.
So mainly we are given following four coordinates. 
l1: Top Left coordinate of first rectangle. 
r1: Bottom Right coordinate of first rectangle. 
l2: Top Left coordinate of second rectangle. 
r2: Bottom Right coordinate of second rectangle.
"""

def do_overlap(l1x, l1y, r1x, r1y, l2x, l2y, r2x, r2y) -> bool:

    if l1x > r2x or l2x > r1x:
        return False
    
    if r1y > l2y or r2y > l1y:
        return False
    
    return True


if __name__ == "__main__":
    l1x = 0
    l1y = 10
    r1x = 10
    r1y = 0
    
    l2x = 5
    l2y = 5
    r2x = 15
    r2y = 0

    print(do_overlap(l1x, l1y, r1x, r1y, l2x, l2y, r2x, r2y))
