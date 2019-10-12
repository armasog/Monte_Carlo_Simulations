from random import choice
from slot_machine_config import lines, symbols, pay_table, pay_symbols

'''A simple slot machine simulation'''


def cycle_symbols(center_symbol, symbols, up_or_down):
    # Simulates cycling up or down a row of symbols in order to calculate lines based on the center line
    center_symbol_index = symbols.index(center_symbol)
    if up_or_down.lower() == "up":
        if center_symbol_index == 0:
            return symbols[len(symbols) - 1]
        else:
            return symbols[center_symbol_index-1]
    if up_or_down.lower() == "down":
        if center_symbol_index == len(symbols) - 1:
            return symbols[0]
        else:
            return symbols[center_symbol_index+1]


def spin(lines):
    global symbols
    # Center line
    spin_results = []
    line_1 = [choice(symbols[0]), choice(symbols[1]), choice(symbols[2])]
    spin_results.append(line_1)
    if lines > 5:
        return "This slot machine only accepts up to 5 lines"
    if lines > 1:
        # Upper horizontal line
        line_2 = [cycle_symbols(line_1[0], symbols[0], "up"),cycle_symbols(line_1[1], symbols[1], "up"), cycle_symbols(line_1[2], symbols[2], "up")]
        spin_results.append(line_2)
    if lines > 2:
        # Lower horizontal Line
        line_3 = [cycle_symbols(line_1[0], symbols[0], "down"),cycle_symbols(line_1[1], symbols[1], "down"), cycle_symbols(line_1[2], symbols[2], "down")]
        spin_results.append(line_3)
    if lines > 3:
        # Diagonal line from the left down to right
        line_4 = [cycle_symbols(line_1[0], symbols[0], "up"), line_1[1],
                  cycle_symbols(line_1[2], symbols[2], "down")]
        spin_results.append(line_4)
    if lines > 4:
        # Diagonal line from the right down to the left
        line_5 = [cycle_symbols(line_1[0], symbols[0], "down"), line_1[1],
                  cycle_symbols(line_1[2], symbols[2], "up")]
        spin_results.append(line_5)

    return spin_results


def payout_multiple(line):
    global pay_symbols, pay_table
    if line.count(pay_symbols['gold']) == 3:
        return pay_table['3_of_a_kind_gold']
    if line.count(pay_symbols['silver']) == 3:
        return pay_table['3_of_a_kind_silver']
    if line.count(pay_symbols['bronze']) == 3:
        return pay_table['3_of_a_kind_bronze']
    if line.count(line[0]) == 3:
        return pay_table['3_of_a_kind_any']
    if line.count(pay_symbols['gold']) == 2:
        return pay_table['2_of_a_kind_gold']
    if line.count(pay_symbols['silver']) == 2:
        return pay_table['2_of_a_kind_silver']
    if line.count(pay_symbols['bronze']) == 2:
        return pay_table['2_of_a_kind_bronze']
    if line.count(line[0]) == 2:
        return pay_table['2_of_a_kind_any']
    if line.count(pay_symbols['gold']) == 1:
        return pay_table['special_symbol_gold']
    if line.count(pay_symbols['silver']) == 1:
        return pay_table['special_symbol_silver']
    if line.count(pay_symbols['bronze']) == 1:
        return pay_table['special_symbol_bronze']
    return 0


def slot_machine_game(bet_per_line, lines):
    outcome = spin(lines)
    payout = 0
    for line in outcome:
        payout += (bet_per_line * payout_multiple(line))
    return payout - (bet_per_line * lines), outcome
