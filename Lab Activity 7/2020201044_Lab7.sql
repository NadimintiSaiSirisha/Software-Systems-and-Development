#q1
# Find the names of all employees have ‘Jennifer Wallace’ as their direct supervisor.
SELECT FName, LName FROM EMPLOYEE WHERE Super_ssn IN( SELECT Ssn FROM EMPLOYEE WHERE Fname="Jennifer" AND LName="Wallace");

#q2
# Retrieve the name of each employee who has a dependent with the same first name and same sex as the employee.
SELECT Fname, LName FROM EMPLOYEE e JOIN DEPENDENT d ON e.Ssn = d.Essn WHERE e.FName = d.Dependent_Name AND e.Sex = d.Sex;

#q3
# Retrieve the names of all employees in department 5 who work more than 10 hours per week on the Product X project.
SELECT e.FName, e.LName FROM EMPLOYEE e WHERE e.Ssn IN (SELECT w.Essn FROM WORKS_ON w WHERE w.PNo IN (SELECT p.PNumber FROM PROJECT p WHERE p.PName="ProductX") AND w.Hours>10);

#q4
# For every project located in ‘Stafford’, list the project number, the controlling department number, and the department manager’s last name, address, and birthdate.
SELECT p.PNumber,p.Dnum, e.LName, e.Address, e.Bdate FROM PROJECT p JOIN DEPARTMENT d ON d.Dnumber = p.Dnum JOIN EMPLOYEE e ON d.Mgr_ssn = e.Ssn WHERE p.Plocation="Stafford";

#q5
# Retrieve the name of each employee who works on all the projects controlled by department number 5.
SELECT e.FName, e.LName FROM EMPLOYEE e WHERE NOT EXISTS (SELECT p.Pnumber FROM PROJECT p WHERE p.Dnum=5 AND p.Pnumber NOT IN (SELECT w.Pno FROM WORKS_ON w WHERE w.Essn=e.Ssn));
