from random import randint, choice
from slot_machine_config import lines, symbols

'''A simple slot machine simulation'''

# TODO Give each spinner its own order for symbols

def spin(lines, symbols):
    # Center line
    spin_results = []
    line_1 = [choice(symbols), choice(symbols), choice(symbols)]
    spin_results.append(line_1)
    if lines > 5:
        return "This slot machine only accepts up to 5 lines"
    if lines > 1:
        # Upper horizontal line
        line_2 = [symbols[symbols.index(line_1[0]) - 1], symbols[symbols.index(line_1[1]) - 1],
                  symbols[symbols.index(line_1[2]) - 1]]
        spin_results.append(line_2)
    if lines > 2:
        # Lower horizontal Line
        line_3 = [symbols[symbols.index(line_1[0]) + 1], symbols[symbols.index(line_1[1]) + 1],
                  symbols[symbols.index(line_1[2]) + 1]]
        spin_results.append(line_3)
    if lines > 3:
        # Diagonal line from the left down to right
        line_4 = [symbols[symbols.index(line_1[0]) - 1], line_1[1],
                  symbols[symbols.index(line_1[2]) + 1]]
        spin_results.append(line_4)
    if lines > 4:
        # Diagonal line from the right down to the left
        line_5 = [symbols[symbols.index(line_1[0]) + 1], line_1[1],
                  symbols[symbols.index(line_1[2]) - 1]]
        spin_results.append(line_5)
    return spin_results

print(spin(lines, symbols))