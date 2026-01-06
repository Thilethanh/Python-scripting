def calculate_experience_points(level):
    XP = 0
    for i in range(level-1, 0, -1):
        XP += i*5
    return XP 
