class Counter:
    def __init__(self, count): 
        self.count = 0    
        self.initValue = count  

    def reset(self):
        self.count = self.initValue  

    def increment(self):
        self.count += 1

    def get(self):
        return self.count 

a = Counter(0)
b = Counter(100)

a.reset()
a.increment()
print(a.get())

b.reset()
b.increment()
print(b.get()) 
