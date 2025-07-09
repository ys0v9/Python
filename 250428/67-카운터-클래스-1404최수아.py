class Counter:
    def __init__(self): #생성자, 초기화
        self.count = 0 #인스턴스 변수

    def reset(self, initValue=0):
        self.count = initValue

    def increment(self):
        self.count += 1

    def get(self):
        return self.count 

a = Counter()
b = Counter()

a.reset()
a.increment()
print(a.get())

b.reset(100)
b.increment()
print(b.get()) 
