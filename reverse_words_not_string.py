def reverse_words_not_string(s):
    words=s.split()
    final_string=""
    for i in range(len(words)):
        if i!=len(words)-1:
            final_string=final_string+words[i][::-1]+" "
        else:
            final_string=final_string+words[i][::-1]
    return final_string

s="Let's take LeetCode contest"
print(reverse_words_not_string(s))
