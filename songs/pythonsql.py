import sqlite3
from employee import Employee


conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
# 	first TEXT,
# 	last TEXT,
# 	pay INTEGER
# 	)""")

# emp1 = Employee('John', 'Doe', 8000)
# emp1 = Employee('Jane', 'Doe', 9000)

# print(emp1.first)

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': 'Helmut', 'last': 'Heimut', 'pay': 30000})

# conn.commit()

def get_emp_by_name(lastname):
	with conn:
		c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
		return c.fetchall()

# c.execute("SELECT DISTINCT * FROM employees")
emps = get_emp_by_name('Heimut')

print(emps)
# conn.commit()

conn.close()