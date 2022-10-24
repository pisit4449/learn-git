import sqlite3

conn = sqlite3.connect('productdb.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                name TEXT,
                price REAL,
                image TEXT) """)

# ========  บันทึกข้อมูลสินค้าเก็บไว้ในตาราง Product =============================================
def Insert_Product(productid,name,price,image):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)' # จำนวนเเท่ากับ ตัวแปร บวก ID
        c.execute(command,(None,productid,name,price,image))
    conn.commit()  # save database
    print('saved')
    # add status after insert product
    # find = View_product_single(productid)
    # insert_product_status(find[0],'show')
# ========  แสดงสินค้าทั้งหมดใน Product ======================================================
def View_product():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        result = c.fetchall()
    return result

def Product_List():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        product = c.fetchall()

    result = []

    for p in product:
        result.append(p)

    result_dict = {}
    for r in result:
        result_dict[r[0]] = {'id':r[0],'productid':r[1],'name':r[2],'price':r[3]}

    return result_dict
    


if __name__=='__main__':
    Product_List()
    # Insert_product('CF-1002','espresso',45,r'c:\Images\espresso.png')
    # View_product()
    # View_product_table_icon()
    # insert_product_status(1,'show')
    # print(View_product_status(1))
    # x=product_icon_list()
    # print(x)
