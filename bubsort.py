from time import sleep
from orig import gen_orig

class BubbleSort():
    def __init__(self, min=10, max=20):
        self.orig = gen_orig(min, max)
        print(self.orig)
        self.bubble_sort(self.orig)
    
    def bubble_sort(self, target:list):
        unsorted = True
        
        while unsorted:
            changed = False
            for i in target:
                try:
                    k = target[target.index(i)+1]
                    if i > k:
                        target[target.index(k)], target[target.index(i)] = i, k
                        changed = True
                        print(f"\r{target}", end="", flush=True)
                        break
                    else:
                        continue
                except IndexError:
                    if not changed:
                        unsorted = False
                        print(f"\r{target}", flush=True)                       
                        break
                        
    
if __name__ == "__main__":
    BubbleSort()