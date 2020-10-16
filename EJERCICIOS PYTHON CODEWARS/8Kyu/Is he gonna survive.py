def hero(bullets, dragons):
    if (bullets / 2) == dragons:
        Lucky = True
    elif (bullets / 2) > dragons:
        Lucky = True
    else:
        Lucky = False
    return Lucky