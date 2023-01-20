PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

A company has different types of employees and requires to manage the calculation of their salaries based
on different parameters. Figure 1 illustrates the different types of employees of this company which are the
following types: Employee, Permanent Employee, Temporary Employee, Consultant, Manager and
Consultant Manager.

• Employee has the following properties: name, id and salary.

• Permanent_Employee is a Employee. A Permanent Employee has benefits that he/she can se-
lect from [”health insurance”], [”retirement”], or both [”retirement”, ”health insurance”]. Imple-
ment a method cal salary() to calculate the actual salary based on selected benefits. If benefits =
[”health insurance”] then return salary ∗0.9, if [”retirement”] then salary ∗0.8 and if benefits =
[”retirement”, ”health insurance”] is selected then salary ∗0.7.

• Temporary_Employee has a property ”hours” which is the working hours per mount. The salary
property represents the amount that a temporary employee is paid per hour. Implement a method
cal salary() to calculate the actual salary by returning salary ∗hours

• A Consultant is a Temporary Employee and has in addition to travel. The property
travel represents number of travel trips that a Consultant has to do and is paid additionally 1000
dollar for each travel. Implement a method cal salary() to calculate the actual salary similar to a
Temporary Employee with an additional payment of travel ∗1000. (Tip: Try to reuse your code as
much as possible to avoid having duplicated code)

• A Manager is a special type of employee and is paid with a bonus payment in addition
to his/her main salary. Manager has a property bonus which adds to his/her main salary on top.
Implement a method cal salary() to return salary + bonus

• Consultant_Manager is a Consultant and is a Manager as well. A Consultant Manager has travel,
hours of work and bonus payment. Implement a method cal salary() to calculate the salary similar to
a Temporary Employee and Consultant with an additional bonus payment. The cal salary() method
should return salary ∗hours + travel ∗1000 + bonus

Also, please consider the following implementation instructions for this assignment:

• Each of your class constructors should use the following format ” init (self, **kwargs)”

• Each of your classes should have a string method implementation (Define str (self) in each of your
classes). You can design a string method to represent the objects in a string format.

• The main() function prints out statements to test the other functions; hence, no input data is needed.
