def bill(a,b,c):
    sum=0
    print('''\t\t\t  SARAVANA SUPER MARKET
\t\t\t\t Redhills ch-52''')
    print("*"*63)
    print("NAME\t\tMRP\t\tNO OF PRODUCTS\t\tPRICE")
    for i in range(len(a)):
        print("{}\t\t {}\t\t {}\t\t\t{}".format(str(a[i]),int(b[i]),int(c[i]),int(b[i]*c[i])))
        sum+=b[i]*c[i]
    print("-"*100)
    print("\t\t\t\t\t\t\t Total=",sum)
    print("-"*100)
    print("\t\t\t\t\t\t\tDiscount=",dis,"%")
    print("\t\t\t\t\t\t\tSale price=",sum-((dis/100)*sum))
    print("\t\t\tTHANK YOU")
n=int(input("Enter the total products..."))
product_name=[]
price=[]
no_of_pro=[]
for i in range(n):
    product_name.append(input("Enter the product name:"))
    price.append(int(input("Enter price:")))
    no_of_pro.append(int(input("Enter the no of products:")))
global dis
dis=int(input("Enter discount:"))
bill(product_name,price,no_of_pro)
