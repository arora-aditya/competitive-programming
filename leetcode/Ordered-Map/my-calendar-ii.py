class MyCalendarTwo:
    # https://leetcode.com/problems/my-calendar-ii/
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        count = 0
        commons = []
        for s, e in self.events:
            key = [max(s, start), min(e, end)]
            if key[0] < key[1]:
                commons.append(key)
        if commons:
            commons.sort(key=lambda x: x[0])
            commons2 = [commons[0]]
            for i in range(1, len(commons)):
                event = commons[i]
                if event[0] < commons2[-1][1]:
                    # print(f'False e{[start, end]} c{commons} e{self.events}')
                    return False
                else:
                    commons2.append(event)
        # print(f'True e{[start, end]} c{commons} e{self.events}')
        self.events.append([start, end])
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
