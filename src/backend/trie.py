# ----------------------------------------------------------------------
# trie.py
# ----------------------------------------------------------------------


class TrieNode:
    """Represents a Node in a Trie with Node children
    and whether or not Node marks the end of a word"""

    def __init__(self):
        self.children = {}  # Node children
        self.is_word = False


# ----------------------------------------------------------------------


class Trie:
    """Represents Trie data structure for dictionary of words"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Adds word into Trie word dictionary

        Parameters:
        word (str) - word to be added to Trie
        """

        word = word.lower()
        current_node = self.root

        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]

        current_node.is_word = True

    def search(self, word: str) -> bool:
        """
        Determines whether or not word is in Trie word dictionary

        Parameters:
        word (str): word to be checked in Trie

        Returns:
        bool: True if word is found in Trie, False otherwise
        """

        word = word.lower()
        current_node = self.root

        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return current_node.is_word

    def starts_with(self, prefix: str) -> bool:
        """
        Determines whether or not words beginning
        with prefix exist in Trie word dictionary

        Parameters:
        prefix (str): prefix to be checked in Trie

        Returns:
        bool: True if words in Trie begin with prefix, False otherwise
        """

        prefix = prefix.lower()
        current_node = self.root

        for letter in prefix:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return True


# ----------------------------------------------------------------------


def main():
    test = Trie()
    test.insert("apple")
    print(test.search("app"))
    print(test.starts_with("app"))


# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()
