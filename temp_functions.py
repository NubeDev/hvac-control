def in_temp_range(min_temp, max_temp, temp):
    if temp is None or temp == '':
        return False
    if float(temp) < min_temp or float(temp) > max_temp:
        return False
    else:
        return True


def current_humid():
    r = 55
    return r


def current_temp():
    r = 22
    return r


def sp():
    r = 22
    return r


def clg_offset():
    r = 1
    return r


def htg_offset():
    r = 1
    return r


def t_stat():
    temp = current_temp()
    set_point = sp()
    clg_sp = set_point + clg_offset()
    htg_sp = set_point - htg_offset()
    ht_mode = False
    clg_mode = False
    if temp < htg_sp:
        ht_mode = True
        clg_mode = False
    elif temp > clg_sp:
        clg_mode = True
        ht_mode = False
    elif (clg_mode and temp < set_point) or (ht_mode and temp > set_point):
        clg_mode = False
        ht_mode = False
    return {"clg_mode": clg_mode, "ht_mode": ht_mode}
