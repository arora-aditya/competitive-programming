class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        https://leetcode.com/problems/unique-morse-code-words/description/
        :type words: List[str]
        :rtype: int
        """
        def morse(s):
            k = ""
            di = {'a': '.-', 'c': '-.-.', 'b': '-...', 'e': '.', 'd': '-..', 'g': '--.', 'f': '..-.', 'i': '..', 'h': '....', 'k': '-.-', 'j': '.---', 'm': '--', 'l': '.-..', 'o': '---', 'n': '-.', 'q': '--.-', 'p': '.--.', 's': '...', 'r': '.-.', 'u': '..-', 't': '-', 'w': '.--', 'v': '...-', 'y': '-.--', 'x': '-..-', 'z': '--..'}
            for i in s:
                k += di[str(i)]
            return k
        return len(set(map(morse, words)))
