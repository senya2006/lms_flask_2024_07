"""
Основні типи колонок в табличці це integer, Nvarchar, datetime, bool.
Primary key - унікальний індифікатор нашої таблички. Колонка або набір колонок
яка визначає унікальність кожного рядка.
Foreign key - це ключ з іншої таблички,за допомогою нього якраз і будуються зв'язки між іншими
табличками.
Index - ми його використовуємо для швидкого пошуку і коли ми захочемо витягнути щось з колонки.
Але є мінус, вони сповільнюють записування даних.

O(n)
O onatation - для підрахунку складності алгоритмів.

"""
# ВІКОННІ ФУНКЦІЇ
# SUM(), AVG(), COUNT(), MAX(), MIN(), а также специализированные оконные функции, такие как ROW_NUMBER(),
# RANK(), DENSE_RANK(), NTILE(), LAG(), LEAD().
# Ключевое слово OVER: Указывает, что это оконная функция, и определяет, как окно строк будет определено.
# PARTITION BY: Делит набор строк в таблице на группы, на которые будет применяться оконная функция.
# Аналогично GROUP BY, но результат сохраняет исходные строки.
# ORDER BY: Определяет порядок строк в каждой группе.


# -- inner join
# -- в результуючий табличці буде мати тільки спільні данні
#
# -- left join
# -- візьме ті що спільні і з ліва
#
# -- right join
# -- навпаки з left join
#
# -- full join
# -- візьме всі данні
#
# -- anti join
# -- беруться тільки ті що не співпали
#
# -- CRUD
# -- Create
# -- Read
# -- Update
# -- Delete

# CREATE TABLE new_customers
# (
#     CustomerId  INTEGER     not null
#         primary key autoincrement,
#     FirstName   NVARCHAR(40) not null,
#     LastName    NVARCHAR(20) not null,
#     Fax         NVARCHAR(24),
#     Email       NVARCHAR(60) not null,
#     SupportRepId INTEGER
#         references employees
# );
#
# SELECT * FROM new_customers;
#
# INSERT INTO new_customers (FirstName, LastName, Email)
# VALUES ('Semen1', 'Shneider1', 'admin@gmail.com1');
#
# -- DELETE FROM new_customers WHERE CustomerId = 5;
# -- DELETE from "sqlite_sequence" WHERE name = 'new_customers'  -- скидає айдішки і починається зпочатку
# -- drop table new_customers; -- якщо інші видаляли контент то це видаляє повністтю таблчику
