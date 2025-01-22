import customtkinter
from tkinter import ttk
import tkinter as tk
from handlers import *

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

main_window = customtkinter.CTk()
main_window.title('Employee Management System')
main_window.geometry('1400x600')
main_window.resizable(True, True)

header_font = ('Arial', 24, 'bold')
label_font = ('Arial', 16)
entry_font = ('Arial', 14)
button_font = ('Arial', 14)

input_frame = customtkinter.CTkFrame(main_window)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

main_title = customtkinter.CTkLabel(input_frame, text='Employee Management System', font=header_font)
main_title.grid(row=0, column=0, columnspan=2, pady=10)

name_label = customtkinter.CTkLabel(input_frame, text='Name:', font=label_font)
name_label.grid(row=1, column=0, padx=10, sticky='e')
name_entry = customtkinter.CTkEntry(input_frame, font=entry_font, width=200)
name_entry.grid(row=1, column=1, padx=10, pady=5)

role_label = customtkinter.CTkLabel(input_frame, text='Role:', font=label_font)
role_label.grid(row=2, column=0, padx=10, sticky='e')
role_entry = customtkinter.CTkEntry(input_frame, font=entry_font, width=200)
role_entry.grid(row=2, column=1, padx=10, pady=5)

salary_label = customtkinter.CTkLabel(input_frame, text='Salary:', font=label_font)
salary_label.grid(row=3, column=0, padx=10, sticky='e')
salary_entry = customtkinter.CTkEntry(input_frame, font=entry_font, width=200)
salary_entry.grid(row=3, column=1, padx=10, pady=5)

department_label = customtkinter.CTkLabel(input_frame, text='Department:', font=label_font)
department_label.grid(row=4, column=0, padx=10, sticky='e')
department_entry = customtkinter.CTkEntry(input_frame, font=entry_font, width=200)
department_entry.grid(row=4, column=1, padx=10, pady=5)

hire_date_label = customtkinter.CTkLabel(input_frame, text='Hire Date:', font=label_font)
hire_date_label.grid(row=5, column=0, padx=10, sticky='e')
hire_date_entry = customtkinter.CTkEntry(input_frame, font=entry_font, width=200)
hire_date_entry.grid(row=5, column=1, padx=10, pady=5)

gender_label = customtkinter.CTkLabel(input_frame, text='Gender:', font=label_font)
gender_label.grid(row=6, column=0, padx=10, sticky='e')
gender_options = ['Male', 'Female']
gender_var = customtkinter.StringVar()
gender_dropdown = customtkinter.CTkComboBox(input_frame, values=gender_options, variable=gender_var, font=entry_font, width=200)
gender_dropdown.set('Male')
gender_dropdown.grid(row=6, column=1, padx=10, pady=5)

status_label = customtkinter.CTkLabel(input_frame, text='Status:', font=label_font)
status_label.grid(row=7, column=0, padx=10, sticky='e')
status_entry = customtkinter.CTkEntry(input_frame, font=entry_font, width=200)
status_entry.grid(row=7, column=1, padx=10, pady=5)

button_frame = customtkinter.CTkFrame(input_frame)
button_frame.grid(row=8, column=0, columnspan=2, pady=10)

add_button = customtkinter.CTkButton(button_frame, text='Add Employee', font=button_font, width=200, command=lambda: add_employee(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry, tree))
add_button.grid(row=0, column=0, padx=10, pady=5)

new_button = customtkinter.CTkButton(button_frame, text='New Employee', font=button_font, width=200, command=lambda: clear_fields(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry))
new_button.grid(row=0, column=1, padx=10, pady=5)

update_button = customtkinter.CTkButton(button_frame, text='Update Employee', font=button_font, width=200, command=lambda: update_employee(name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry, tree))
update_button.grid(row=1, column=0, padx=10, pady=5)

delete_button = customtkinter.CTkButton(button_frame, text='Delete Employee', font=button_font, width=200, command=lambda: delete_employee(tree, name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry))
delete_button.grid(row=1, column=1, padx=10, pady=5)

reset_button = customtkinter.CTkButton(button_frame, text='Reset Application', font=button_font, width=200, command=lambda: reset_application(tree, name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry))
reset_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

tree_frame = customtkinter.CTkFrame(main_window)
tree_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#2B2B2B", foreground="white", fieldbackground="#2B2B2B", rowheight=25, font=('Arial', 12))
style.map('Treeview', background=[('selected', '#3A7FF6')])

style.configure("Treeview.Heading", background="#2B2B2B", foreground="white", relief="flat", font=('Arial', 12))
style.map("Treeview.Heading", background=[('active', '#535353')])

tree = ttk.Treeview(tree_frame, height=15)
tree['columns'] = ('ID', 'Name', 'Role', 'Salary', 'Department', 'Hire Date', 'Gender', 'Status')
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=100)
tree.column('Name', anchor=tk.CENTER, width=200)
tree.column('Role', anchor=tk.CENTER, width=200)
tree.column('Salary', anchor=tk.CENTER, width=150)
tree.column('Department', anchor=tk.CENTER, width=200)
tree.column('Hire Date', anchor=tk.CENTER, width=150)
tree.column('Gender', anchor=tk.CENTER, width=100)
tree.column('Status', anchor=tk.CENTER, width=200)

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Role', text='Role')
tree.heading('Salary', text='Salary')
tree.heading('Department', text='Department')
tree.heading('Hire Date', text='Hire Date')
tree.heading('Gender', text='Gender')
tree.heading('Status', text='Status')

tree.pack(fill=tk.BOTH, expand=True)
tree.bind('<<TreeviewSelect>>', lambda event: select_employee(event, tree, name_entry, role_entry, salary_entry, department_entry, hire_date_entry, gender_var, status_entry))

main_window.grid_rowconfigure(0, weight=1)
main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=3)

input_frame.grid_rowconfigure(8, weight=1)
input_frame.grid_columnconfigure(1, weight=1)

tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)

add_to_treeview(tree)

main_window.mainloop()