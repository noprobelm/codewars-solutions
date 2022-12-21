import codewars_test as test
import re


class Blobservation:
    def __init__(self, matrix):
        self.matrix = matrix

    def move(self, instruction):
        def transpose(matrix):
            return [list(idx) for idx in zip(*matrix)]

        def filter_nonzeros(matrix):
            return [list(filter(lambda x: x != 0, m)) for m in matrix]

        def fill_zeros(matrix):
            max_array = max([len(m) for m in matrix])
            for m in matrix:
                while len(m) < max_array:
                    m.append(0)
            return matrix

        def execute():
            new = [list(m) for m in self.matrix]
            is_transposed = False
            is_reversed = False

            if re.search('N|S', instruction):
                new = transpose(new)
                is_transposed = True
            if re.search('S|E', instruction):
                new = [n[::-1] for n in new]
                is_reversed = True
            new = filter_nonzeros(new)

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

            new = fill_zeros(new)
            if is_reversed is True:
                new = [n[::-1] for n in new]
            if is_transposed is True:
                new = [list(idx) for idx in zip(*new)]

            self.matrix = tuple(tuple(m) for m in new)

        execute()

    def read(self, instructions):
        for instruction in instructions:
            self.move(instruction)

    def state(self):
        def shrink(matrix):
            while len([n for n in matrix[0] if n == 0]) == len(matrix[0]):
                del matrix[0]
            while len([n for n in matrix[-1] if n == 0]) == len(matrix[-1]):
                del matrix[0]

            return matrix

        state = shrink(self.matrix)
        state = tuple(tuple(idx) for idx in zip(*state))
        state = shrink(state)
        state = tuple(tuple(idx) for idx in zip(*state))
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
