SELECT MAX(months*salary), COUNT(*)
FROM Employee
WHERE months*salary = (select max(salary * months) from employee);
