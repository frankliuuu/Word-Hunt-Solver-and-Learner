# ----------------------------------------------------------------------
# wordhunt.py
# ----------------------------------------------------------------------

import json
from src.backend import trie

# ----------------------------------------------------------------------


class Wordhunt:
    """Represents Word Hunt Solver"""

    trie_dictionary = None
    definitions = {}

    def __init__(self):
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        self.result = {}
        self.visited = []

        if Wordhunt.trie_dictionary is None:
            Wordhunt.trie_dictionary = self.make_trie()
        if not Wordhunt.definitions:
            Wordhunt.definitions = self.load_definitions()

    def make_board(self, board: str):
        """
        Replicates Word Hunt board with input board

        Parameters:
        board (str): Word Hunt board of letters
        """

        letters = board.lower()
        for i in range(4):
            for j in range(4):
                self.board[i][j] = letters[4 * i + j]

    def make_trie(self):
        """
        Makes Trie word dictionary from JSON file
        """

        with open("./src/backend/dictionary.json", "r", encoding="utf-8") as file:
            words_dict = json.load(file)
            t = trie.Trie()
            for word in words_dict.keys():
                t.insert(word)
            return t

    def load_definitions(self):
        """
        Load definitions from JSON file
        """
        with open("./src/backend/dictionary.json", "r", encoding="utf-8") as file:
            word_definitions = json.load(file)
        return word_definitions

    def solve(self):
        """
        Looks for all words in Word Hunt board
        """

        for i in range(4):
            for j in range(4):
                self.solve_dfs(i, j, "")

    def solve_dfs(self, i: int, j: int, curr: str):
        """
        Looks for all possible words at positions i and j on board
        recursively using depth first search

        Parameters:
        i (int): row on board
        j (int): column on board
        curr (str): word constructed at each recursive step
        """

        if (
            i not in range(4)
            or j not in range(4)
            or not Wordhunt.trie_dictionary.starts_with(curr)
            or self.board[i][j] == 0
        ):
            return

        curr_letter = self.board[i][j]
        new = curr + curr_letter
        self.board[i][j] = 0
        self.visited.append((i, j))

        if len(new) >= 3 and Wordhunt.trie_dictionary.search(new):
            definition = Wordhunt.definitions.get(new, "Definition not found")
            positions = [4 * pos[0] + pos[1] for pos in self.visited]
            self.result.setdefault(len(new), {})[new] = {
                "positions": positions,
                "definition": definition,
            }

        directions = (
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [-1, -1],
            [-1, 1],
            [1, 1],
            [1, -1],
        )

        for di, dj in directions:
            self.solve_dfs(i + di, j + dj, new)

        self.board[i][j] = curr_letter
        self.visited.pop()

    def results(self):
        """
        Prints all found words, their paths, and paths from board

        """

        for i in range(15, -1, -1):
            if i in self.result and len(self.result[i]) > 0 and i >= 3:
                for word, info in self.result[i].items():
                    positions = ",".join(map(str, info["positions"]))
                    print(f"{word}: {positions} (Definition: {info['definition']})")


# ----------------------------------------------------------------------


def main():
    solver = Wordhunt()
    board = "applabcedeffffff"
    solver.make_board(board)
    solver.solve()
    solver.results()


# ----------------------------------------------------------------------

if __name__ == "__main__":
    main()
