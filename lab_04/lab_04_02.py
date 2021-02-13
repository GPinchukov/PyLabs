class Worker:
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


w1 = Worker('Boris', 'Borisov')
print('w1.count: ', w1.count)
w2 = Worker('Grigory', 'grigorev')
print('w2.count: ', w2.count)
print('w1.count: ', w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print('Worker.__name__ :', Worker.__name__)
print('Worker.__dict__: ', Worker.__dict__)
print('Worker.__doc__:', Worker.__doc__)
print('Worker.__bases__ :', Worker.__bases__)


class Animal:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1
        self.id = Animal.count  # в отличии от задания 8, атрибут id становится уникальным для каждого объекта класса

    def display(self):
        print('Animal id: ', self.id)
        print('Name: ', self.name)
        print('Age: ', self.age)


zebra = Animal('Egor', 5)
elepthant = Animal('Dasha', 7)
giraffe = Animal('Alexey', 4)

zebra.display()
elepthant.display()
giraffe.display()