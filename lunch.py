import logging


def lunch_log():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="lunch.log",
    )

    logging.debug("Debug")
    logging.info("Info")
    logging.warning("Warning")
    logging.error("Error")
    logging.critical("Critical")

def calc_add(money, bonus_amt):
    xander = BONUS + money[2] + money[1] - 2 * money[0]
    xander = xander / 3
    new_total = xander + money[0]
    tristan = new_total - money[2]
    pierre = new_total - money[1]
    return [xander, pierre, tristan]


def round_to_100ths(number):
    text = f'{number:.2f}'
    return float(text)


def blank_float(value: str):
    '''
    This converts any non-numerical entry like a blank return to be processed as a zero float value
    '''
    try:
        output = float(value)
    except(ValueError):
        output = 0.0
    return output


def fix_rounding(money_add: float, bonus_amt: float) -> float:
    ''' deals with edge case where rounding makes total
    money added less than the amount required to earn
    the bonus by adding the difference (never more than 3 cents)
    to Xander's total.'''
    total = 0
    for money in money_add:
        total += money
    if total < bonus_amt:
        difference = bonus_amt - total
        money_add[0] = money_add[0] + difference
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
    xander_current = blank_float(xander_current) + blank_float(xander_bonus)


def pierre_input():
    global pierre_current
    pierre_current = input('How much does Pierre have now? ')
    pierre_bonus = input('How much bonus? ')
    pierre_current = blank_float(pierre_current) + blank_float(pierre_bonus)


def tristan_input():
    global tristan_current
    tristan_current = input('How much does Tristan have now? ')
    tristan_bonus = input('How much bonus?')
    tristan_current = blank_float(tristan_current) + blank_float(tristan_bonus)


def print_results(xander_add, pierre_add, tristan_add):
    print('===================================')
    print(f'Xander needs: ${xander_add:.2f}')
    print(f'Pierre needs: ${pierre_add:.2f}')
    print(f'Tristan needs: ${tristan_add:.2f}')


BONUS = 52.50


def main():
    lunch_log()
    xander_input()
    pierre_input()
    tristan_input()

    money_list = [xander_current, pierre_current, tristan_current]
    money_list = calc_add(money_list, BONUS)
    money_list = fix_negative(money_list, BONUS)
    money_list = [round_to_100ths(i) for i in money_list]
    fixed_tuple = tuple(fix_rounding(money_list, BONUS))
    xander_add, pierre_add, tristan_add = fixed_tuple
    print_results(xander_add, pierre_add, tristan_add)


if __name__ == "__main__":
    main()
