-- 1. Простые запросы
select * from employee;
select id, name, surname from employee;
select id, name, surname from employee limit 10;
select id, concat(name, ' ', surname) as fio from employee;

-- 2. Применение аггрегирующих функций
select count(*) from employee;
select count(*), max(salary), min(salary), avg(salary) from employee;

-- 3. Применение ограничивающих условий
select count(*) from employee
where salary > 5000;

select count(*) from employee
where salary > 5000 and salary < 8000;

select count(*) from employee
where salary >= 8000 or salary <= 5000;

select count(*) from employee
where name = 'Tom';

select count(*) from employee
where name in ('Tom', 'Mark', 'Kate');

select count(*) from employee
where name like 'A%'; -- % - любое число символов

-- Число сотрудников с именем начинающимся на А и из 4 букв
select count(*) from employee
where name like 'A___'; -- _ - один любой символ

-- Число сотрудников с именем из 4 букв
select count(*) from employee
where length(name) = 4;

-- 4. Группировка и упорядочивание данных
select name, count(name) from employee
where length(name) > 3
group by name;

select name, count(name) as count from employee
where length(name) > 3
group by name
order by count desc;

select name, count(name) as count from employee
where length(name) > 3
group by name
having count(name) >= 150
order by count desc;

-- группировки и упорядочивания отлично подходят при решений для нахождения самых популярных значений
select name, count(name) as count from employee
group by name
order by count desc
limit 3;


-- 5. Join
select c.name, o.country from office o
join company c on o.company_id = c.id;

select distinct c.name, o.country from office o
join company c on o.company_id = c.id
order by name;

-- 6. Вложенные запросы
-- Список сотрудников с зарплатой выше средней
select name, surname from employee
where salary > (select avg(salary) from employee);
