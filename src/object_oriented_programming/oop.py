# class User:
#     count = 0

#     def __init__(self):
#         User.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count
# u=User()
# p=User()
# print(u.get_count())

from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def play(self):
        pass

    def details(self):
        return f"Owner: {self._owner}"


class Drum(Instrument):
    def play(self):
        return "Drum goes: Boom Boom"


class Flute(Instrument):
    def play(self):
        return "Flute goes: Fii Fii"


class EchoBox(Instrument):
    def play(self, times=1):
        return ("EchoBox says: Echo! " * times).strip()


def perform(instrument: Instrument):
    print(instrument.details())
    print(instrument.play())
    print("-----")


d = Drum("Ravi")
f = Flute("Neha")
e = EchoBox("Aman")

perform(d)
perform(f)
perform(e)

print(e.play())
print(e.play(3))
