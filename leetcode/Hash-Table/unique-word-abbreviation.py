class ValidWordAbbr(object):
    """
    https://leetcode.com/problems/unique-word-abbreviation/description/
    """
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.se = set()
        self.di = {}
        for i in dictionary:
            if i not in self.se:
                self.se.update([i])
            else:
                continue
            # print(self.se)
            if len(i) <= 2:
                key = i
            elif len(i) == 3:
                key = i[0] + "1" + i[-1]
            else:
                key = i[0] + str(len(i)-2)+i[-1]
            self.di[key] = self.di.get(key, 0) + 1
            # print(self.di)
        # print(self.di)

    def isUnique(self, i):
        """
        :type word: str
        :rtype: bool
        """
        if len(i) <= 2:
            key = i
        elif len(i) == 3:
            key = i[0] + "1" + i[-1]
        else:
            key = i[0] + str(len(i)-2)+i[-1]
        # print(key)
        if i not in self.se:
            # print(key, "not in set")
            if key in self.di:
                # print(key, "in dict")
                return False
            # print(key, "not in dict")
            return True
        try:
            # print(key, "found")
            # print(self.di)
            return self.di[key] == 1
        except KeyError:
            # print(key, "not found")
            return True



# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
