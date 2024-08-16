# class Point:
#     __slots__ = ('x', 'y')  # визначаємо атрибути які будемо використовувати і інші вже не можна буде додати
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print(x, y)
#
#
# point = Point(10, 15)
#
# додавання нового атрибуту але з функцією __slots__ це неможливо
# point.z = 20


my_class = type('MyClass', (object, ), {'first_name': 'Semen',
                                        'last_name': 'Shneider'})

# print(my_class)     # <class '__main__.MyClass'>
# print(type(my_class))      # <class 'type'>

# print(type('x'))      # <class 'str'>

# my_object = my_class()
# print(my_object)    # <__main__.MyClass object at 0x000001D3204C6C90>
# print(my_object.first_name)     # Semen
