def spam(number):
    return 'bulochka'*number


def my_sum(list_of_numbers):
    s=0
    for i in list_of_numbers:
        s+=i
    return s

def shortener(string):
    l=string.split()
        l1=[word[0:6]+'*' if len(word)>6 else word for word in l]
        s=' '.join(l1)
        return s

def compare_ends(words):
    l1=[word for word in words if len(word)>=2 and word[0]==word[-1]]
    return len(l1)
