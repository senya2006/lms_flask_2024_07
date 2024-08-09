SELECT * FROM customers;

SELECT FirstName, LastName FROM customers;

SELECT FirstName, LastName AS NAME FROM customers;

SELECT FirstName || '_' || LastName AS FullName FROM customers; -- між ім'ям та прізвищем буде "_" і назва колонки FullName

SELECT Quantity * UnitPrice FROM invoice_items;

SELECT FirstName, LastName FROM customers WHERE FirstName = 'Daan'; -- Where витягує данні

SELECT FirstName, LastName FROM customers WHERE FirstName LIKE 'D%'; -- Починається з букви D

SELECT FirstName, LastName FROM customers WHERE FirstName LIKE '____'; -- Витягне Ім'я з 4 буквами

SELECT * FROM customers WHERE Country = 'USA' AND State = 'CA' OR Country = 'Norway';

SELECT FirstName, LastName FROM customers WHERE Country IN ('USA', 'Spain');

SELECT * FROM customers WHERE CustomerId BETWEEN 1 and 10; -- відрізок від 1 до 10 так само можна і з стрінгою

SELECT * FROM customers ORDER BY FirstName; -- сортування по алфавіту, спадаючий

SELECT * FROM customers ORDER BY FirstName DESC; -- сортування по алфавіту, зростаючий

SELECT * FROM customers ORDER BY CustomerId LIMIT 5 OFFSET 0; -- OFFSET відступає певну кількість рядків

SELECT * FROM customers ORDER BY CustomerId LIMIT 5 OFFSET 10; -- LIMIT якого моменту, тут від 11 включно до 15

SELECT COUNT(*), Country FROM customers GROUP BY Country; -- рахує скільки покупців з кожної країни

SELECT COUNT(*), Country FROM customers GROUP BY Country HAVING Country = 'USA'; -- HAVING дає змогу фільтрувати
-- по от цих погруповані данні, а WHERE фільтрує рядок

SELECT COUNT(*) OVER (PARTITION BY Country), Country FROM customers; -- Просто витягнули данні не стиснули їх

SELECT COUNT(*) OVER (ORDER BY Country), Country FROM customers; -- посортує і потім буде виділяти ті групки

SELECT row_number() OVER (PARTITION BY Country), Country FROM customers; -- виділяє групку і потім в кожній групці виділяє номер рядка

SELECT rank() over (ORDER BY Country), Country FROM customers; -- розділяє на групки і виділяє цифрку для окремої групи

SELECT dense_rank() OVER (ORDER BY Country), Country FROM customers; -- не враховує кількість попередніх, а просто бере наступну цифру

SELECT lag(Country) OVER (ORDER BY Country), Country FROM customers; -- зміщення на один запис і о це зміщення він виводить в окрему колонку

SELECT lag(InvoiceDate) OVER (PARTITION BY CustomerId ORDER BY InvoiceDate) AS LAG1,
    IvoiceDate, CustomerId FROM invoices;

SELECT LAG1 AS PREVIOUS_BUY FROM (
    SELECT lag(InvoiceDate) OVER (PARTITION BY CustomerId ORDER BY InvoiceDate) AS LAG1,
    IvoiceDate, CustomerId FROM invoices
              );

SELECT * FROM albums;

SELECT * FROM artists;

SELECT * FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId; -- з'єднали дві таблички

SELECT artists.Name, albums.Title FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId; -- Показує альбом і хто його виконує

-- inner join
-- в результуючий табличці буде мати тільки спільні данні

-- left join
-- візьме ті що спільні і з ліва

-- right join
-- візьме ті що спільні і з права

-- full join
-- візьме всі данні

-- anti join
-- беруться тільки ті що не співпали

-- CRUD
-- Create
-- Read
-- Update
-- Delete

SELECT * FROM customers;
UPDATE customers SET Company = 'SoftServe', State='Lviv' WHERE CustomerId = 59;

INSERT INTO customers (FirstName, LastName, Email)
VALUES ('Semen1', 'Shneider1', 'admin@gmail.com1');

DELETE FROM customers WHERE CustomerId = 58;


CREATE TABLE new_customers
(
    CustomerId  INTEGER     not null
        primary key autoincrement,
    FirstName   NVARCHAR(40) not null,
    LastName    NVARCHAR(20) not null,
    Fax         NVARCHAR(24),
    Email       NVARCHAR(60) not null,
    SupportRepId INTEGER
        references employees
);

SELECT * FROM new_customers;

INSERT INTO new_customers (FirstName, LastName, Email)
VALUES ('Semen1', 'Shneider1', 'admin@gmail.com1');

-- DELETE FROM new_customers WHERE CustomerId = 5;
-- DELETE from "sqlite_sequence" WHERE name = 'new_customers'  -- скидає айдішки і починається зпочатку
-- drop table new_customers; -- якщо інші видаляли контент то це видаляє повністтю таблчику
