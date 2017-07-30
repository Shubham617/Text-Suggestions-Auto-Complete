import suffix
import prefix
from functools import *

NONWORD = '\n'

def build(name):
    return build_chain(add_to_chain, pairs_gen(name, line_gen), suffix.empty_suffix())




def build_chain(fxn, gen_obj, imm_obj):
    return reduce(fxn, gen_obj, imm_obj)


def add_to_chain(chain, pair):
    if (chain.get(pair[0])) == None:
        #sfx = suffix.empty_suffix()
        return chain.put(pair[0], suffix.add_word(suffix.empty_suffix(), pair[1]))
        #sfx.put(pair[1], 1))

    return chain.put(pair[0], suffix.add_word(chain.get(pair[0]), pair[1]))




def line_gen(name):
    with open(name) as in_file:
        data = in_file.readlines()
        for line in data:
            yield line

def pairs_gen(name, gen_fxn):
    gen = gen_fxn(name)
    start = prefix.new_prefix(NONWORD, NONWORD)
    for line in gen:
        lst = list(line.split())
        for i in lst:
            copy = start
            start = prefix.shift_in(start,i)
            yield ((copy),i)

    yield ((start), NONWORD)





