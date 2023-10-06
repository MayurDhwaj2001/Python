class Parent:
    def phone(self):
        print("Nokia")


class Me(Parent):
    def phone(self):
        print("Oppo")


obj = Me()
obj.phone()
