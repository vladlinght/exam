class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._log = []
        return cls._instance

    def log(self, message):
        self._log.append(message)

    def show_log(self):
        for message in self._log:
            print(message)

class InsufficientFundsException(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.logger = Logger()

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.logger.log(f"Attempted to withdraw {amount} from account {self.account_number}. Insufficient funds.")
            raise InsufficientFundsException("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            self.logger.log(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

try:
    account = BankAccount("12345678", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  
except InsufficientFundsException as e:
    print(e)

# Показати журнал логів
logger = Logger()
logger.show_log()
