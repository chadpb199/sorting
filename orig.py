import random

def gen_orig(min, max):
        orig = [i for i in range(random.randint(min,random.randint(min,max)))]
        random.shuffle(orig)
        return orig