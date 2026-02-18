import requests


class Employee():
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def raise_pay(self):
        self.pay = int(self.pay*self.raise_amt)

    def monthly_schedule(self, month):
        res = requests.get(f"http://server:port/{self.last}/{month}")
        if res.ok:
            return res.text
        else:
            return "Bad Response!"
