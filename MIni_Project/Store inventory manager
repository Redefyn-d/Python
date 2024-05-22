from tkinter import *
def add_elements():
    prd_name = prd_var_name.get()
    prd_qty = prd_var_qty.get()
    prd_buy_price = prd_var_buy_price.get()
    prd_sell_price = prd_var_sell_price.get()
    item_data[prd_name] = [prd_qty, prd_buy_price, prd_sell_price]
    # sql = "INSERT INTO products (name, quantity, buy_price, sell_price) VALUES (%s, %s, %s, %s)"
    # values = (prd_name, prd_qty, prd_buy_price, prd_sell_price)
    # cursor.execute(sql, values)
    # db.commit()

def display_items():
    display_text.delete('1.0', END) 
    for name, details in item_data.items():
        display_text.insert(END, f"Product Name: {name}\n")
        display_text.insert(END, f"Quantity: {details[0]}\n")
        display_text.insert(END, f"Buy Price: {details[1]}\n")
        display_text.insert(END, f"Sell Price: {details[2]}\n\n")

def check_prd():
    find_name = find_var_name.get()
    display_text.delete('1.0', END)
    for name, details in item_data.items():
        if name == find_name:
            if details[0] != 0:
                display_text.insert(END, f"The product is available and {details[0]} are left\n")
            else:
                display_text.insert(END, f"The product you are looking for is out of stock\n")
            break
    else:
        display_text.insert(END, f"No such product found\n")

def change_value():
    global item_data
    new_quantity=new_var_quantity.get()
    find_prd_name=find_var_prd_name.get()
    for name, details in item_data.items():
        if(name==find_prd_name):
            item_data[name][0]=new_quantity

s = Tk()
s.title("Inventory Management System")
s.geometry("800x600")
s.configure(bg="#FF9F66") 

# Styles
font_bold = ("Arial", 12, "bold")
font_normal = ("Arial", 12)
font_large = ("Arial", 16, "bold")

# Labels
Label(s, text="Add Items", font=font_large, bg="#FF9F66").grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)
Label(s, text="Name:", font=font_bold, bg="#FF9F66").grid(row=1, column=0, padx=10, pady=5, sticky=W)
Label(s, text="Quantity:", font=font_bold, bg="#FF9F66").grid(row=2, column=0, padx=10, pady=5, sticky=W)
Label(s, text="Buy Price:", font=font_bold, bg="#FF9F66").grid(row=3, column=0, padx=10, pady=5, sticky=W)
Label(s, text="Sell Price:", font=font_bold, bg="#FF9F66").grid(row=4, column=0, padx=10, pady=5, sticky=W)
Label(s, text="Display Items", font=font_large, bg="#FF9F66").grid(row=0, column=2, padx=10, pady=10, sticky=W)
Label(s, text="Find Product:", font=font_bold, bg="#FF9F66").grid(row=8, column=2, padx=10, pady=5, sticky=W)
Label(s, text="Change In the Values:", font=font_bold, bg="#FF9F66").grid(row=6, column=0, padx=10, pady=5, sticky=W)

# Entries
prd_var_name = StringVar()
prd_var_qty = IntVar()
prd_var_buy_price = IntVar()
prd_var_sell_price = IntVar()
find_var_name = StringVar()
new_var_quantity= IntVar()
find_var_prd_name= StringVar()
Entry(s, textvariable=prd_var_name, width=30, font=font_normal).grid(row=1, column=1, padx=10, pady=5, sticky=W)
Entry(s, textvariable=prd_var_qty, width=30, font=font_normal).grid(row=2, column=1, padx=10, pady=5, sticky=W)
Entry(s, textvariable=prd_var_buy_price, width=30, font=font_normal).grid(row=3, column=1, padx=10, pady=5, sticky=W)
Entry(s, textvariable=prd_var_sell_price, width=30, font=font_normal).grid(row=4, column=1, padx=10, pady=5, sticky=W)
Entry(s, textvariable=find_var_name, width=30, font=font_normal).grid(row=9, column=2, padx=10, pady=5, sticky=W)
Entry(s, textvariable=find_var_prd_name, width=30, font=font_normal).grid(row=7, column=0, padx=10, pady=5, sticky=W)
Entry(s, textvariable=new_var_quantity, width=30, font=font_normal).grid(row=8, column=0, padx=10, pady=5, sticky=W)


# Buttons
Button(s, text="ADD ITEM", command=add_elements, width=20, font=font_bold).grid(row=5, column=0, padx=10, pady=5, sticky=W)
Button(s, text="DISPLAY ITEMS", command=display_items, width=20, font=font_bold).grid(row=7, column=2, padx=10, pady=5, sticky=W)
Button(s, text="CHECK PRODUCT", command=check_prd, width=20, font=font_bold).grid(row=10, column=2, padx=10, pady=5, sticky=W)
Button(s, text="CHANGE QUANTITY", command=change_value, width=20, font=font_bold).grid(row=10, column=0, padx=10, pady=5, sticky=W)

# Text widget
display_text = Text(s, width=60, height=20)
display_text.grid(row=1, column=2, rowspan=6, padx=10, pady=10, sticky=W)

s.mainloop()
