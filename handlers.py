from datetime import datetime
import db_handler
import tkinter as tk
from tkinter import messagebox

global selected_id
selected_id = None

def add_to_treeview(tree):
    employees = db_handler.get_all_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', tk.END, values=employee)

def add_employee(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry, tree):
    name = name_entry.get()
    role = role_entry.get()
    salary = salary_entry.get()
    department = department_entry.get()
    hire_date = hire_date_entry.get()
    gender = gender_var.get()
    status = status_entry.get()
    
    if not (name and role and salary and department and hire_date and gender and status):
        messagebox.showerror('Error', 'All fields are required')
        return
    try:
        salary = float(salary)
        if salary < 0:
            messagebox.showerror('Error', 'Salary must be a positive number')
            return
    except ValueError:
        messagebox.showerror('Error', 'Salary must be a number')
        return
    
    try:
        datetime.strptime(hire_date, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror('Error', 'Hire Date must be in the format YYYY-MM-DD')
        return
    
    if name.isdigit() or role.isdigit() or department.isdigit() or status.isdigit():
        messagebox.showerror('Error', 'Name, Role, Department, and Status must contain letters')
        return
    
    db_handler.add_employee(name, role, salary, department, hire_date, gender, status)
    add_to_treeview(tree)
    clear_fields(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry)
    messagebox.showinfo('Success', 'Employee added successfully')

def clear_fields(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry):
    name_entry.delete(0, tk.END)
    role_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    hire_date_entry.delete(0, tk.END)
    gender_var.set('Male')
    status_entry.delete(0, tk.END)
    global selected_id
    selected_id = None

def select_employee(event, tree, name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry):
    global selected_id
    selected_item = tree.focus()
    values = tree.item(selected_item, 'values')
    
    if values:
        selected_id = values[0]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[1])
        role_entry.delete(0, tk.END)
        role_entry.insert(0, values[2])
        salary_entry.delete(0, tk.END)
        salary_entry.insert(0, values[3])
        department_entry.delete(0, tk.END)
        department_entry.insert(0, values[4])
        hire_date_entry.delete(0, tk.END)
        hire_date_entry.insert(0, values[5])
        gender_var.set(values[6])
        status_entry.delete(0, tk.END)
        status_entry.insert(0, values[7])

def update_employee(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry, tree):
    if selected_id is None:
        messagebox.showerror('Error', 'Please select an employee to update')
        return
    
    new_name = name_entry.get()
    new_role = role_entry.get()
    new_salary = salary_entry.get()
    new_department = department_entry.get()
    new_hire_date = hire_date_entry.get()
    new_gender = gender_var.get()
    new_status = status_entry.get()
    
    if not (new_name and new_role and new_salary and new_department and new_hire_date and new_gender and new_status):
        messagebox.showerror('Error', 'All fields are required')
        return
    
    try:
        salary = float(new_salary)
        if salary < 0:
            messagebox.showerror('Error', 'Salary must be a positive number')
            return
    except ValueError:
        messagebox.showerror('Error', 'Salary must be a number')
        return
    
    try:
        datetime.strptime(new_hire_date, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror('Error', 'Hire Date must be in the format YYYY-MM-DD')
        return
    
    if new_name.isdigit() or new_role.isdigit() or new_department.isdigit() or new_status.isdigit():
        messagebox.showerror('Error', 'Name, Role, Department, and Status must contain letters')
        return
    
    db_handler.update_employee_record(selected_id, new_name, new_role, new_salary, new_department, new_hire_date, new_gender, new_status)
    add_to_treeview(tree)
    messagebox.showinfo('Success', 'Employee updated successfully')

def delete_employee(tree, name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry):
    if selected_id is None:
        messagebox.showerror('Error', 'Please select an employee to delete')
        return
    confirmation = messagebox.askyesno('Delete Employee', f'Are you sure you want to delete this employee with ID {selected_id}?')
    if confirmation:
        db_handler.remove_employee(selected_id)
        add_to_treeview(tree)
        clear_fields(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry)
        messagebox.showinfo('Success', 'Employee deleted successfully')

def reset_application(tree, name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry):
    confirmation = messagebox.askyesno('Reset Application', 'Are you sure you want to reset the application? This will delete all employees.')
    if confirmation:
        db_handler.delete_all_employees()
        add_to_treeview(tree)
        clear_fields(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry)
        messagebox.showinfo('Success', 'Application has been reset successfully')