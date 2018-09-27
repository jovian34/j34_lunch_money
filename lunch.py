def calc_add(money, bonus_amt):
    xander = BONUS + money[2] + money[1] - 2 * money[0]
    xander = xander / 3
    new_total = xander + money[0]
    tristan = new_total - money[2]
    madison = new_total - money[1]
    return [xander, madison, tristan]


def round_to_100ths(number):
    text = f'{number:.2f}'
    return float(text)


def fix_rounding(money_add, bonus_amt):
    ''' deals with edge case where rounding makes total
    money added less than the amount required to earn
    the bonus by adding the difference (never more than 3 cents)
    to Xander's total.'''
    total = 0
    for money in money_add:
        total += money
    if total < bonus_amt:
        differnce = bonus_amt - total
        money_add[0] = money_add[0] + differnce
    return money_add


def fix_negative(money, bonus_amt):
    '''deals with common edge case of values being negative
    this function reduces the other 2 evenly since a negative
    value cannot be keyed'''
    for i in range(0, len(money)):
        if money[i] < 0:
            diff = 0 - money[i]
            diff = diff / 2
            money = [diff + kid for kid in money]
            money[i] = 0
    total = money[0] + money[1] + money[2]
    if total > bonus_amt:
        diff = total - bonus_amt
        diff = diff / 2
        for i in range(0, len(money)):
            if money[i] != 0:
                money[i] -= diff
    return money


def xander_input():
    global xander_current
    xander_current = input('How much does Xander have now? ')
    xander_bonus = input('How much bonus? ')
    xander_current = float(xander_current) + float(xander_bonus)


def madison_input():
    global madison_current
    madison_current = input('How much does Madison have now? ')
    madison_bonus = input('How much bonus? ')
    madison_current = float(madison_current) + float(madison_bonus)


def tristan_input():
    global tristan_current
    tristan_current = input('How much does Tristan have now? ')
    tristan_bonus = input('How much bonus?')
    tristan_current = float(tristan_current) + float(tristan_bonus)


def print_results(xander_add, madison_add, tristan_add):
    print('===================================')
    print(f'Xander needs: ${xander_add:.2f}')
    print(f'Madison needs: ${madison_add:.2f}')
    print(f'Tristan needs: ${tristan_add:.2f}')


BONUS = 52.50


def main():
    xander_input()
    madison_input()
    tristan_input()

    money_list = [xander_current, madison_current, tristan_current]
    money_list = calc_add(money_list, BONUS)
    money_list = fix_negative(money_list, BONUS)
    money_list = [round_to_100ths(i) for i in money_list]
    fixed_tuple = tuple(fix_rounding(money_list, BONUS))
    xander_add, madison_add, tristan_add = fixed_tuple
    print_results(xander_add, madison_add, tristan_add)


if __name__ == "__main__":
    main()
