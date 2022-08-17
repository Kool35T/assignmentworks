from Creditcard import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and
    fees."""
    def __init__(self, customer, bank, acnt, limit, apr, charge_count):
        """Create a new predatory credit card instance."""
        super()._init_(customer, bank, acnt, limit)
        self._apr = apr
        self._charge_count = 0

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit
        limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        self._charge_count += 1
        if self._charage_count > 10:
            print("after 10 transaction $1 charged")
            self._balance += 1

        success = super().charge(price)
        if not success:
            self._balance += 5
            print("$5 penalty charge")
            return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        self._charge_count = 0

        if self._balance >0:
            
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance += self._apr

if __name__ == '__main__':

    for val in range(1, 17):
        wallet = []
        wallet.append(CreditCard('John Lee', 'DBS',
                             '5391 0375 9387 5309', 2500) )
        wallet.append(CreditCard('John Lee', 'OCBC',
                              '3485 0399 3395 1954', 3500) )
        wallet.append(CreditCard('John Lee', 'Maybank',
                             '5391 0375 9387 5309', 5000) )
                             
        wallet[0].charge(200)
        print('transaction number:', val)
        print(": charge $200 balance =", wallet[0].get_balance())

