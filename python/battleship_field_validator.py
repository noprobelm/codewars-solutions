import codewars_test as test
"""
PROBLEM
------
Original problem: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has 
a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in 
the array are numbers, 0 if the cell is free and 1 if occupied by ship. 

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid 
containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. 
The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this 
kata we will use Soviet/Russian version of the game. 

Before the game begins, players set up the board and place the ships accordingly to the following rules:

    There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (
    size 1). Any additional ships are not allowed, as well as missing ships. Each ship must be a straight line, 
    except for submarines, which are just single cell. The ship cannot overlap or be in contact with any other ship, 
    neither by edge nor by corner. 
    
SOLUTION
------ 
This problem presents a traditional 'battleship' game board as a 10x10 list of lists. Ideally the game board would be 
represented as a class with a fully-fleshed coordinate system to allow for more optimized search algorithms (i.e. 
special methods to handle custom iteration over the game board positions, methods to translate x and y positions into
positions on the board, etc.), but that's outside the question criteria, so we'll do it using handy Python built-ins
 
The solution I've laid out follows the logic:
- Create a nested for loop, accessing each element among our list of lists (i.e. each game board 'position')
- For each position:
    1. Check if the position equals '1'
        - If yes, try/except a ValueError for the 'crawl' function. If a ValueError is encountered, we've identified an
            invalid game board. Return 'False'
        - If no, carry on to next position index
    2. Initiate the 'crawl' function, which accepts a game board position in the format of [xpos, ypos]
        2a. Create the 'positions' variable, which will ultimately store each position for the ship being looked at
        2b. Check to ensure the current position in question is valid. The 'valid_pos' function is only checking to
            ensure there are no corner tiles with a value of '1' among the next row in sequence.
            - If valid, return 'True' and proceed to step 2c.
            - If invalid, the problem has been solved. Raise 'ValueError'.
        2c. Call 'get_nextpos' to get the next position in question. Since we're working left to right, top to bottom,
            and we've validated there are no invalid adjacent tiles, we can simply find whether the next '1' value is
            to the right along the 'x' axis, or below along with 'y' access.
            - Locate the next '1' along the x or y axis and return it. If only '0' is found, we've reached the end
            coordinate of the ship being looked at. Return 'None'.
        2d. Check the condition
            - 'get_nextpos' returned None: Attempt to add the ship coordinates to 'ships_accounted'. If a 'KeyError' is
            encountered, we're working with an invalid ship size. Raise 'ValueError'. The problem is solved.
            - 'get_nextpos' returned a new coordinate: Perform step '2c'
    3. All positions have been logged, all ships are of valid sizes, and they are all in valid positions. Now check
        to ensure we've logged the number of ships we expected to.
            - If 'ships_expected == ships_accounted', return True. The problem has been solved.
            - Else, return False. The problem has been solved.
    """

ship_sizes = {4: 'battleship', 3: 'cruiser', 2: 'destroyer', 1: 'submarine'}
ships_expected = {'battleship': 1, 'cruiser': 2, 'destroyer': 3, 'submarine': 4}
ships_accounted = {'battleship': 0, 'cruiser': 0, 'destroyer': 0, 'submarine': 0}


def validate_battlefield(field):
    def log(positions):
        try:
            ships_accounted[ship_sizes[len(positions)]] += 1
        except KeyError:
            raise ValueError(f"Ship length {len(positions)} does not match any known ship type.")
        for position in positions:
            field[position[1]][position[0]] = ship_sizes[len(positions)]

    def lookup(pos):
        return field[pos[1]][pos[0]]

    def valid_pos(pos):
        try:
            if lookup([pos[0] + 1, pos[1] + 1]) == 1:
                return False
            elif lookup([pos[0] - 1, pos[1] + 1]) == 1 and pos[0] > 0:
                return False
        except IndexError:
            pass
        return True

    def get_nextpos(pos):
        try:
            if lookup([pos[0] + 1, pos[1]]) == 1:
                return [pos[0] + 1, pos[1]]
        except IndexError:
            pass
        try:
            if lookup([pos[0], pos[1] + 1]) == 1:
                return [pos[0], pos[1] + 1]
        except IndexError:
            pass
        else:
            return None

    def crawl(pos):
        positions = [pos]
        while pos:
            if not valid_pos(pos):
                raise ValueError(f"Position {pos} surrounded by invalid adjacents")
            pos = get_nextpos(pos)
            if pos is not None:
                positions.append(pos)
        log(positions)

    for ypos in range(len(field)):
        for xpos in range(len(field[ypos])):
            pos = [xpos, ypos]
            if lookup(pos) == 1:
                try:
                    crawl(pos)
                except ValueError as e:
                    print(e)
                    return False

    if ships_accounted == ships_expected:
        return True
    else:
        return False


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

test.assert_equals(validate_battlefield(battleField), True, "Yep! Seems alright", "Nope, something is wrong!");