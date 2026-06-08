class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_emps += 1
    
    @property    
    def fulname(self):
        return "{} {}".format(self.fname, self.lname)
    @fulname.setter
    def fulname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last
    @fulname.deleter
    def fulname(self):
        print("Name has been deleted.")
        self.fname = None
        self.lname = None
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"
    def apply_raise(self):
        self.pay = int(int(self.pay) * self.raise_amount)
        return self.pay
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp):
        fname, lname, pay = emp.split(",")
        return cls(fname, lname, pay)
    @classmethod
    def from_string_all(cls, emp):
        return cls(*emp.split(","))
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    def __add__(self, other):
        int_self = int(self.pay)
        int_other = int(other.pay)
        return int_self + int_other 
    def __len__(self):
        return len(self.fulname())
        
    
class data_scientist(Employee):
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang
    
    @classmethod    
    def from_str_ds(cls, ds):
        return super().from_string_all(ds)
    
class Manager(Employee):
    def __init__(self, fname, lname, pay, employees = None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rmv_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def show_emp(self):
        for emp in self.employees:
            return "--> " + emp.fulname()
    def __repr__(self):
        return f"Manager('{self.fname}', '{self.lname}', '{self.pay}')"
    def __str__(self):
        return f"full name is {self.fulname()} \nemail: {self.email}"
 
   
emp_1 = ("Ratul, Shariar, 1000000")
emp_2 = ("Monira, Yeasmin, 80000")

neww_emp_1 = Employee.from_string(emp_1)
neww_emp_2 = Employee.from_string(emp_2)

ds_1 = ("Ratul, Shariar, 1000000, Python")
ds_2 = ("Chorey, Schafer, 100000000000, Python")

new_ds_1 = data_scientist.from_str_ds(ds_1)
new_ds_2 = data_scientist.from_str_ds(ds_2)

mgr_1 = Manager("Chorey", "Schafer", "100000000000", [new_ds_1])

print(repr(mgr_1))
print(str(mgr_1))

print(neww_emp_1 + neww_emp_2)
print(len(neww_emp_2))

# print(mgr_1.email)
# print(mgr_1.show_emp())


# print(new_mgr_1.show_emp)

# print(new_mgr_1.email)

# print(new_ds_1.__dict__, "\n", new_ds_2.__dict__)




# import datetime

# date = datetime.date(2026, 6, 7)

# print(Employee.is_workday(date))



# print(neww_emp_1.__dict__, "\n", neww_emp_2.__dict__ )

# emp_2.set_raise_amt(1.06)

# print(emp_1.fname)
# print(emp_2.email)

# print(Employee.email(emp_1))
# print(Employee.email(emp_1))
# print(Employee.apply_raise(emp_1))
# print(Employee.__dict__)
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.num_of_emps)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)