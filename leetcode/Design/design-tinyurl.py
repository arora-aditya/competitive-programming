import random

class Codec:
    """
    https://leetcode.com/problems/design-tinyurl/
    """
    STRING = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    map = {}

    def encode(self, longUrl):
        tag = self.gen_tag()
        self.map[tag] = longUrl
        return "http://tinyurl.com/" + tag

    def gen_tag(self):
        tag = self.gen_random_str()
        while tag in self.map.keys():
            tag = self.gen_random_str()
        return tag

    def gen_random_str(self):
        result = ""
        for i in range(6):
            result += self.STRING[random.randint(0,61)]
        return result

    def decode(self, shortUrl):
        return self.map[shortUrl[-6:]]

codec = Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tingdrtdyurl")))
