# 1)создать класс SuperHero с атрибутом класса people='people'

# def name(a,b):...
# class SuperHero:
#     people ='people'

# 2)создать конструктор класса с атрибутами name,nickname,superpower,health_points,
# catchphrase.

    # def __init__(self,name,nickname,superpower,health_points):
    #     self.name = name
    #     self.nicname = nickname
    #     self.superpower = superpower
    #     self.health_points = health_points

# 5) добавить магический метод который 
# выводит прозвище героя,его суперспособность и его здоровье


    # def __str__(self):
    #     return f'{self.name}\n' \
    #            f'{self.nicname}\n' \
    #            f'{self.superpower}\n' \
    #            f'{self.health_points}'

# 6)создать магический метод который считает длину коронной фразы героя 

#     def __len__(self):
#         return len(self)           

# a = SuperHero('Tony Stark','stark','iron man',100)
# print(len(a.name))

# 3)добавить метод который выводит имя героя

# print(a.name)

# 4)добавить метод который умножает здоровье героя на 2 

# print(a.health_points * 2)


   
class Hero:

    people ='people'

    def __init__(self,name,nickname,superpower,health_points):
        self.name = name
        self.nicname = nickname
        self.superpower = superpower
        self.health_points = health_points


    def __str__(self):
        return f'{self.name}\n' \
               f'{self.nicname}\n' \
               f'{self.superpower}\n' \
               f'{self.health_points}'

a = Hero('Tony Stark','stark','iron man',100)
print(a)
  
print(a.name)  

print(a.health_points * 2)


def __len__(self):
        return len(self) 
print(len(a.name)) 