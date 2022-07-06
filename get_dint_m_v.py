from numba import njit

@njit
def get_mv(tier, player_int, enemy_int):
    #
    # Determine the M and V values to use based on dINT and ninjutsu skill
    #
    # The M and V values were determined through my testing, which I present in this thread:
    # https://www.ffxiah.com/forum/topic/56749/updated-ninjutsu-damage-formulae
    #
    dINT = player_int - enemy_int

    if tier==1:
        if dINT <= -9:
            m=0.00; v=11.0
        elif dINT <= -1:
            m=0.50; v=16.0
        elif dINT <= 24:
            m=1.00; v=16.0
        elif dINT <= 74:
            m=0.50; v=28.5
        else:
            m=0.00; v=66.0

    elif tier==2:
        if dINT <= -43:
            m=0.00; v=47.0
        elif dINT <= -1:
            m=0.50; v=69.0
        elif dINT <= 112:
            m=1.00; v=69.0
        elif dINT <= 338:
            m=0.50; v=125.5
        else:
            m=0.00; v=295.0

    elif tier==3:
        if dINT <= -53:
            m=0.00; v=81.0
        elif dINT <= 1:
            m=1.00; v=134.0
        elif dINT <= 353:
            m=1.50; v=134.0
        else:
            m=0.00; v=655.0

    return(m,v)
