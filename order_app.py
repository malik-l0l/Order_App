from tkinter import *

# GLOBAL VAR
# -------------------------

# available items in menu and its price
menu = {
    "Falafel": 20,
    "Ramen": 50,
    "Burger": 50,
    "Pizza": 100,
    "Shawarma": 100,
    "Chicken-65": 200,
}


# END GLOBAL VAR
# -------------------------

# METHODS
# ------------------------------------------------------


def order():
    """
    checks if ordered items are in menu list,
    if yes creates bill for ordered items and shows unavailable items in the placed-order.
    if there is no unavailable items in placed-order,program won't show unavailable items
    :return: None
    """

    # if there is no items order-list -> no bill is created
    if listbox.size() != 0:
        bill = 0
        items_available = {}
        items_unavailable = []

        # turtle checks order-list
        for i in range(listbox.size()):
            # rabbit checks menu_items
            for j in menu.keys():
                # check if ordered_items is in menu
                if listbox.get(i) == j:
                    # bill + item's price
                    bill += menu[j]
                    items_available[j] = menu[j]

        # checks if there is ordered but not in menu items
        for i in range(listbox.size()):
            if listbox.get(i) not in menu.keys():
                items_unavailable.append(listbox.get(i))

        # you can check if it works
        # print(bill)
        # print(items_available)
        # print(items_unavailable)

        # creates a new window for bill
        create_bill(bill, items_available, items_unavailable)


def add(event=None):
    """
    simply add items to the order-list
    when,1) add button is pressed
         2) hit enter after typing
    :param event: None by default(used to handle keyboard event)
    :return:
    """

    # add fn won't work if entry box is null or digits
    if entry_box.get() == "" or entry_box.get().isdigit():
        pass
    else:
        listbox.insert(listbox.size(), entry_box.get().capitalize())
        entry_box.delete(0, END)
        listbox.config(height=listbox.size())


def delete():
    """
    deletes cursor-selected item from list
    :return: None
    """
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


# END METHODS
# ------------------------------------------------------


# WINDOWS
# ----------------------------------------------------------------------------------------
def help_user():
    """
    function that creates a help-window to make user
    aware more about app functionalities.
    :return: None
    """
    help_text = """
List-box :
-------------
shows all your orders

Entry-box :
-------------
helps to enter order to the list  

Buttons :
-------------
menu   : to see available items.
add/Enter : add items to the list.
delete : deletes 'selected' item from list.
order  : shows bill according to bill.
help   : to get help about functionalities.

-- Thanks for using this program :) --
created by malik-l0l
    """
    help_window = Toplevel()
    help_window.title("Help :)")
    help_window.resizable(False, False)  # non-resizable

    Label(help_window, font=("Arial", 16, "bold"), relief=RAISED,
          bd=5, foreground='white', width=38, height=19, background='black',
          text=help_text).pack()

    help_window.mainloop()


def create_bill(bill, items_available, items_unavailable):
    """
    function that creates a window to show items available, bill, items_unavailable
    :param bill: total bill of items from order-list
    :param items_available: items in menu and ordered by user
    :param items_unavailable: items in order-list but not in menu
    :return: None
    """
    bill_window = Toplevel()
    bill_window.title("Bill")
    bill_window.resizable(False, False)  # non-resizable

    frame_1 = Frame(bill_window)
    frame_1.pack()

    frame_2 = Frame(bill_window)
    frame_2.pack()

    # items ordered
    for i in range(len(items_available.keys())):
        # item   $price
        item = list(items_available.keys())[i]
        price = list(items_available.values())[i]
        Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED,
              bd=5, foreground='black', width=10, background='pink', text=f"{item}").grid(row=i, column=0)
        Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED,
              bd=5, foreground='black', width=10, background='pink', text=f"+ ${price}").grid(row=i, column=1)

    index_after_available = len(items_available.keys()) + 1
    # BILL ->
    Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED,
          bd=5, foreground='black', width=10, background='grey', text="Bill").grid(row=index_after_available, column=0,
                                                                                   pady=5)
    Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED,
          bd=5, foreground='black', width=10, background='grey', text=f"${bill}").grid(row=index_after_available,
                                                                                       column=1, pady=5)

    # shows only if there is unavailable_items are in order_list
    # unavailable items are items in order-list but not in menu
    if len(items_unavailable) != 0:

        Label(bill_window, font=("Arial", 18, "bold"), relief=RAISED,
              bd=5, foreground='black', width=21, background='#82bf8b',
              text="Unavailable items :", justify="left", underline=True).pack()

        for i in range(len(items_unavailable)):
            Label(bill_window, font=("Arial", 18, "bold"), relief=RAISED,
                  bd=5, foreground='black', width=21, background='#82bf8b',
                  text=f"{items_unavailable[i]}").pack(side=BOTTOM)

    bill_window.mainloop()


def create_menu():
    """
    function that creates a window to show all available items and its price.
    :return: None
    """
    menu_window = Toplevel()
    menu_window.title("Menu")
    menu_window.resizable(False, False)

    frame_1 = Frame(menu_window)
    frame_1.pack()

    frame_2 = Frame(menu_window)
    frame_2.pack()

    Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED, underline=True,
          bd=5, foreground='black', width=10, background='grey', text="Item").pack(side=LEFT)
    Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED, underline=True,
          bd=5, foreground='black', width=10, background='grey', text="Price").pack(side=RIGHT)

    for i in range(len(menu.keys())):
        item = list(menu.keys())[i]
        price = list(menu.values())[i]
        Label(frame_2, font=("Arial", 18, "bold"), relief=RAISED,
              bd=5, foreground='black', width=10, background='pink', text=f"{item}").grid(row=i, column=0)
        Label(frame_2, font=("Arial", 18, "bold"), relief=RAISED,
              bd=5, foreground='black', width=10, background='pink', text=f" ${price}").grid(row=i, column=1)
    menu_window.mainloop()


# MAIN WINDOW
# ======================================================
window = Tk()
window.title("Order App")
window.resizable(False, False)
window.config(background="#f7ffde")

listbox = Listbox(window,
                  font=("Constantia", 30, "bold"),
                  bg="#f7ffde",
                  fg='#e45c5c',
                  # width=12
                  selectmode=MULTIPLE)
listbox.pack()

listbox.config(height=listbox.size())  # Adjusts the Size

# let's create an Entry box to append to the listbox
entry_box = Entry(window, width=31, font=("Arial", 20), )
entry_box.pack()

frame = Frame(window, bg="#f7ffde", bd=5, relief=SUNKEN)
frame.pack(side=TOP)

menu_button = Button(frame, text="menu", command=create_menu, relief=RAISED, bd=5, padx=10, bg='#84bd85',
                     font=("Arial", 9, "bold italic"))
menu_button.pack(side=LEFT)

add_button = Button(frame, text="add", command=add, relief=RAISED, bd=5, padx=20, bg='#84bd85',
                    font=("Arial", 9, "bold italic"))
add_button.pack(side=LEFT)
# When hit enter, items are added into order-list
window.bind('<Return>', add)

delete_button = Button(frame, text="delete", command=delete, relief=RAISED, bd=5, padx=10, bg='#84bd85',
                       font=("Arial", 9, "bold italic"))
delete_button.pack(side=LEFT)

order_button = Button(frame, text="order", command=order, relief=RAISED, bd=5, padx=10, bg='#84bd85',
                      font=("Arial", 9, "bold italic"))
order_button.pack(side=LEFT)

help_button = Button(frame, text="help", command=help_user, relief=RAISED, bd=5, padx=10, bg='#84bd85',
                     font=("Arial", 9, "bold italic"))
help_button.pack(side=LEFT)

window.mainloop()

# END MAIN WINDOW
# ======================================================
# END WINDOWS
# ----------------------------------------------------------------------------------------
