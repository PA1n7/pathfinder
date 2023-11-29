def get_fraction(num:float):
    num = abs(num)
    top = 1
    bot = 1
    div = 0
    while div != num:
        div = top/bot
        if abs(div-num) < 1:
            break
        if div < num:
            top+=1
        if div > num:
            bot+=1
    return [top, bot]
    