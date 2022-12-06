import codewars_test as test
import math
from typing import Optional, List

"""
PROBLEM
------
Original url: https://www.codewars.com/kata/5abab55b20746bc32e000008/train/python

Blobs of various sizes are situated in a room. Each blob will move toward the nearest smaller blob until it reaches it and engulfs it. After consumption, the larger blob grows in size.

Your task is to create a class Blobservation (a portmanteau of blob and observation) and methods that give information about each blob after an arbitrary number of moves.
Class Details

A Blobservation class instance is instantiated with two integer values, h and w, that represent the dimensions of the room. The instance methods are as follows:
populate

The populate method is called with an array/list representing a list of blobs.

    Each element is an object/dict (Map<String,Integer> in Java) with the following properties:
        x: vertical position
        y: horizontal position
        size: size of the blob
    This method may be called multiple times on the same class instance
    If a new blob's position is already occupied by an existing blob, the two fuse into a single blob
    If the list input contains any invalid values, discard it entirely and throw an error (do not update/modify the instance)

move

The move method may be called with up to one argument — a positive integer representing the number of move iterations (ie. turns) to process. If no argument is given, the integer value defaults to 1.
print_state

The print_state method is a nullary function that returns an array of the positions and sizes of each blob at the current state (Java: a List<List<Integer>> ), sorted in ascending order by x position, then by y. If there are no blobs, return an empty array.
Blob Movement Behavior

With each turn, every blob whose size is larger than the smallest blob size value will move to one of the 8 spaces immediately surrounding it (Moore neighborhood) in the direction of the nearest target blob with a lower relative size.

    If a target's coordinates differ on both axes, the predatory blob will move diagonally. Otherwise, it will move in the cardinal direction of its target
    If multiple targets are at the same movement distance, the blob with the largest size is focused
    If there are multiple targets that have both the largest size and shortest movement distance, priority is set in clockwise rotation, starting from the 12 position
    If two blobs pass each other (e.g. swap positions as a result of their movement), they will not fuse
    Blobs of the smallest size remain stationary

Additional Technical Details

    A blob's initial size will range between 1 and 20
    Multiple blobs occupying the same space will automatically fuse into one
    When a blob consumes another blob, or when two blobs fuse, the remaining blob's size becomes the sum of the two
    The 2nd argument for the class constructor is optional; if omitted, the room defaults to a square, where w == h.
    Room dimensions (h and w) will range between 8 and 50
    Class instances will always be instantiated with valid arguments
    Methods should throw an error if called with invalid arguments
    Boolean values are not to be regarded as valid integers
    Python translation: Use Python 3 only

Test Example

The image above shows the state at turn 0 (the initial state), turn 1, and turn 2.

    At T:0, the orange blob at [4,3] with a size of 4 has four different targets of equal movement distance — the blobs occupying the green, yellow, and red spaces. The adjacent matching-color spaces are the positions it would initially move to in pursuit of each respective target. Here it targets the size 3 blob at [7,0].
    At T:1, the size 2 blob that was in the yellow space has consumed the size 1 blob at [6,7] and now has a size of 3
    At T:2, the size 3 blob in the green space has consumed the size 1 blob to become the size 4 blob at [7,2]. At this point, the two orange blobs will both target the green blob at [4,2] and all size 2 blobs will remain stationary

generation0 = [
    {'x':0,'y':4,'size':3},
    {'x':0,'y':7,'size':5},
    {'x':2,'y':0,'size':2},
    {'x':3,'y':7,'size':2},
    {'x':4,'y':3,'size':4},
    {'x':5,'y':6,'size':2},
    {'x':6,'y':7,'size':1},
    {'x':7,'y':0,'size':3},
    {'x':7,'y':2,'size':1}
]
blobs = Blobservation(8)
blobs.populate(generation0)
blobs.move()
blobs.print_state() #[[0,6,5],[1,5,3],[3,1,2],[4,7,2],[5,2,4],[6,7,3],[7,1,3],[7,2,1]]
blobs.move()
blobs.print_state() #[[1,5,5],[2,6,3],[4,2,2],[5,6,2],[5,7,3],[6,1,4],[7,2,4]]
blobs.move(1000)
blobs.print_state() #[[4,3,23]]

If you enjoyed this kata, be sure to check out my other katas
"""


class Blobservation:
    """
    Simulation of a grid-like object which can be populated with "blobs". "Blobs" are represented as dictionaries with
    'x', 'y' positions, and a 'size'. Blobs are popoulated by passing a list of valid blob dictionaries to the
    'populate' method. A blobservation is iterated by calling the 'move()' method. Each iteration will result in all
    valid "predator" blobs moving according to a predefined conditional ruleset, then merged with other blobs who share
    the same space in the blobservation coordinate plane.

    Parameters:
        h (int): The height of the Blobservation (corresponds with 'x' for blobs)
        w (int): The width of the Blobservation (corresponds with 'y' for blobs)
        blobs (List[dict]): A list of dictionary representations of each blob.

    Methods:
        - populate: Populate a blobservation plane
        - merge: Merge one blob with another, deleting the second blob from memory.
         - _get_targets: Gets a list of tuple pairs of a predator blob and its prey's x and y position.
        - move: Iterate the blobservation by 'num_moves'
        - print_state: Return the state of the blobservation as a list of lists for the 'x', 'y', and 'size' of a blob.
        Blobservation states are sorted by 'x', then 'y', then 'size'.
    """

    def __init__(self, h: int, w: Optional[int] = None) -> None:
        self.h = h
        if w:
            self.w = w
        else:
            self.w = h
        self.blobs = []

    def populate(self, population: List[dict]) -> None:
        """
        Populate a blobservation plane

        Behavior:
            - 'populate' can be called an arbitrary number of times
            - 'populate' can be called at any point during a blobservation
            - Upon populating, new blobs whose position are equal to an existing blob will be merged and dropped.
            - A newly populated blob's size will be no larger than '20'.
            - 'x' coordinates are vertical, 'y' are horizontal.

        Parameters:
            population (List[dict]): A list of dictionaries containing information about a blob. A 'blob' dictionary
            must contain values for 'x' (vertical position), 'y' (horizontal position) and 'size'.

            'x': Integer whose value falls within range <= 'x' < 'self.h'.
            'y': Integer whose value falls within range 0 <= 'y' < 'self.w'
            'size': Integer whose value falls within range 0 <= 'size' <= 20

        Raises:
            TypeError: An invalid type has been passed for a blob's dict representation
            ValueError: A value outside the allowed bounds for a blob's 'x', 'y', or 'size' has been passed.

        """
        for blob in population:
            for attribute in blob:
                if type(blob[attribute]) != int:
                    raise TypeError(f"Expected type 'int' for {attribute}, got {type(blob[attribute])}")
            if not 0 <= blob['x'] < self.h:
                raise ValueError(f"Value 'x' == {blob['x']} out of bounds. 'x' must be within range 0 < x < {self.h}")
            if not 0 <= blob['y'] < self.w:
                raise ValueError(f"Value 'y' == {blob['y']} out of bounds. 'y' must be within range 0 < y < {self.w}")
            if not 0 <= blob['size'] <= 20:
                raise ValueError(f"Value 'size' out of bounds. '{blob['size']}' must be within range 0 < size < 20")
        if not self.blobs:
            self.blobs.append(population.pop(0))
        for new in population:
            is_new = True
            for blob in self.blobs:
                if [blob['x'], blob['y']] == [new['x'], new['y']]:
                    is_new = False
                    self.merge(blob, new)
                    break
            if is_new is True:
                self.blobs.append(new)

    def merge(self, first: dict, second: dict) -> None:
        """
        Merge one blob with another, deleting the second blob from memory

        Parameters:
            first (dict): Dict of the blob to be retained in memory
            second (dict): Dict of the blob to be merged with 'first'. Will be removed from memory.
        """
        self.blobs[self.blobs.index(first)]['size'] += second['size']
        try:
            del self.blobs[self.blobs.index(second)]
        except ValueError:
            pass

    def _get_targets(self):
        """
        Get a list of tuple pairs of a predator blob and its prey's x and y position.

        Target prioritization ruleset:
            - Identify all blobs whose sizes are smaller than the predator blob's size. These are the candidate "prey".
            If no blob is smaller than the predator, do nothing.
            - If there are multiple prey who meet these criteria, find the prey of the shortest move distance.
            - If there are multiple prey of equal move distances, find the largest.
            - If there are multiple prey whose size are equal to the largest, find the prey whose clockwise position
            is encountered first (starting from 12:00).

        The result of this ruleset logic will invariably produce a single prey. The predator and its prey's x and y
        position are then paired as a tuple and appended to a list of other similar tuple pairs.

        Returns:
            move_targets (List[tuple]): List of tuple pairs whose first value is the "predator" blob, the second its
            prey's x and y coordinates
        """
        predators = [blob.copy() for blob in self.blobs]
        move_targets = []
        for predator in predators:
            preys = [candidate.copy() for candidate in self.blobs if candidate['size'] < predator['size']]
            if not preys:
                continue
            for prey in preys:
                leg_a = abs(predator['x'] - prey['x'])
                leg_b = abs(predator['y'] - prey['y'])
                move_distance = max([leg_a, leg_b])
                prey['move_distance'] = move_distance
            min_moves = min([candidate['move_distance'] for candidate in preys])
            preys = list(filter(lambda candidate: candidate['move_distance'] == min_moves, preys))
            if len(preys) > 1:
                largest = max([candidate['size'] for candidate in preys])
                preys = list(filter(lambda candidate: candidate['size'] == largest, preys))
            if len(preys) > 1:
                for prey in preys:
                    prey['angle'] = math.atan2(prey['y'] - predator['y'], prey['x'] - predator['x'])
                max_angle = max([candidate['angle'] for candidate in preys])
                preys = list(filter(lambda candidate: candidate['angle'] == max_angle, preys))
            prey = preys[0]
            move_targets.append((predator, {'x': prey['x'], 'y': prey['y']}))
        return move_targets

    def move(self, num_moves: Optional[int] = 1):
        """
        Iterate the blobservation by 'num_moves'.

        Works by calling 'get_targets', then iterating through each target and updating its predator blob's x and y
        position in the blobservation's coordinate plane according to its prey's relative location.

        After all blobs have moved, check for blobs in identical positions and merge. Delete one of the blobs from
        memory.

        Args:
            num_moves (int): Positive integer representing the number of moves to iterate the blobservation by.
        """

        def get_position(predator: dict, prey: dict):
            old = {'x': predator['x'], 'y': predator['y']}
            new = {}
            if predator['x'] < prey['x']:
                new['x'] = old['x'] + 1
            elif predator['x'] > prey['x']:
                new['x'] = old['x'] - 1
            if predator['y'] < prey['y']:
                new['y'] = old['y'] + 1
            elif predator['y'] > prey['y']:
                new['y'] = old['y'] - 1
            return new

        if num_moves < 1:
            raise ValueError(f"Invalid 'num_moves': {num_moves}.")
        elif type(num_moves) != int:
            raise TypeError(f"Got {type(num_moves)} for 'num_moves', expected type 'int'")

        for move in range(num_moves):
            move_targets = self._get_targets()
            for pair in move_targets:
                new_position = get_position(pair[0], pair[1])
                self.blobs[self.blobs.index(pair[0])].update(new_position)

            for blob in self.blobs:
                for other in self.blobs:
                    if blob is other:
                        continue
                    elif [blob['x'], blob['y']] == [other['x'], other['y']]:
                        self.merge(blob, other)

    def print_state(self) -> List[List]:
        """
        Print the state of the blobservation as a list of lists for the 'x', 'y', and 'size' of a blob. Blobservation
        states are sorted by 'x', then 'y', then 'size'.

        If no blobs are found in the blobservation, return an empty list.
        """
        if self.blobs:
            state = sorted(self.blobs, key=lambda b: (b['x'], b['y']))
            return [[blob['x'], blob['y'], blob['size']] for blob in state]
        else:
            return self.blobs


test.describe('Example Tests')
pf = lambda x, r: test.assert_equals(x.print_state(), r)

generation0 = [
    {'x': 0, 'y': 4, 'size': 3},
    {'x': 0, 'y': 7, 'size': 5},
    {'x': 2, 'y': 0, 'size': 2},
    {'x': 3, 'y': 7, 'size': 2},
    {'x': 4, 'y': 3, 'size': 4},
    {'x': 5, 'y': 6, 'size': 2},
    {'x': 6, 'y': 7, 'size': 1},
    {'x': 7, 'y': 0, 'size': 3},
    {'x': 7, 'y': 2, 'size': 1},
]
blobs = Blobservation(8)
blobs.populate(generation0)
blobs.move()
pf(blobs, [[0, 6, 5], [1, 5, 3], [3, 1, 2], [4, 7, 2], [5, 2, 4], [6, 7, 3], [7, 1, 3], [7, 2, 1]])
blobs.move()
pf(blobs, [[1, 5, 5], [2, 6, 3], [4, 2, 2], [5, 6, 2], [5, 7, 3], [6, 1, 4], [7, 2, 4]])
blobs.move(1000)
pf(blobs, [[4, 3, 23]])

generation1 = [
    {'x': 3, 'y': 6, 'size': 3},
    {'x': 8, 'y': 0, 'size': 2},
    {'x': 5, 'y': 3, 'size': 6},
    {'x': 1, 'y': 1, 'size': 1},
    {'x': 2, 'y': 6, 'size': 2},
    {'x': 1, 'y': 5, 'size': 4},
    {'x': 7, 'y': 7, 'size': 1},
    {'x': 9, 'y': 6, 'size': 3},
    {'x': 8, 'y': 3, 'size': 4},
    {'x': 5, 'y': 6, 'size': 3},
    {'x': 0, 'y': 6, 'size': 1},
    {'x': 3, 'y': 2, 'size': 5},
]
generation2 = [
    {'x': 5, 'y': 4, 'size': 3},
    {'x': 8, 'y': 6, 'size': 15},
    {'x': 1, 'y': 4, 'size': 4},
    {'x': 2, 'y': 7, 'size': 9},
    {'x': 9, 'y': 0, 'size': 10},
    {'x': 3, 'y': 5, 'size': 4},
    {'x': 7, 'y': 2, 'size': 6},
    {'x': 3, 'y': 3, 'size': 2},
]
blobs = Blobservation(10, 8)
blobs.populate(generation1)
blobs.move()
pf(
    blobs,
    [
        [0, 6, 1],
        [1, 1, 1],
        [1, 6, 2],
        [2, 1, 5],
        [2, 6, 7],
        [4, 2, 6],
        [6, 7, 3],
        [7, 1, 2],
        [7, 4, 4],
        [7, 7, 1],
        [8, 7, 3],
    ],
)
blobs.move(2)
pf(blobs, [[0, 6, 7], [1, 5, 3], [2, 2, 6], [4, 1, 6], [6, 1, 2], [6, 4, 4], [6, 6, 7]])
blobs.move(2)
pf(blobs, [[2, 4, 13], [3, 3, 3], [6, 1, 8], [6, 2, 4], [6, 4, 7]])
blobs.populate(generation2)
pf(
    blobs,
    [
        [1, 4, 4],
        [2, 4, 13],
        [2, 7, 9],
        [3, 3, 5],
        [3, 5, 4],
        [5, 4, 3],
        [6, 1, 8],
        [6, 2, 4],
        [6, 4, 7],
        [7, 2, 6],
        [8, 6, 15],
        [9, 0, 10],
    ],
)
blobs.move()
pf(
    blobs,
    [[2, 4, 9], [3, 3, 13], [3, 6, 9], [4, 4, 4], [5, 3, 4], [5, 4, 10], [6, 2, 6], [7, 2, 8], [7, 5, 15], [8, 1, 10]],
)
blobs.move(3)
pf(blobs, [[4, 3, 22], [5, 3, 28], [5, 4, 9], [6, 2, 29]])
test.expect_error('Invalid input for the move method should trigger an error', lambda: blobs.move(-3))
blobs.move(30)
pf(blobs, [[5, 3, 88]])
test.expect_error(
    'Invalid elements should trigger an error',
    lambda: blobs.populate([{'x': 4, 'y': 6, 'size': 3}, {'x': '3', 'y': 2, 'size': True}]),
)

generation_3 = [
    {'x': 0, 'y': 3, 'size': 7},
    {'x': 1, 'y': 6, 'size': 1},
    {'x': 1, 'y': 18, 'size': 3},
    {'x': 2, 'y': 11, 'size': 3},
    {'x': 3, 'y': 3, 'size': 3},
    {'x': 4, 'y': 12, 'size': 1},
    {'x': 4, 'y': 14, 'size': 1},
    {'x': 5, 'y': 0, 'size': 6},
    {'x': 5, 'y': 7, 'size': 5},
    {'x': 5, 'y': 18, 'size': 8},
    {'x': 6, 'y': 13, 'size': 3},
    {'x': 8, 'y': 4, 'size': 4},
    {'x': 8, 'y': 7, 'size': 6},
    {'x': 8, 'y': 10, 'size': 2},
    {'x': 8, 'y': 13, 'size': 7},
    {'x': 8, 'y': 6, 'size': 5},
    {'x': 10, 'y': 2, 'size': 3},
    {'x': 10, 'y': 7, 'size': 5},
    {'x': 11, 'y': 11, 'size': 2},
    {'x': 12, 'y': 6, 'size': 1},
    {'x': 12, 'y': 14, 'size': 2},
    {'x': 13, 'y': 1, 'size': 2},
    {'x': 14, 'y': 9, 'size': 5},
    {'x': 16, 'y': 0, 'size': 1},
    {'x': 16, 'y': 11, 'size': 3},
    {'x': 16, 'y': 16, 'size': 3},
    {'x': 17, 'y': 6, 'size': 1},
    {'x': 18, 'y': 10, 'size': 5},
    {'x': 18, 'y': 13, 'size': 7},
    {'x': 18, 'y': 18, 'size': 5},
    {'x': 19, 'y': 2, 'size': 6},
    {'x': 19, 'y': 16, 'size': 8},
]
blobs = Blobservation(20)
blobs.populate(generation_3)
blobs.move(6)
blobs.move(5)
pf(
    blobs,
    [
        [6, 11, 24],
        [7, 10, 8],
        [8, 10, 6],
        [9, 10, 7],
        [15, 5, 19],
        [15, 10, 8],
        [16, 6, 19],
        [16, 8, 11],
        [16, 9, 10],
        [16, 10, 12],
    ],
)
print('<COMPLETEDIN::>')
