class Car:
    price = 1000000

    def horse_powers(self, horses):
        self.horses = horses
        return self.horses


class Nissan(Car):
    price = 1100000

    def horse_powers(self, horses):
        self.horses = horses
        return None


class Kia(Car):
    price = 1200000

    def horse_powers(self, horses):
        self.horses = horses
        if self.horses:
            return True
        else:
            return False


car_ = Car()
nissan_ = Nissan()
kia_ = Kia()

print(car_.price)
print(nissan_.price)
print(kia_.price)

print(car_.horse_powers(20))
print(nissan_.horse_powers(30))
print(kia_.horse_powers(40))
print(kia_.horse_powers(0))
