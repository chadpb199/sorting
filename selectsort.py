from time import sleep
from orig import gen_orig

class SelectSort():
    def __init__(self, min=10, max=20):
        self.orig = gen_orig(min, max)
        print(self.orig)
        self.select_sort(self.orig)
        
    def select_sort(self, target):
        unsorted = True
        smallest = 0
        
        while unsorted:
            for i in target:
                if i == smallest:
                    k = target[i]
                    if i == k:
                        if i + 1 == len(target):
                            unsorted = False
                            break
                        else:
                            smallest += 1
                            continue
                    else:
                        target[target.index(i)], target[i] = k, i
                        smallest += 1
                        break
                else:
                    continue
            
            print(f"\r{target}", end="", flush=True)
        
        print(f"\r{target}", flush=True)
if __name__ == "__main__":
    SelectSort()