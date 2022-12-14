# =========== Up git ==============================================
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/pisit4449/CoffeeManager.git
# git push -u origin main
#==================================================================
from tkinter import *
from tkinter import ttk, messagebox
from menufunction import *

addproduct = AddProduct()

# ==============================================================================================
root = Tk()
root.title("โปรแกรมร้านกาแฟ Pupea Coffee")
root.iconbitmap('images/dog.ico')
root.geometry("1200x650+100+10")
root.state('zoomed')

# ========== Main Menu Bar ==========================================================================
menubar = Menu(root)
root.config(menu=menubar)
# ========== Menu ย่อย ==========================================================================
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Exit", font = 10,background='white', activebackground='red', command=lambda : root.destroy())  #  ออกจากโปรแกรม

productmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='สินค้า', menu=productmenu)
productmenu.add_cascade(label='เพิ่มสินค้า', font = 10, command=addproduct.command)
productmenu.add_cascade(label='สต๊อคสินค้า', font = 10)

membermenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='สมาชิก', menu=membermenu)
membermenu.add_cascade(label='เพิ่มสมาชิก', font = 10)

salespersonmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='พนักงาน', menu=salespersonmenu)
salespersonmenu.add_cascade(label='เพิ่มพนักงาน', font = 10)
# ==============================================================================================
# ========== Tabs =============================================================================
Tab = ttk.Notebook(root)
Tab.pack(fill=BOTH,expand=1)

Tab_Main = ttk.Frame(Tab)
Tab_Order = ttk.Frame(Tab)

icon_tab = PhotoImage(file='images/tab.png')

Tab.add(Tab_Main, text='Main Sale Coffee',image=icon_tab,compound='left')
Tab.add(Tab_Order, text='Order List',image=icon_tab,compound='left')
# Set Font

# ==============================================================================================
# ========== Frame =============================================================================
SearchFrame = Frame(Tab_Main)
SearchFrame.place(x=50,y=20)

Main_button_Frame = Frame(Tab_Main)
Main_button_Frame.place(x=50,y=80)
# ==============================================================================================
# ========== ช่อง SEACH สินค้า  ===================================================================
v_search = StringVar()
ESearch = Entry(SearchFrame, textvariable=v_search, width=20, font=(None, 20)).grid(row=0,column=0)
L = Label(SearchFrame, text="ค้นหาสินค้า", font=(None, 20)).grid(row=0, column=1, padx=10)
# ==============================================================================================
# ========== ปุ่มเพิ่มสินค้าในการขาย  ==============================ช=================================
allorder = {}
product = Product_List() # product = product_icon_list()
# {1: {'id': 1, 'productid': 'A-1001', 'name': 'espresso', 'price': 50.0}

# ใส่ค่าการสั่งซื้อเข้าไปใน  allmenu
def AddMenu(name = 'espresso'):
    if name not in allorder:
        allorder[name] = [product[name]['id'],product[name]['name'],product[name]['price'], 1, product[name]['price']]
    else:
        quan = allorder[name][2] + 1
        total = product[name]['price'] * quan
        allorder[name] = [product[name]['id'],product[name]['name'],product[name]['price'], quan, total]

    # ALLMENU =========>  {'espresso': ['espresso', 40, 2, 80], 'latte': ['latte', 50, 2, 100]}
# ========== สร้างปุ่มเพิ่มสินค้าในการขาย  ==============================ช=================================
# button_dict = {}
icon_button = PhotoImage(file='images/dog-icon.png')
row = 0
column = 0
column_quan = 4
for k,p in product.items():
    if column == column_quan:
        column = 0
        row += 1

    B = Button(Main_button_Frame,text=p['name'],font=(None, 10),image=icon_button,compound='top')
    B.config(command=lambda m = k : AddMenu(m))
    # B.config(image=new_icon)
    B.grid(row=row,column=column,ipadx=40,ipady=10)
    

    column += 1
# ==============================================================================================

root.mainloop()