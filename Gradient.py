import os
def GetLinearRule(cord1, cord2):
    """args must be in tuple or list of 2 values for each:
    cord1: (x1, y1), cord2: (x2, y2)"""

    perfect_vertical = False
    perfect_horizontal = False

    if cord1[0] == cord2[0] and cord1[1] != cord2[1]:
        gradient = 0
        perfect_vertical = True

    elif cord1[1] == cord2[1] and cord1[0] != cord2[0]:
        gradient = 0
        perfect_horizontal = True

    else:
        gradient = float((cord2[1] - cord1[1]) / (cord2[0] - cord1[0]))

    c = cord1[1] - (cord1[0] * gradient)

    if perfect_vertical == True:
        return(f"x = {cord1[0]}")
    
    elif perfect_horizontal == True:
        return(f"y = {cord1[1]}")
    
    else:
        return(f"y = {gradient}x + {c}")

def GetInput():
    user_input = input("Input in THIS format, cuz im too lazy to do input validation: x1 y1 x2 y2: ")
    user_input = user_input.lower().split()
    cords1 = (int(user_input[0]), int(user_input[1]))
    cords2 = (int(user_input[2]), int(user_input[3]))
    return(cords1, cords2)

while True:
    os.system("cls")
    try:
        cordset1, cordset2 = GetInput()
        print(GetLinearRule(cordset1, cordset2))
    except:
        print("Invalid Input!")
    input("'ENTER' to continue")