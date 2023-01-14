import tkinter as tk
import mysql.connector

def create_login():
    # create a new window for the login screen
    login_window = tk.Toplevel(root)

    # create labels for the username and password fields
    tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)

    # create entry fields for the username and password
    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")

    # place the entry fields on the grid
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # create a login button
    login_button = tk.Button(login_window, text="Login", command=lambda: check_login(username_entry.get(), password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def check_login(username, password):
    # connect to the MySQL database
    conn = mysql.connector.connect(
        host="hostname",
        user="username",
        password="password",
        database="database_name"
    )

    # create a cursor object
    cursor = conn.cursor()

    # execute the SELECT statement to check if the entered username and password match any records in the database
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))

    # fetch the results of the SELECT statement
    results = cursor.fetchone()

    # if there are no matches, display an error message
    if not results:
        tk.messagebox.showerror("Error", "Invalid username or password.")

    # if there is a match, close the login window and open the main window for the hostel management system
    else:
        login_window.destroy()
        create_main_window()

def create_main_window():
    # code for creating the main window for the hostel management system goes here
    pass

root = tk.Tk()
create_login()
root.mainloop()
