print("Pick your favourite product to Cart and then to home ,  great discounts are awaiting"  "\n" "Product A :$20" "\n" "Product B :$40" "\n" "Product C :$50")
print("Discount :")
print("flat_10_discount : If cart total exceeds $200, apply a flat $10 discount on the cart total.")
print("bulk_5_discount: If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price. ")
print("10 % discount on total quantity of products more than 20 units ")
print("tiered_50_discount: If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantities have the original price and units above 15 will get a 50% discount.")
print("Note:" "\n" "Gift wrap fee will be $1 per unit." "\n" " Shipping fee will be  10 units can be packed in one package, and the shipping fee for each package is $5.")

cartA={}
cartB={}
cartC={}
shippingfee=0
carttotal=0
total_quantity=0

pro1=input("would you like to purchase product A ?" "\n")
if pro1=="yes":
    pro1quantity=int(input("enter the quantity of the product A" "\n"))
    cartA['Product A']=pro1quantity
    subtotal=pro1quantity*20
    print("subtotal of the product A is",subtotal)
    giftwrap=input("would you like to gift wrap the product ?""Note: Special Charges are included $1 per unit" "\n")  
    
    if giftwrap=="yes":
      wrapfee=pro1quantity*1
      print("gift wrapping fee for product A is",wrapfee)

    else:
      wrapfee=0
      print("gift wrapping fee for product A is",wrapfee)
    

    shippingfee=pro1quantity//10*5 
    print("shipping fee for product A is",shippingfee) 

    pro1total=20*pro1quantity+wrapfee+shippingfee
    print(" product name  and Quantity is",cartA," and total price of product A is",pro1total)
    

pro2=input("would you like to purchase product B  ?" "\n")
if pro2=="yes":
    pro2quantity=int(input("enter the quantity of the product B" "\n"))
    cartB['Product B']=pro2quantity
    subtotal=pro2quantity*40
    print("subtotal of the product B is",subtotal)
    giftwrap=input("would you like to gift wrap the product ?""Note: Special Charges are included $1 per unit" "\n")  
    
    if giftwrap=="yes":
     wrapfee=pro2quantity*1
     print("gift wrapping fee for product B is",wrapfee)

    else:
       wrapfee=0
       print("gift wrapping fee for product B is",wrapfee)
    
    shippingfee=pro2quantity//10*5 
    print("shipping fee for product B is",shippingfee) 

    pro2total=40*pro2quantity+wrapfee+shippingfee
    print(" product name  and Quantity is",cartB," and total price of product B is",pro2total)       


pro3=input("would you like to purchase product C ?" "\n")
if pro3=="yes":
    pro3quantity=int(input("enter the quantity of the product C" "\n"))
    cartC['Product C']=pro3quantity 
    subtotal=pro3quantity*50
    print("subtotal of the product C is",subtotal)
    giftwrap=input("would you like to gift wrap the product ?""Note: Special Charges are included $1 per unit""\n")  

    if giftwrap=="yes":
      wrapfee=pro3quantity*1
      print("gift wrapping fee for product C is",wrapfee)

    else:
      wrapfee=0
      print("gift wrapping fee for product C is",wrapfee)
    
    shippingfee=pro3quantity//10*5 
    print("shipping fee for product C is",shippingfee) 

    pro3total=50*pro3quantity+wrapfee+shippingfee
    print(" product  and Quantity is",cartC," and total price  of Product C is",pro3total)       
    
carttotal=pro1total+pro2total+pro3total
print("your cart total price is ",carttotal)

total_quantity=pro1quantity+pro2quantity+pro3quantity
cart={}
cart['product A']=pro1quantity
cart['product B']=pro2quantity
cart['product C']=pro3quantity

products={"product A":20,"product B":40,"product C":50}


if carttotal>200:
   discount_name="flat_10_discount"
   discount_amount=10
   discount_cart=carttotal-discount_amount
   print("total amount after discount",discount_cart,"discount name applied is",discount_name)


elif  pro1quantity>10:
   discount_name="bulk_5_discount"
   discount_percentage=0.05
   discount_amount=pro1quantity*20*discount_percentage
   discount_total_price=pro1quantity*20-discount_amount
   print("total amount after discount",discount_total_price,"discount name applied is",discount_name)  

elif  pro2quantity>10:
   discount_name="bulk_5_discount"
   discount_percentage=0.05
   discount_amount=pro2quantity*40*discount_percentage
   discount_total_price=pro2quantity*40-discount_amount
   print("total amount after discount",discount_total_price,"discount name applied is",discount_name) 

elif  pro3quantity>10:
   discount_name="bulk_5_discount"
   discount_percentage=0.05
   discount_amount=pro3quantity*50*discount_percentage
   discount_total_price=pro3quantity*50-discount_amount
   print("total amount after discount",discount_total_price,"discount name applied is",discount_name)      

elif total_quantity>20:
   discount_name="bulk_10_discount"
   discount_percentage=0.1
   discount_amount=carttotal*discount_percentage
   discount_total_price=carttotal-discount_amount
   print("total amount after discount",discount_total_price,"discount name applied is",discount_name) 


elif total_quantity>30:
   for product,quantity in cart.items():
      original_price=products.get(product)
      if quantity>15:
          discount_name="tiered_50_discount"
          discount_percentage=0.5
          discounted_quantity = quantity - 15
          discounted_price=0.5*original_price
          discount_total_price=15*original_price+discounted_quantity*discounted_price    
          print("total amount after discount",discount_total_price,"discount name applied is",discount_name) 
else:
   print("no discounts are applied")          
            
      
      