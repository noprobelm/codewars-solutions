import codewars_test as test
from typing import Tuple, List
import re


class Blobservation:
    """
    A 'Blobservation' is an 'm' x 'n' style matrix where each index is either empty (0) or occupied by a blob (int
    representing its size).

    Parameters:
        matrix (Tuple[Tuple, ...], ...): The matrix representative of each blob's position and size. The 'm' and 'n'
        axis of the matrix are always of equal dimensions.

    Methods:
        - read: Reads a cardinal direction ('N', 'E', 'S', or 'W') or series of cardinal directions as a string. This
        method hooks to the 'move' method, which executes the logic behind the moves.
        - state: Returns the current 'state' of the matrix. The returned 'state' is represented as a matrix sized to be
        as small as possible without excluding any blob positions.
        - move: Executes a single move based on a passed cardinal direction.
        - _transpose: Static method for internal use. Transposes the matrix. Utilized by the 'move' and 'state' methods.
        - _remove_zeros: Static method for internal use. Removes zeros from each row of a passed matrix.
        Utilized by the 'move' method
        - _fill_zeros: Static method for internal use. Adds zeros as necessary to make all rows of a matrix the same
        length.
    """
    def __init__(self, matrix: Tuple[Tuple[int, ...], ...]) -> None:
        self.matrix = matrix

    @staticmethod
    def _transpose(matrix: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
        """Static method for internal use. Transposes the matrix. Utilized by the 'move' and 'state' methods."""
        return tuple(tuple(idx) for idx in zip(*matrix))

    @staticmethod
    def _remove_zeros(matrix: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
        """
        Static method for internal use. Removes zeros from each row of a passed matrix.Utilized by the 'move' method
        """
        matrix = [list(filter(lambda x: x != 0, m)) for m in matrix]
        return tuple(tuple(m) for m in matrix)

    @staticmethod
    def _fill_zeros(matrix: List[List[int]]) -> Tuple[Tuple[int, ...], ...]:
        """
        Static method for internal use. Adds zeros as necessary to make all rows of a matrix the same length.
        """
        max_array = max([len(m) for m in matrix])
        for m in matrix:
            while len(m) < max_array:
                m.append(0)
        return tuple([tuple(n) for n in matrix])

    def move(self, instruction: str) -> None:
        """Executes a single move based on a passed cardinal direction.

        The 'move' method executes 3 main steps:
            1. Transform the matrix as needed to make our 'move' operation common between any cardinal direction
                a. If an instruction is 'N' or 'S', transpose our matrix to swap 'm' with 'n'
                b. If an instruction is 'S' or 'E', reverse 'm' so we can traverse each row in a common manner when
                executing the move.
                c. Remove all zeros from each 'm' so we're left with only valid blobs.
            2. Execute the 'move' steps
                a. All blob merges are concurrent. Therefore, we can't execute any merges until we're aware of whether
                one blob will be absorbing another. To solve this, we initiate an empty list 'absorb', which stores
                the value (in order) of each 'chain' of blobs to be absorbed.
                b. After we have a list of all blobs to be absorbed, overwrite 'm' to be a list of the sum of each value
                from our 'absorb' list.
                c. Overwrite the current index of 'new' with the new 'm'.
            3. Revert the original transformations, thereby restoring the matrix to its original format.
                a. Read each bool flag (is_transposed, is_reversed) to check if a transformation operation needs to
                occur. Execute transformations as necessary.
                b. Finally, update self.matrix with the newly calculated matrix.

        Args:
            instruction: str representation of the cardinal direction where we need to move ('N', 'E', 'S', 'W')

        Parameters:
            - new (Tuple[Tuple, ...], ...): A copy of class attribute 'matrix'. 'new' is the variable we work with to
            perform the necessary transformations in order to execute a move.
            - is_transposed (bool): Boolean indicating whether the matrix is transposed
            - is_reversed (bool): Boolean indicating whether each row in the matrix is reversed.
        """
        new = self.matrix
        is_transposed = False
        is_reversed = False

        if re.search('N|S', instruction):
            new = self._transpose(new)
            is_transposed = True
        if re.search('S|E', instruction):
            new = tuple([m[::-1] for m in new])
            is_reversed = True
        new = self._remove_zeros(new)

        new = [list(m) for m in new]
        for idm, m in enumerate(new):
            idn = 0
            absorb = [[m[idn]]]
            while idn < len(m) - 1:
                if m[idn] > m[idn + 1]:
                    absorb[-1].append(m[idn + 1])
                else:
                    absorb.append([m[idn + 1]])
                idn += 1
            m = [sum(a) for a in absorb]
            new[idm] = m

        new = self._fill_zeros(new)
        if is_reversed is True:
            new = tuple([tuple(m[::-1]) for m in new])
        if is_transposed is True:
            new = self._transpose(new)

        self.matrix = tuple(tuple(m) for m in new)

    def read(self, instructions: str) -> None:
        """Executes a single move based on a passed cardinal direction."""
        for instruction in instructions:
            self.move(instruction)

    def state(self) -> Tuple[Tuple[int, ...], ...]:
        """
        Returns the current 'state' of the matrix. The returned 'state' is represented as a matrix sized to be
        as small as possible without excluding any valid blob positions.

        Returns: state (Tuple[Tuple, ...], ...) - The current state of the matrix, represented as small as possible
        without excluding any valid blob positions
        """
        state = self.matrix
        while len([n for n in state[0] if n == 0]) == len(state[0]):
            del state[0]
            state = self._transpose(state)
        while len([n for n in state[-1] if n == 0]) == len(state[-1]):
            del state[0]
            state = self._transpose(state)
        return state

@test.describe("Example Tests")
def example_tests():
    @test.describe("Verify correctness of step-by-step instructions")
    def example1():
        grid = ((9, 4, 6), (8, 8, 8), (3, 6, 9))
        instructions = ("E", "S", "E", "N")
        transition_steps = (
            (
                (0, 9, 10),
                (8, 8, 8),
                (0, 0, 18),
            ),
            (
                (0, 9, 10),
                (8, 8, 26),
            ),
            (
                (0, 19),
                (8, 34),
            ),
            (
                (8, 19),
                (0, 34),
            ),
        )

        blobs = Blobservation(grid)

        for i, move in enumerate(instructions):

            @test.it(f"Reading instruction: \"{move}\"")
            def single_steps():
                blobs.read(move)
                test.assert_equals(blobs.state(), transition_steps[i])

    @test.it("Test a simple case")
    def example2():
        grid = (
            (4, 3, 5),
            (1, 4, 6),
            (5, 2, 6),
        )
        final_state = (
            (7, 0),
            (7, 22),
        )
        blobs = Blobservation(grid)
        blobs.read("WENS")
        test.assert_equals(blobs.state(), final_state)
