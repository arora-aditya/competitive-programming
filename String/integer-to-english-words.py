def numberToWords(num):
    """
    https://leetcode.com/problems/integer-to-english-words/description/
    :type num: int
    :rtype: str
    """
    if num == 0:
            return "Zero"
        words = ""
        ones = ["",'One ', 'Two ', 'Three ', 'Four ','Five ','Six ','Seven ','Eight ','Nine ']
        tens = ["",'Ten ','Twenty ','Thirty ','Forty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ']
        specialtens = ["Ten ",'Eleven ','Twelve ','Thirteen ','Fourteen ','Fifteen ','Sixteen ','Seventeen ','Eighteen ','Nineteen ']
        positions = ["",'Thousand ','Million ','Billion ']
        def hundred(num1):
            num1 = int(num1)
            word = ""
            word += ones[num1//100]
            if num1//100 != 0:
                word += "Hundred "
            if (num1%100)//10 != 1:
                word += tens[(num1%100)//10]
                word += ones[num1%10]
            else:
                word += specialtens[(num1%10)]
            return word
        
        st = str(num)[::-1]
        length_of_num = len(st)
        st = [st[i:i+3][::-1] for i in range(0,length_of_num, 3)]
        length_of_num = len(st)
        for nu in range(length_of_num):
            to_be_added = ""
            to_be_added = hundred(st[nu])
            if to_be_added != "":
                to_be_added += positions[nu]
            words = to_be_added + words
        return words[:len(words)-1]
