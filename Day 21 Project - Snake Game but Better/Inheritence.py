class Animal:

    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("underwater")

    def swim(self):
        print("Movind around underwater")


nemo = Fish()
nemo.breathe()
