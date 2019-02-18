class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True
    def failedAttempt1(self, words: List[str], order: str) -> bool:
        char_score = {}
        for i in range(len(order)):
            char_score[order[i]] = i
        char_score[' '] = -1
        j = 0

        max_le = 0
        for word in words:
            max_le = max(max_le, len(word))
        chars = [""]*max_le
        flag = True
        for j in range(max_le):
            for i in words:
                if j >= len(i):
                    chars[j] += ' '
                else:
                    chars[j] += i[j]
            chars[j] += order[0]
        print(chars)
        for char in chars:
            print(char)
            for i in range(len(words)):
                if char[0] == 'u':
                    print(char_score[char[i]], char_score[char[i-1]])
                if char_score[char[i]] < char_score[char[i-1]]:
                    return False
        return True
        
    def failedAttempt2(self, words: List[str], order: str) -> bool:
        i = 0
        su = [0]*len(words) + [-1]
        # mi =
        flag = False
        while True and not flag:
            # print(su)
            flag = True
            mi = -1
            for j in range(len(words)):
                try:
                    print(words[j][i])
                    su[j] = su[j] + char_score[words[j][i]]
                    if su[j] < su[j-1]:
                        return False
                    flag = False
                    last = True
                except:
                    print(su)
                    if not last and j != len(words) - 1 and su[j] < su[j-1]:
                        return False
                    last = False
            i += 1
        return True






# ["apple","app"]
# "abcdefghijklmnopqrstuvwxyz"
# ["word","world","row"]
# "worldabcefghijkmnpqstuvxyz"
# ["hello","leetcode"]
# "hlabcdefgijkmnopqrstuvwxyz"
# ["kuvp","q"]
# "ngxlkthsjuoqcpavbfdermiywz"
