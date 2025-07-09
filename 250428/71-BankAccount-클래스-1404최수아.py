class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt
        print(f'{self.name} 통장에 {amt}원이 입금된.')
        print(f'{self.name} 현재 잔액은 {self.balance}원')

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print(f'{self.name} 통장에서 {amt}원이 출금됨')
            print(f'{self.name} 현재 잔액은 {self.balance}원')
        else:
            print(f'{self.name} 통장 출금 실패: 잔액 부족 (현재 잔액 {self.balance}원)')

a = BankAccount('123-456')
a.deposit(10000)
a.withdraw(5000)

b = BankAccount('456-789')
b.deposit(2000)