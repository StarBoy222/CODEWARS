def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    if (fuel_left * mpg) >= distance_to_pump:
        lucky = True
    else:
        lucky = False
    return lucky