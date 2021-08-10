class Person:
    name = "hihi"
    def __init__(self, name=None):
        self.name = name
an = Person("Văn An")
print("{0} ơi, {1} à".format(an.name, Person.name))