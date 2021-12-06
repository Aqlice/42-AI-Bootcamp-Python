import sys

class Account:
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

class Bank:
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        if not isinstance(amount, int) or amount < 1:
            sys.exit("invalid transaction")
        if not isinstance(origin, Account) or not isinstance(dest, Account):
            sys.exit("invalid Account")
        if len(getattr(origin)) % 2 == 0 or \
        hasattr(origin, 'b*') or \
        not hasattr(origin, 'zip*') or \
        not hasattr(origin, 'addr*') or \
        not origin.name or not origin.id or not origin.value:
            sys.exit("Corrupted account : origin")
        elif len(getattr(dest)) % 2 == 0 or \
        hasattr(dest, 'b*') or \
        not hasattr(dest, 'zip*') or \
        not hasattr(dest, 'addr*') or \
        not dest.name or not dest.id or not dest.value:
            sys.exit("Corrupted account : dest")
        if amount > origin.value:
            sys.exit("Not enough funds")
        
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            NOT FINISHED"""

bank = Bank
account = Account
account.transfer