# Функция не обладает параметрами и ничего  не возвращает

def func_1():
    print('hello from func_1')

# Функция обладает параметрами и ничего  не возвращает
def func_2(par_0, par_1, p2=100):
    res = par_0 + par_1 * p2
    print(res)

# Функция обладает параметрами и что-то возвращает
def func_3(a, b):
    res = a ** b
    return res


# вызов функции
# func_1()
# func_2(10, 5)
res = func_3(2, 8)

# print(res)

# классы

#  creating class
class Cat:
    # constructor
    def __init__(self, name, age):
        # atributes
        self.name = name
        self.age = age

    # sample methods
    def mur(self):
        res = f'Мяу-мяу, мазафака, я - {self.name}, мне {self.age} лет'
        print(res)

# making examples (objects) of cat class
c_0 = Cat('Братан', 6)
c_1 = Cat('Борис', 11)

# call method 
c_0.mur()
c_1.mur()
