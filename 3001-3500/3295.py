class Trie:
    def __init__(self):
        self.count = 0
        self.list = [None] * 26  # Initialize the list of 26 elements for 'a'-'z'

    def put(self, node, ch):
        self.list[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.list[ord(ch) - ord('a')]

    def setEnd(self):
        self.count += 1

    def isEnd(self):
        return self.count


class Solution:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        node = self.root
        for ch in word:
            if node.get(ch) is None:
                node.put(Trie(), ch)
            node = node.get(ch)
        node.setEnd()

    def search(self, word):
        node = self.root
        for ch in word:
            if node.get(ch) is None:
                return 0
            node = node.get(ch)
        return node.isEnd()

    def reportSpam(self, message, bannedWords):
        # Insert all words in the message into the Trie
        for word in message:
            self.insert(word)

        count = 0
        st = set(bannedWords)

        # Check if banned words exist in the message
        for word in st:
            count += self.search(word)
            if count >= 2:
                return True
        return False


# Example Usage
sol = Solution()
message = ["hello", "world", "spam", "message"]
bannedWords = ["spam", "message", "notfound"]

print(sol.reportSpam(message, bannedWords))  # Output: True
