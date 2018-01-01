def cooldown(rage, cooldown, seconds):
    sign = None
    if rage == 0:
        return rage
    elif rage > 0:
        sign = True
        rage -= (cooldown * seconds)
    elif rage < 0:
        sign = False
        rage += (cooldown * seconds)
    if sign is not None:
        if (rage > 0 and sign is False) or \
           (rage < 0 and sign is True):
            rage = 0
    return rage
