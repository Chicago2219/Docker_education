class Cat:
    def __init__(self, name=None, color=None):
        self.name = name
        self.color = color

    @classmethod
    def name(cls):
        return cls.__name__


cat_1 = Cat("Муся", "Рыжий")
cat_2 = Cat("Барсик", "Белый")
print(cat_1.__dict__)
print(cat_2.__dict__)
print(Cat.name)
