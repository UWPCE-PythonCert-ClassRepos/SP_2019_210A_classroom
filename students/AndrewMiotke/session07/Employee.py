class Employee:
    def __init__(self, name, start_date, coffee_preference):
        self.name = name
        self.start_date = start_date
        self.coffee_preference = coffee_preference

    def print_employee(self):
        print(f" Name: {self.name} \n StartDate: {self.start_date} \n favorite coffee type is: {self.coffee_preference}")


    def employee_sit(self):
        print(f"{self.name} sat at their desk")


    def employee_work(self):
        print(f"{self.name} finally started working")


    def employee_eat(self):
        print(f"{self.name} grabbed a {self.coffee_preference}")


employee = Employee("Gus", "02/23/2019", "latte")
employee.print_employee()
employee.employee_sit()
employee.employee_work()
employee.employee_eat()



class Manager(Employee):
    def __init__(self, name, start_date, coffee_preference, hat):
        super().__init__(name, start_date, coffee_preference)
        self.hat = hat


    def manager_coffee(self):
        print(f"Manager {self.name} grabbed a {self.coffee_preference} coffee")

        if self.hat == True:
            print(f"{self.name} is wearing a hat")
        else:
            print(f"{self.name} should get a hat")



manager = Manager("Rufio", "03/2/2003", "black", True)
manager.manager_coffee()
