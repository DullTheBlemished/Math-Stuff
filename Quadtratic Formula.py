def Solve(a, b, c):
    linear_coefficient_term = b * -1
    thing = (b ** 2) - (4 * a * c)
    bottom_half = 2 * a
    if thing < 0:
        return(None)
    discriminant = thing ** 0.5
    whole_top_half = linear_coefficient_term + discriminant
    whole_top_half2 = linear_coefficient_term - discriminant

    ans1 = whole_top_half / bottom_half
    ans2 = whole_top_half2 / bottom_half
    return(ans1, ans2)

print(Solve(1, -5, 6))