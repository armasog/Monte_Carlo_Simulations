import matplotlib.pyplot as plt

'''A simple Monte Carlo machine which takes a game as an input.'''

def monte_carlo_machine(game, *game_vars, iterations=1000000, plot=True):
    profit_per_trial = []
    profitable_trials = 0
    for i in range(iterations+1):
        profit_per_trial.append(game(*game_vars))
    for j in profit_per_trial: # Count the number of trials where there is a negative profit
        if j > 0:
            profitable_trials += 1
    if plot:
        plt.hist(profit_per_trial)

        plt.show()
    return float(profitable_trials/iterations)

