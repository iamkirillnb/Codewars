def bouncing_ball(h, bounce, window):
    if not 0 < bounce < 1:
        return -1
    else:
        cnt = 0
        while h > window:
            cnt +=1
            h *= bounce
            if h > window:
                cnt += 1
    return cnt or -1