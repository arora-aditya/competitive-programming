class Solution:
    def isValid(self, code: str) -> bool:
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'
        
    def failedAttempt_isValid(self, code: str) -> bool:
        code = re.sub('<!\[CDATA\[.*?\]\]>', '', code)
        current_tag = ''
        tag_stack = []
        tag_seen = False
        alphs = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ/'))
        if not code:
            return False
        # print(code)
        for i in range(len(code)):
            # print(code[i], current_tag, tag_stack)
            if current_tag:
                if code[i] == '>':
                    current_tag += '>'
                    if current_tag[1] == '/':
                        # print('here')
                        if not tag_stack:
                            # print('k,', i, tag_stack, current_tag)
                            return False
                        print(tag_stack[-1], current_tag[2:-1])
                        if tag_stack[-1] == current_tag[2:-1]:
                            # print('here2')
                            if len(tag_stack) == 1 and i != len(code) - 1:
                                # print(i, tag_stack, current_tag)
                                return False
                            current_tag = ''
                            tag_stack.pop()
                    else:
                        tag = current_tag[1:-1]
                        if len(tag) > 9 or len(tag) < 1:
                            return False
                        tag_stack.append(tag)
                        tag_seen = True
                        current_tag = ''
                elif code[i] not in alphs or len(current_tag) > 12:
                    return False
                else:
                    current_tag += code[i]
            elif code[i] == "<":
                current_tag = "<"
        # print(code[i], current_tag, tag_stack)
        return tag_stack == [] and current_tag == ''
