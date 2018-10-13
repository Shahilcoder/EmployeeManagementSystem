import sqlite3
from sqlite3 import Error

def create_connection():
	try:
		conn = sqlite3.connect("skyland_corp.db")
		return conn
	except Error as e:
		print(e)

	finally:
		conn.commit()

	return None

def create_table_employees(conn):
	try:
		create_table_employees_sql ='''CREATE TABLE IF NOT EXISTS employees(
        	                                Id integer PRIMARY KEY,
            	                            Name text NOT NULL,
                	                        Mobile_number integer NOT NULL,
                    	                    Address text NOT NULL,
                        	                Branch text NOT NULL,
                            	            Salary integer NOT NULL);'''
		cursor = conn.cursor()
		cursor.execute(create_table_employees_sql)

		print('table created')

	except Error as e:
		print(e)

	finally:
		conn.commit()

def create_employee(conn, employee):
	try:
		create_employee_sql = '''INSERT INTO employees(Name, Mobile_number, Address, Branch, Salary)
								VALUES (?,?,?,?,?)'''
		cur = conn.cursor()
		cur.execute(create_employee_sql, employee)
		
		print('employee created')
	except Error as e:
		print(e)

	finally:
		conn.commit()

def update_employee(conn, employee):
	try:
		update_employee_sql = '''UPDATE employees
								SET Name = ?,
									Mobile_number = ?,
									Address = ?,
									Branch = ?,
									Salary = ?
								WHERE Id = ?'''
		cur = conn.cursor()
		cur.execute(update_employee_sql, employee)
		
		print('employee updated')
	except Error as e:
		print(e)

	finally:
		conn.commit()

def delete_employee(conn, Id):
	try:
		delete_employee_sql ='''DELETE FROM employees WHERE Id = ?'''

		cur = conn.cursor()
		cur.execute(delete_employee_sql, (Id,))
		
		print('employee deleted')
	except Error as e:
		print(e)

	finally:
		conn.commit()

def delete_all_employees(conn):
	try:
		delete_all_employees_sql = '''DELETE FROM employees'''

		cur = conn.cursor()
		cur.execute(delete_all_employees_sql)

		print("all employees deleted")
	
	except Error as e:
		print(e)

	finally:
		conn.commit()

def show_employees_table(conn):
	try:
		show_employees_table_sql = '''SELECT * FROM employees'''

		cur = conn.cursor()
		cur.execute(show_employees_table_sql)

		print("all employees shown")

		rows = cur.fetchall()

		return rows

	except Error as e:
		print(e)

	return None

def start_service():
	conn = create_connection()
	if conn is not None:
		create_table_employees(conn)

		with conn:
			employee = ('Sahil Hussain', 8439482440, 'Gorabazar, West Bengal', 'None', 40000)
			create_employee(conn, employee)

			employee_update = ('Shahilsky', 7017179196, 'Rosemarry school, West Bengal', 'None', 45000, 1)
			update_employee(conn, employee_update)

			delete_employee(conn, 1)
			#delete_all_employees(conn)
	else:
		print('database connection failed')

if __name__ == '__main__':
	start_service()
