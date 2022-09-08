import pyfiglet
import qrcode
file = open('E://hdd/my websayt/python/t6/test.txt', 'r')
data = file.read()
product_list = data.split('\n')
products = []
for i in range(len(product_list)):
    product_list_info = product_list[i].split(',')
    mydict = {'id': product_list_info[0],
    'name': product_list_info[1],
    'price': product_list_info[2],
    'count': product_list_info[3] }
    products.append(mydict)
def menu():
    print('1 for add product')
    print('2 for edit product')
    print('3 for delete product')
    print('4 for search product')
    print('5 for show list productes')
    print('6 for buy product')
    print('7 for Qr code of product')
    print('8 for exit')
def loading():
    result = pyfiglet.figlet_format('MY STORE', font = 'roman')
    print(result)
def add():
    f=open('E://hdd/my websayt/python/t6/test.txt','a')
    b=input()
    f.write('\n')
    f.write(b)
    f.close()
def edit():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
            c=int(input('id ? : '))
            n=int(input('name ? : '))
            p=int(input('price ? : '))
            k=int(input('count ? : '))
            products[i]['id']==c and products[i]['name']==n and products[i]['price']==p and products[i]['count']==k
            print('Done')
            break
    else:
        print('Does not exist')
def delete():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
            products.remove(i)
            print('Done')
            break
    else:
        print('Does not exist')
def search():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
            print(products[i])
            break
    else:
        print('Does not exist')
def show():
    for i in range(len(products)):
        print(products[i])
def Qr():
    na=input('name or id of product ? : ')
    for i in range(len(products)):
        if products[i]['name'] == na or str(products[i]['id'] )== na:
          qr=qrcode.make(products[i])
          qr.save(f'qrcode{i}.png')
          print('Done')
def buy():
    pri=[]
    while True:
        na=input('name or id of product ? : ( stop Stop to see the total price )')
        for i in range(len(product_list)):
            if products[i]['name'] == na or str(products[i]['id'] )== na:
                cou=int(input('count ? : '))
                if int(products[i]['count'])>=cou:
                    pri.append({'name':products[i]['name'],
                            'price':products[i]['price'],
                            'count':cou})        
                else:
                    print('The number of products is not enough')
                s=int(input('Do you still want to buy something? : (1 for yes 2 for no)'))
                if s==2:
                    break
        else:
            print('Does not exist')
        print(pri)
        tpri=0
        for j in range(len(pri)):
            tpri+=pri[i]['price']*pri[i]['count']
        print("total price : ", tpri)
        break
loading()
while True:
    menu()
    a=int(input())
    if   a<2:
        add()
    elif a==2:
        edit()
    elif a==3:
        delete()
    elif a==4:
        search()
    elif a==5:
        show()
    elif a==6:
        buy()
    elif a==7:
        Qr()
    elif a==8:
        exit()