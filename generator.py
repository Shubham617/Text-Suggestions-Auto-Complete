import suffix
import prefix

def get_word_list(chain, prefix, randomizer, num, NONWORD):
    lst = helper(chain, prefix, randomizer, num, NONWORD, [])
    #print(l1)
    #print(lst)
    return tuple(lst)

def helper(chain, pfx, randomizer, num, NONWORD, lst):
    str = suffix.choose_word(chain, pfx, randomizer)
    if str == NONWORD:
        return lst
    if len(lst) == num:
        return lst

    return helper(chain, prefix.shift_in(pfx, str), randomizer, num, NONWORD, lst+[str])

def generate(chain, randomizer, num, NONWORD):
    space = ' '
    tup = get_word_list(chain, (NONWORD, NONWORD), randomizer, num, NONWORD)
    return space.join(tup)

#l1 = [1,2,4]
#l2 = l1 + [4]
#print(l1)
#print(l2)
#t = ('a','b')
#print(t.__str__())



