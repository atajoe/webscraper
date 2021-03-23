class Employee:
    amount= 1.08
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}{self.last}@company.com"
        Employee.num_of_emps +=1
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay*Employee.amount)
    
    



class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
            super().__init__(first,last,pay)
            self.prog_lang = prog_lang

emp_1= Employee('George','Smith',50000)
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)
print(Employee.num_of_emps)
dev_1 = Developer('Adam', 'Sandler', 60000, 'C++')
print(dev_1.prog_lang)
#print(emp_1.num_of_emps)
dev_2 = Developer('Maria', 'Sandler', 60000, 'C++')
print(Employee.num_of_emps)