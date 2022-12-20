import codewars_test as test
import numpy as np


class Blobservation:
    def __init__(self, matrix):
        self.matrix = matrix

    def move(self, instructions):
        def transpose(matrix):
            return [list(idx) for idx in zip(*matrix)]

        def filter_nonzeros(matrix):
            return [list(filter(lambda x: x!=0, m)) for m in matrix]

        def fill_zeros(matrix):
            max_array = max([len(m) for m in matrix])
            for m in matrix:
                while len(m) < max_array:
                    m.append(0)
            return matrix

        new = [list(m) for m in self.matrix]
        if instructions == "N" or instructions == "S":
            new = transpose(new)
        new = filter_nonzeros(new)
        if instructions == "S" or instructions == "E":
            new = [n[::-1] for n in new]

        for m in new:
            idx = 0
            while idx < len(m) - 1:
                if m[idx] > m[idx + 1]:
                    m[idx] += m.pop(idx+1)
                idx += 1

        new = fill_zeros(new)
        if instructions == "S" or instructions == "E":
            new = [n[::-1] for n in new]
        if instructions == "N" or instructions == "S":
            new = [list(idx) for idx in zip(*new)]

        self.matrix = tuple(tuple(m) for m in new)

    def read(self, instructions):
        self.move(instructions)

    def state(self):
        state = [list(m) for m in self.matrix]
        while len([n for n in state[0] if n == 0]) == len(state[0]):
            del state[0]
        while len([n for n in state[-1] if n == 0]) == len(state[-1]):
            del state[0]
        state = [list(idx) for idx in zip(*state)]
        while len([n for n in state[0] if n == 0]) == len(state[0]):
            del state[0]
        while len([n for n in state[-1] if n == 0]) == len(state[-1]):
            del state[0]
        state = [tuple(idx) for idx in zip(*state)]
        state = tuple(state)
        return state


@test.describe("Example Tests")
def example_tests():
    @test.describe("Verify correctness of step-by-step instructions")
    def example1():
        grid = (
            (9, 4, 6),
            (8, 8, 8),
            (3, 6, 9)
        )
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