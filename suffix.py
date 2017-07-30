from immdict import ImmDict
from functools import *


def empty_suffix():
    return ImmDict()

def add_word(suffix, word):
    if suffix.get(word) != None:
        return suffix.put(word, suffix.get(word)+1)
    else:
        return suffix.put(word, 1)

def choose_word(chain, prefix, randomizer):
    suffix = chain.get(prefix)
    return aise(suffix, randomizer)

def aise(suffix, randomizer):
    lst = suffix.values()
    sum = reduce(lambda x, y: x + y, lst)
    #print(sum)
    num = randomizer(sum)
    #print(num.__str__() + "Hi")
    index = aise2(lst, num, 0)
    return suffix.keys()[index]

def aise2(lst, num, index):
    if num <= lst[index]:
        return index
    #num = num - lst[index]
    #index += 1
    return aise2(lst, num - lst[index], index + 1)



#def helper(suffix, randomizer):
#    lst = suffix.values()
#    sum = reduce(lambda x, y: x+y, lst)
#    lst_exp = helper2(suffix.keys(), suffix.values(), [])
#    print(lst_exp)
#    if suffix not in list(seq.keys()) or seq[suffix] == []:
#        seq[suffix] = helper3(sum, randomizer,[])
#        print("Hi")
#    num = seq[suffix][0]
#    seq[suffix] = seq[suffix][1:]
#    print(num)
#    print(seq[suffix])
#    return lst_exp[num - 1]

#def helper3(sum, randomizer, lst):
#    if len(lst) == sum:
#        return lst
#    n = randomizer(sum)
#    if n not in lst:
#        lst.append(n)
#    return helper3(sum, randomizer, lst)

#def helper2(lst1, lst2, lst):
    #print(lst)
#    if lst1 == [] and lst2 ==[]:
#        return lst
#    if lst2[0] != 0:
#        lst2[0] = lst2[0] - 1
#        lst.append(lst1[0])
#        return helper2(lst1, lst2, lst)

#    return helper2(lst1[1:], lst2[1:], lst)



#d = ImmDict()
#p = (((d.put('also', 3)).put('been', 5)).put('there', 1))
#chain = ImmDict()
#e = chain.put(('There', 'is'), p)
#print(p.values())
#print(p.keys())
#print(chain.get(('There', 'is')))
#def randomizer(bound):
#    return random.randint(1,bound)

#ctr1 = 0
#ctr2 = 0
#ctr3 = 0
#for i in range(0,100):
#    str = choose_word(e , ('There', 'is'), randomizer)
#    print(str)
#    if (str == 'also'):
#        ctr1 += 1
#    if (str == 'been'):
#        ctr2 += 1
#    if (str == 'there'):
#        ctr3 += 1

#print(ctr1)
#print(ctr2)
#print(ctr3)

    #print(choose_word(e , ('There', 'is'), randomizer))
#print("-------------------------")

#for i in range(0,10):
#    print(randomizer(10))

