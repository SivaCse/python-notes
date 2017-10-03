'''sqlite3 Example'''

# This is a modified version of sqlite3_example.py. In continuing to explore
# ways of storing and retreiving both UTC and local time, this example includes
# a column in the history table that contains a pickled datetime object which
# is the local time zone (PDT). This pickled object can then unpickled and
# displayed later. This whole example is probably overkill for most situations
# but may prove useful as an example alone.

import sqlite3
import datetime
import pytz
import pickle # <-- added

db = sqlite3.connect('accounts.sqlite')
db.execute('''CREATE TABLE IF NOT EXISTS accounts
              (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)''')
# added timezone column to the history table:
db.execute('''CREATE TABLE IF NOT EXISTS history
              (time TIMESTAMP NOT NULL, account TEXT NOT NULL,
              amount INTEGER NOT NULL, timezone INTEGER NOT NULL,
              PRIMARY KEY (time, account))''')

class Account():

    @staticmethod
    def _current_time():
        # changed this to return both utc time and local time zone:
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        timezone = local_time.tzinfo
        return utc_time, timezone # <-- returns a tuple

    def __init__(self, name: str, opening_balance: int=0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row
            print('Retrieved record for {}'.format(self.name))
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print('Account created for {}'.format(self.name))
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        time, timezone = Account._current_time() # <-- unpack the tuple
        pickled_timezone = pickle.dumps(timezone) # <-- pickle the time zone
        db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
        # add the pickled_timezone the update:
        db.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (time, self.name, amount, pickled_timezone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int):
        if amount > 0.0:
            self._save_update(amount)
            print('{:.2f} deposited'.format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int):
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print('{:.2f} withdrawn'.format(amount / 100))
            return amount / 100
        else:
            print('Amount must be greater than 0 and not exceed balance')
            return 0.0

    def show_balance(self):
        print('Balance on account {} is {:.2f}'.format(self.name, self._balance / 100))


# Testing ---------------------------------------------------------------------

if __name__ == '__main__':
    rick = Account('Rick')
    morty = Account('Morty', 50000)
    pingpong = Account('Ping Pong', 10000)
    boktoktok = Account('Boktoktok', 2000)

    # rick.deposit(10010)
    # rick.deposit(49910)
    # rick.deposit(5510)
    # rick.withdraw(8000)
    # morty.withdraw(1000)

    db.close()

print('-' * 50)

# Get the pickled timezone ----------------------------------------------------

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    pickled_timezone = row[3]
    timezone = pickle.loads(pickled_timezone)
    local_time = pytz.utc.localize(utc_time).astimezone(timezone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))