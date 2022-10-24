from tkinter import *
from tkinter import ttk, messagebox, filedialog
from productdb import *

class AddProduct:

    def __init__(self):
        self.rootAP = None
        self.v_productid = None
        self.v_name = None
        self.v_price = None
        self.v_imagepath = None
        self.Bsave = None
        self.Bedit = None
        self.Badd = None
        self.ProductImage = None
        self.table_product = None

    def popup(self):
        self.rootAP = Toplevel()
        self.rootAP.geometry('1060x750')
        self.rootAP.iconbitmap('images/dog.ico')
        self.rootAP.title('Add Product')

        self.v_productid = StringVar()
        self.v_name = StringVar()
        self.v_price = StringVar()
        self.v_imagepath = StringVar()

        Frame_AP = Frame(self.rootAP, width=700)
        Frame_AP.place(x=50, y=20)

        Frame_TP = Frame(self.rootAP)
        Frame_TP.place(x=600, y=50)

        L = Label(Frame_AP,text=" " * 50,font=(None,30)).pack()
        L = Label(Frame_AP,text="Add Product",font=(None,30))
        L.pack(pady=20)

        L = Label(Frame_AP,text="Product Code",font=(None,20)).pack()
        E1 = ttk.Entry(Frame_AP,textvariable=self.v_productid,font=(None,20))
        E1.pack(pady=10)

        L = Label(Frame_AP,text="Product Name",font=(None,20)).pack()
        E2 = ttk.Entry(Frame_AP,textvariable=self.v_name,font=(None,20))
        E2.pack(pady=10)

        L = Label(Frame_AP,text="Product Price",font=(None,20)).pack()
        E3 = ttk.Entry(Frame_AP,textvariable=self.v_price,font=(None,20))
        E3.pack(pady=2)

        img = PhotoImage(file='images/dog-icon.png')
        self.ProductImage = Label(Frame_AP,textvariable=self.v_imagepath, image=img, compound='top')
        self.ProductImage.pack()

        self.v_imagepath.set('C:/Users/Asus/Desktop/ProgramCoffeeShop/images/dog-icon.png')

        Bselect = ttk.Button(Frame_AP,text="Image(50x50 px)",command=self.SelectFile)
        Bselect.pack(pady=2)

        self.Bsave = ttk.Button(Frame_AP,text="Save", command=self.SaveProduct)
        self.Bsave.pack(pady=2,ipadx=20,ipady=10)

        self.Bedit = ttk.Button(Frame_AP,text="Edit")  # ,command=self.update_product_to_database
        self.Bedit.pack(pady=2,ipadx=20,ipady=10)
        self.Bedit.pack_forget()  #  ซ่อนไว้ตอนเริ่มต้น

        self.Badd = ttk.Button(Frame_AP,text="New")  # ,command=self.add_button
        self.Badd.pack(pady=2,ipadx=20,ipady=10)

        # =============== Table Order ======================================================
        header = ['ID','ProductID','Prodcut Name', 'Price']
        h_width = [50,100,150,100]

        self.table_product = ttk.Treeview(Frame_TP,columns=header,show='headings',height=25)
        self.table_product.pack()

        for hd,hw in zip(header,h_width):
            self.table_product.heading(hd,text=hd)
            self.table_product.column(hd,width=hw)

        self.Insert_Table()
        # self.table_product.bind('<Double-1>', self.update_product) # ดัลเบิ้ลคลิก
        self.table_product.bind('<Delete>',self.delete_product_database)



        self.rootAP.mainloop()

    def SelectFile(self):
        filetypes = (
            ('PNG','*.png'),
            ('All files','*.*')
        )
        import os
        DIR = os.getcwd()  # ตำแหน่งโฟลเดอร์ของโปรแกรม

        select = filedialog.askopenfilename(title='Select Image',initialdir=DIR,filetypes=filetypes)
        img = PhotoImage(file=select)
        self.ProductImage.configure(image=img)
        self.ProductImage.image = img
        self.v_imagepath.set(select)
        self.rootAP.focus_force()  # ทำให้วินโด อยู่ด้านบน
        self.rootAP.grab_set()
        
    def SaveProduct(self):
        v1 = self.v_productid.get()
        v2 = self.v_name.get()
        v3 = float(self.v_price.get())
        v4 = self.v_imagepath.get()
        Insert_Product(v1,v2,v3,v4)

        self.v_productid.set('')
        self.v_name.set('')
        self.v_price.set('')
        self.v_imagepath.set('')

        View_product()
        # self.clearbutton()
        # self.create_button()
        self.Insert_Table()
        
    def Insert_Table(self):
        self.table_product.delete(*self.table_product.get_children())
        data = View_product()
        for d in data:
            row = list(d) # convert tuple to list
            self.table_product.insert('',END, value=row[:4])


    def command(self):
        self.popup()


if __name__=='__main__':
    AddProduct()
    # Insert_Product()
