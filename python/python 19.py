class Salary:
    '''算工资'''
    def __call__(self, salary):
        daysalary=salary/30
        hoursalary=daysalary/24
        return  dict(daysalary=daysalary,hoursalary=hoursalary,salary=salary)

s=Salary()
print(s(5000))