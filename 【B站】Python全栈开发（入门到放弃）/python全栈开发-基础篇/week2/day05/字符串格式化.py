name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

msg = """
---------- info of  %s ----------
Name : %s
Age  : %s
Job  : %s
Salary: %s
----------     end     ----------
""" % (name, name, age, job, salary)

print(msg)

if salary.isdigit():    # 是不是数字
    print("salary 是数字")
else:
    print("不是数字")


