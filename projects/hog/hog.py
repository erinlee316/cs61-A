"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"

    # initialize variables
    total = 0
    counter = 1
    sow_sad = False

    # keep looping through until max number of rolls achieved
    while counter <= num_rolls:
        roll = dice()

        # player landed on 1 and now has sow sad
        if roll == 1:
            sow_sad = True

        # player does not land on 1
        else:
            total = total + roll

        counter = counter + 1   

    # dice landed on 1, returns the current player's score as 1
    if sow_sad:
        return 1
    
    # dice never landed on 1, returns the current player's score as accumulated total
    return total
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    # initialize variable
    points = 0

    # player_score = ones place
    player_score = player_score % 10

    # opponent_score = tens place
    opponent_score = opponent_score // 10

    # ONLY if opponent_score has three or more digits (100+)
    while opponent_score > 10:
        opponent_score = opponent_score % 10
        
    new_points = 3 * abs(opponent_score - player_score)

    if new_points == 0:
        return 1

    return new_points
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"

    # apply boar brawl rule if no dice are rolled
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    
    # roll dice and return total score for turn
    else: 
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3



def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"

    # initialize variables
    counter = 1
    factors = 0

    # incrementing while loop checks to see if remainder exists
    # remainder exists, value is not a factor of n
    while counter <= n:
        if n % counter == 0:
            factors += 1
        counter += 1

    # return number of factors
    return factors
    # END PROBLEM 4



def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"

    # should recheck factors when score increases, but only need to check once
    # you should check for finding prime, factors no longer matter
    factors = num_factors(score)
    if (factors == 3 or factors == 4):
        while not is_prime(score):
            score += 1

    # return new score
    return score
    # END PROBLEM 4


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"

    # add current player's score to score after taking turn to find total score 
    total_score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    # print(player_score)
    # print(total_score)
    # print(take_turn(num_rolls, player_score, opponent_score, dice))
    return sus_points(total_score)
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    # keep playing until a player reached goal score of 100+
    while (score0 < goal and score1 < goal):

        # player 0's turn
        if who == 0:
            # take in number of dice player will roll that turn, player's score, opponent's score, and rolling dice
            # updates to new score
            score0 = update(strategy0(score0, score1), score0, score1, dice)

        # player 1's turn
        else:
            # take in number of dice player will roll that turn, player's score, opponent's score, and rolling dice
            # updates to new score
            score1 = update(strategy1(score1, score0), score1, score0, dice)

        # alternate between players
        who = 1 - who

    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"

    # always returns the same number of dice
    # current and opponent's score don't matter
    def strategy(current_player, opponent_player):
        return n
    
    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5
    

def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"

    # initialize variables
    current_score = 0
    opponent_score = 0
    beginning = strategy(0, 0)
    
    # keep looping through all current player's possible scores
    while current_score < goal:
        opponent_score = 0

        # keep looping through all opponent player's possible scores
        while opponent_score < goal:
            
            # number on the dice changes
            if strategy(current_score, opponent_score) != beginning:
                return False
            
            # incrememnt for next combination of scores
            opponent_score += 1
        current_score = current_score + 1
        
    # number on the dice never changes
    return True

    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8        
    "*** YOUR CODE HERE ***"

    def average_value(*arg):
        # initialize variables
        total = 0
        count = 0

        # keep looping to add results into total
        while count < times_called:
            total = total + original_function(*arg)
            count = count + 1

        # return average value
        return total / times_called
    return average_value
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    # initialize variables
    best_dice_roll = 1
    current_dice_roll = 1
    max_average_score = 0
    max_average_roll = make_averaged(roll_dice, times_called)

    # keep looping for all number of dice to roll
    while current_dice_roll <= 10:
        current_average_score = max_average_roll(current_dice_roll, dice)

        # check and update if current average score is higher than current max
        if current_average_score > max_average_score:
            max_average_score = current_average_score
            best_dice_roll = current_dice_roll

        # check and update if current average score is equal to current max
        # choose smaller number of dice
        elif current_average_score == max_average_score:
            best_dice_roll = min(best_dice_roll, current_dice_roll)

        current_dice_roll = current_dice_roll + 1
    
    # return highest average score
    return best_dice_roll
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    # check if boar brawl rule causes points to be greater than or equal to threshold
    # if so, no dice rolled
    if boar_brawl(score, opponent_score) >= threshold:
        return 0

    # dice is rolled the set number of times
    else:
        return num_rolls
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11

    # dice (4th argument) already defined in original function
    # use sus fuss and see if it is greater than or equal to threshold
    # if so, no dice rolled
    if (sus_update(0, score, opponent_score) - score) >= threshold:
        return 0
    
    # dice is rolled the set number of times
    else:
        return num_rolls
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()