def is_valid_walk(walk):
    if 'n' in walk and len(set(walk)) <= 2:
        if walk.count('n') == walk.count('s') and len(walk) == 10:
            return True
    if 'w' in walk and len(set(walk)) <= 2:
        if walk.count('w') == walk.count('e') and len(walk) == 10:
            return True
    if len(set(walk)) > 2:
        if (walk.count('w') == walk.count('e') and walk.count('n') == walk.count('s')) and len(walk) == 10:
            return True

    return False

