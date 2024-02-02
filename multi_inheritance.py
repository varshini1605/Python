class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name="class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name="class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def show(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)




c = C()
print(C.__mro__)#to check class orders
c.show()