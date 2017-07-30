import builder
import generator
import random

def randomizer(bound):
    return random.randint(1, bound)

if __name__ == "__main__":
    file_name = 'books/aladdin.txt'
    chain = builder.build(file_name)
    #print(chain.imm_dict)
    #lst = chain.values()
    #for i in lst:
    #    print(i.keys())
    num_words = 25
    outstr = generator.generate(chain, randomizer, num_words, builder.NONWORD)
    print(outstr)