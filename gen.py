mylist = [x*x for x in range(3)]
print(mylist[0], mylist[1], mylist[2])

mygenerator = (x*x for x in range(3))
print(next(mygenerator))
print(next(mygenerator))

def createGenerator():
  mylist = range(3)
  for i in mylist:
    yield i*i

mygenerator = createGenerator()
print(hex(id(mygenerator)))
# print(mygenerator)
print(next(mygenerator))
print(next(mygenerator))
# print(next(mygenerator))
# print(next(mygenerator))
print('~' * 20)
mygenerator_2 = createGenerator()
print(hex(id(mygenerator)))
for i in mygenerator:
  print(i)


class Bank:
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield "$100"


hsbc = Bank()  # When everything's ok the ATM gives you as much as you want
corner_street_atm = hsbc.create_atm()
print(next(corner_street_atm))

print(next(corner_street_atm))

print([next(corner_street_atm) for cash in range(5)])

hsbc.crisis = True
print(next(corner_street_atm))


symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

