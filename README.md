# Employee Management System  
This is a Python-based app built with `customtkinter` and `tkinter` to make managing employee data quick and hassle-free. You can add, view, update, and delete employee records easily, thanks to an interactive table powered by `ttk.Treeview`. The whole thing is structured using Object-Oriented Programming (OOP), keeping the code clean and easy to maintain. Event handling is in place to ensure smooth user interaction, and the dark-themed UI, styled with `ttk.Style`, gives it a modern touch.  

---
<img width="1046" alt="{05235E51-621F-4683-93A8-F8D3BC80CDA5}" src="https://github.com/user-attachments/assets/9185df02-57de-4cd8-b2ea-6da7b147cc0d" />

---
Now, let’s dive into the details of how the app works and how I handled common user mistakes. When entering data, users might leave fields empty, enter invalid formats (like text in a salary field), or forget to select required options. To prevent these issues, I added input validation and error handling. If something's off, the app gives clear messages instead of crashing. This way, users can quickly fix their input and keep things running smoothly.  

---
If a user starts filling in the fields but forgets or skips one, they’ll get a clear error message reminding them that all fields must be filled. This ensures no incomplete records are saved. The app won’t proceed until everything is properly entered, making sure the data stays clean and accurate. Instead of crashing or allowing bad input, it prompts users to fix mistakes right away.

---
<img width="1049" alt="{9737DAF3-B972-45AE-A17A-4C971AC82151}" src="https://github.com/user-attachments/assets/e0aecd23-8b87-4828-804f-32fd8c3c0eab" />

---
If a user enters incorrect data in a field, the app will show an error message explaining what needs to be fixed. Here’s how validation works for each field:

- **Name:** Must contain only letters. If numbers or special characters are entered, the user will be asked to correct it.  
- **Role:** Cannot be left empty. If skipped, an error message will appear.  
- **Salary:** Must be a number. If a user types text or leaves it blank, they’ll get a warning.  
- **Department:** Required field. The user must enter a valid department name.  
- **Hire Date & Status:** Must be in `YYYY-MM-DD` format. If entered incorrectly, an error will pop up asking for the correct format.  
- **Gender:** The user must select an option from the dropdown. If they try to leave it blank, they’ll be reminded to choose one.  

The app won’t proceed unless all fields are correctly filled out, ensuring clean and accurate data.  

---
<img width="1044" alt="{121BA16D-E172-4A05-A6F7-4FA02EC974E8}" src="https://github.com/user-attachments/assets/3da95876-ced1-4a75-8d61-0ab2f37e20c8" />

---
Need to update an employee’s details? No problem! Whether you’re changing just one field or updating everything, the **Update Employee** button makes it easy.  

For example, if you want to update an employee’s salary:  

1. Click on the employee’s record in the table.  
2. Enter the new salary in the **Salary** field.  
3. Hit the **Update Employee** button.  
4. The app will check if the input is valid before saving.  
5. If there’s a mistake—like typing letters instead of numbers—you’ll see an error message telling you what to fix.  

This works the same way for all fields. The app makes sure everything is entered correctly before saving, so no bad data gets stored.  

---
<img width="1047" alt="{F2F81CF8-D5F9-4DA8-98FB-7AFD719CB4FC}" src="https://github.com/user-attachments/assets/6e50afef-b37a-46d0-8a92-b2019c6e6f28" />
<img width="1046" alt="{0320D241-DD9B-4BA7-9D9B-D487BECF7E02}" src="https://github.com/user-attachments/assets/1bec37fb-a4ce-49dc-a539-98b97a20a89f" />

---
If an employee leaves the company—whether they got a new job, retired, or were let go—you can easily remove their record using the **Delete Employee** button.  

Here’s how it works:  

1. Select the employee from the table.  
2. Click the **Delete Employee** button.  
3. A confirmation message will pop up to make sure you really want to delete the record.  
4. Once confirmed, the employee’s data will be permanently removed.  

This keeps the records clean and up to date, so you’re only managing active employees.  

---
<img width="1044" alt="{B0782A7C-5628-4707-9C26-61DD92CA695B}" src="https://github.com/user-attachments/assets/89f8a4b0-3699-4d5b-9c06-039589d82389" />
<img width="1049" alt="{C68AA3FF-BA60-4045-898A-8D22C17192F9}" src="https://github.com/user-attachments/assets/8c7bffa6-e765-4599-b189-8c37edbc9556" />

---
Need to wipe all employee data and start fresh? Just hit the **Reset Application** button.  

Here’s what happens:  

1. Click **Reset Application**.  
2. A message pops up asking if you're sure.  
3. If you confirm, all employee records get deleted for good.  
4. The app refreshes, leaving you with a clean slate.  

This is great if you want to clear everything at once instead of deleting records one by one. Just a heads-up—once you reset, there’s no undo!  

---
<img width="1044" alt="{C567C54D-6F86-4594-94E3-842D1C5973B9}" src="https://github.com/user-attachments/assets/35ea2194-6813-46ad-9218-1d313bfa6f6d" />
<img width="1046" alt="{A0E036CC-5BD7-442A-ABAC-75D0F37F6997}" src="https://github.com/user-attachments/assets/8853ddb8-630c-4dcf-906e-c805acae1a1d" />

---
***Thanks for making it this far! I’d love for you to stay tuned and check out my future updates. I’ll be adding new features soon, like searching for employees by name or ID and exporting data to an Excel sheet.***

***So, keep an eye out for updates! And if you’ve got any feedback, I’d really appreciate it.***




