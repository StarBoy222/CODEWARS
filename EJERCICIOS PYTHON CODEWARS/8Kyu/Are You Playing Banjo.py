def areYouPlayingBanjo(name):
    # Implement me!
    if (name[0] == "r") or (name[0] == "R"):
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name
