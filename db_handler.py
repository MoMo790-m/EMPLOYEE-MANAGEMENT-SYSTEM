import sqlite3

def create_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Employees(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(70),
                       role TEXT,
                       salary FLOAT,
                       department TEXT,
                       hire_date DATE,
                       sex VARCHAR(6) CHECK(sex IN('Male','Female')),
                       status TEXT)
        ''')
    conn.commit()
    conn.close()

def get_all_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def add_employee(name, role, salary, department, hire_date, sex, status):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Employees(name, role, salary, department, hire_date, sex, status)
                   VALUES (?,?,?,?,?,?,?)
                   ''', (name, role, salary, department, hire_date, sex, status))
    conn.commit()
    conn.close()

def remove_employee(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def delete_all_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees')
    conn.commit()
    conn.close()

def update_employee_record(id, new_name, new_role, new_salary, new_department, new_hire_date, new_sex, new_status):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('''
                   UPDATE Employees SET name = ?, role = ?, salary = ?, department = ?, hire_date = ?, sex = ?, status = ?
                   WHERE id = ?
                   ''', (new_name, new_role, new_salary, new_department, new_hire_date, new_sex, new_status, id))
    conn.commit()
    conn.close()

def is_employee_exists(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()