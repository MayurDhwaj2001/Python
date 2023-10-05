class Computer:
    def __init__(self, cpu, ram):  # <--------------------called every time method is called ie. line 13 & 14
        self.c = cpu
        self.r = ram

    def config(self):
        print("Configration:", self.c, self.r)


com1 = Computer("i5", "16gb")
com2 = Computer("Ryzen 3", "8gb")

com1.config()
com2.config()
