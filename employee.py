#  File: employee.py
#  Description: This code creates classes of employees to practice
#  methods of inheritance overwriting and overloading

#  Student Name: Gaytri Riya Vasal
#  Course Name: CS 313E
#  Unique Number: 86439
#  Date Created: 6/12/22
#  Date Last Modified: 6/12/22


class Employee:
    """ This is the base class for all of the other classes. This class
    initializes name, ID, and salary for anyone that works at
    the company"""

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    def __str__(self):
        return str(self.name) + ' is an employee with id ' + str(self.id) + \
               ' making a salary of ' + str(self.salary)


############################################################
############################################################
############################################################


class Permanent_Employee(Employee):
    """ This is a subclass of Employee. A permanent employee inherits
    all the attributes of an Employee and has benefits like health
    insurance and retirement depending on if they select them."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits')

    # salary is calculated at 10 percent reduction if H.I. is included,
    # 20 percent reduction is Ret. included and 30 percent reduction if
    # both included
    def cal_salary(self):
        if self.benefits == ["health_insurance"]:
            return self.salary * 0.9
        elif self.benefits == ["retirement"]:
            return self.salary * 0.8
        elif self.benefits == ["retirement", "health_insurance"]:
            return self.salary * 0.7

    def __str__(self):
        return str(self.name) + ' is an permanent employee with id ' + \
               str(self.id) + ' making a salary of ' + str(self.salary) + ' ' \
               + 'due to the benefit of ' + str(self.benefits)

############################################################
############################################################
############################################################


class Manager(Employee):
    """ This is a subclass of Employee. A manager inherits
    all the attributes of an Employee and has a bonus that contributes to
    their salary."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus')

    # The salary is calculated by adding the bonus attribute to the
    # salary.
    def cal_salary(self):
        return self.salary + self.bonus

    def __str__(self):
        return str(self.name) + ' is an Manager with id ' + \
               str(self.id) + ' making a salary of ' + str(self.cal_salary())


############################################################
############################################################
############################################################


class Temporary_Employee(Employee):
    """This is a subclass of employee. A Temp Employee inherits all the
    attributes of an employee but also has an hours attribute that helps
    correct the salary when calculating salary"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours')

    # The salary is calculated by multiplying the salary attribute and
    # the unique hours attribute.
    def cal_salary(self):
        return self.salary * self.hours

    def __str__(self):
        return str(self.name) + ' is an temporary employee with id ' + \
               str(self.id) + ' making a salary of ' + str(self.cal_salary()) \
               + ' for ' + str(self.hours) + ' hours'


############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):
    """ Consultant is a subclass of the Temp Employee Class. This class
    inherits all the Temp Employee and employee attributes. This also
    has a unique attribute called travel, which helps adjust the pay for
    the method calc_salary."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel')

    # Calculates salary exactly like a temp employee with a bonus for
    # any related travel
    def cal_salary(self):
        return super().cal_salary() + self.travel * 1000

    def __str__(self):
        return str(self.name) + ' is an Consultant employee with id ' + \
               str(self.id) + ' making a salary of ' + str(self.cal_salary()) \
               + ' for ' + str(self.hours) + ' hours and ' + str(self.travel) \
               + ' trips'

############################################################
############################################################
############################################################


class Consultant_Manager(Manager, Consultant):
    """ Consultant Manager is a subclass of the Consultant class and
    the Manager class. This class inherits all the attributes from
    manager and consultant. The salary is calculated like a consultant,
    but inherits bonuses similar to a manager"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)

    # Pulls from Consultant salary calculation and uses bonuses from
    # manager
    def cal_salary(self):
        return self.bonus + Consultant.cal_salary(self)

    def __str__(self):
        return str(self.name) + ' is an Consultant employee with id ' + \
               str(self.id) + ' making a salary of ' + str(self.cal_salary()) \
               + ' for ' + str(self.hours) + ' hours and ' + str(self.travel) \
               + ' trips and a bonus of ' + str(self.bonus)


############################################################
############################################################
############################################################

# DO NOT CHANGE THE MAIN FUNCTION

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
    main()
