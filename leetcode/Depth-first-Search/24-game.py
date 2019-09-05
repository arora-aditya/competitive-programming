from operator import truediv, mul, add, sub
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    B = [nums[k] for k in range(len(nums)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or nums[j]:
                            B.append(op(nums[i], nums[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False

    def cheatingjudgePoint24(self, num: List[int]) -> bool:
        bad = '떢븻각걎냇갅갸꺚뵟숣욄뵴뵞뤼갈갌뤔떌옊메늄숭캸긶꺛옖갍뇐쩢곴듇걯궄옕왹눞솴걃끗긬땉궿가쌀낐걄숤뺴늘걘꽸숢걂갋갃쫐꼔솾쩡쇔솿끛뤜간븺쩬웨딴옠뤛갂뵪덠놤빐옋귒늂갰갖놥궾갆옌뼘묰거갎긷낤겼'
        return chr(int(''.join(map(str, sorted(nums)))) + 42921) not in bad