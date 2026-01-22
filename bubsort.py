import random
from time import sleep
import tkinter as tk
import ttkbootstrap as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()


class BubbleSort():
    def __init__(self, min:int=1, max:int=255):
        self.bubble_sort(self.gen_orig(min, max))
    
    def gen_orig(self, min, max):
        self.orig = [i for i in range(random.randint(min,random.randint(2,max)))]
        random.shuffle(self.orig)
        print(self.orig)
        sleep(0.01)
        return self.orig
    
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
                        print(target)
                        sleep(0.01)
                    else:
                        continue
                except IndexError:
                    if not changed:
                        unsorted = False
                        break
    
if __name__ == "__main__":
    App()