class employee:

    def __init__(self, employee_id, salary, name):
        self.employee_id = employee_id
        self.salary = salary
        self.name = name

        print("welcome", self.name, self.employee_id, self.salary)


e1 = employee(123, 20000, "sudarshan")
e2 = employee(456, 65749, "raghav")
e3 = employee(789, 22980, "andrew")

print(e1.employee_id, e1.salary, e1.name)
print(e2.employee_id, e2.salary, e2.name)
print(e3.employee_id, e3.salary, e3.name)