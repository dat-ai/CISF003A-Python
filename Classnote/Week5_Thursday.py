class Animal:
    def __init__(self, name=""):
        """

        :param name:
        """
        self.name = name

    def make_noise(self):
        print("I am a " + self.name)


class Dog(Animal):
    def __init__(self, dog_name ="Alsatian"):
        """

        :param dog_name:
        """
        super().__init__("Dog")
        self.d_type = dog_name
    # Over-riding make noise

    def make_noise(self):
        print("I am a " + self.d_type + " " + self.name)


class Cat(Animal):
    def __init__(self, type="Taby Cat"):
        super().__init__()
        self.cat_type = type

    def make_noise(self):
        print("Meow Meow: I am a(n) " + self.cat_type + self.name)


class Lion(Cat):
    def __init__(self ):
        super().__init__()
        self.cat_type = "Lion"

    def make_noise(self):
        print("Hear me roar! I man the Lion and if you don't think I am a cat then that is your problem.")

if __name__ == "__main__":
    first = Animal("Platypus")
    second = Dog("Chihuahua")
    ls = [first, second]  # Type Animal
    for i in ls:
    for i in ls:
        i.make_noise()
    third = Lion()
    third.make_noise()
    ls2 = [third, second, first]
    ls3 = map(lambda  x:x.name, ls2)
    for i in ls3:
        print(i)