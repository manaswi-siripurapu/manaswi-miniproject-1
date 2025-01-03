import random

menu = {
    '100': {
        # beverages
        "signature cold coffee": 150,
        "cappuccino": 210,
        "espresso": 180,
        "filter coffee": 120,
        "cafe latte": 190,
        "iced tea": 140,
        "matcha latte": 200,
        "americano": 230,
        "macchiato": 210
    },
    '200': {
        # SANDWICHES AND WRAPS
        "Spicy tuna": 200,
        "Bacon and cheese": 260,
        "Club grill sandwich": 230,
        "Pesto wrap": 270,
        "Chicken Caesar": 310,
        "Veggie wrap": 190,
        "Salsa chaap wrap": 200,
        "American Mustard Mix Veg": 240
    },
    '300': {
        # MOCKTAILS AND SHAKES
        "Vergin cucumber Gimblet": 120,
        "White lady": 140,
        "Citrus fizz": 120,
        "Dry Cranberry Spitzer": 170,
        "Shirley ginger": 150,
        "Blue almond delight": 160,
        "Omega berry blast": 200,
        "Vanilla verve": 150,
        "Strawberry Spin": 140,
        "Cocoa delight": 220
    },
    '400': {
        # DESSERTS
        "Hot brownie": 220,
        "Nuttella cheese cake": 280,
        "Galata cheese cake": 300,
        "Signature Thiramisu": 250,
        "Sizzling brownie": 250,
        "Rasmalai Tres leches": 300,
        "Lychee Sundae": 230,
        "Red velvet choco sin Sundae": 260,
        "Hot chocolate fudge": 200
    },
    '500': {
        # APPETIZERS
        "BBQ Paneer skewers": 320,
        "Butter garlic prawn": 380,
        "Cheese garlic bread": 250,
        "Cheesy Jalapeno corn bomb": 290,
        "Chipotle fries": 190,
        "Crunchy Taco Supreme": 250,
        "Mexican Taco": 280,
        "Spicy pesto skewers": 320,
        "Barbeque wings": 330
    },
    '600': {
        # PIZZA AND PASTAS
        "Alfredo pasta": 350,
        "Mac and cheese": 370,
        "Pesto grill veg pizza": 350,
        "Spicy herb marinated mushroom pizza": 380,
        "Mexican green veg pizza": 300,
        "Fiery jalapeno pizza": 320,
        "Primavera gourmet pizza": 360,
        "Chicken pepperoni gourmet": 400
    },
    '700': {
        # SOUPS
        "Broccoli and Almonds": 260,
        "Hot and sour soup": 190,
        "Roasted chicken soup": 270,
        "Veg mancho soup": 180,
        "Veg tomato Basil soup": 150,
        "French onion soup": 200
    }
}

#price dictionary with dish code
price={
    101:150,102:210,103:180,104:120,105:190,106:140,107:200,108:230,109:220,
    201:200,202:260,203:230,204:270,205:310,206:190,207:200,208:240,
    301:120,302:140,303:120,304:170,305:150,306:160,307:200,308:150,309:140,310:220,
    401:220,402:280,403:300,404:250,405:300,406:230,407:260,408:200,
    501:320,502:380,503:250,504:290,505:190,506:250,507:280,508:320,509:300,
    601:350,602:370,603:350,604:380,605:300,606:320,607:360,608:400,
    701:260,702:190,703:270,704:180,705:150,706:200
}

#dictionary mapped from no. of ppl per table to table number
tables = {2:['01','1','03','3','12','13'],
        4:['02','2','04','4','06','6','07','7','08','8','10','14','15','19'],
        6:['05','5','11','16','17'],
        8:['09','9','15','18']}

#taking table number
print("Hey, welcome to our CAFE :)")

validseater = False
while validseater==False:
    ppl = int(input("How many seater table do you want?\n"))
    if ppl == 2:
        print("Table numbers \n01 \n03 \n12 \n13 are available.")
        validseater = True
    elif ppl == 4:
        print("Table numbers \n02 \n04 \n06 \n07 \n08 \n10 \n14 \n15 \n19 are available.")
        validseater = True
    elif ppl == 6:
        print("Table numbers \n05 \n11 \n16 \n17 are available.")
        validseater = True
    elif ppl == 8:
        print("Table numbers \n09 \n15 \n18 are available.")
        validseater = True
    else:
        print("Sorry!! Only 2, 4, 6, and 8 seater tables are available.")

valid_table = False
while valid_table==False:
    table_num = input("Enter your table number: ")
    # table_num_int = int(table_num)
    if ppl == 2 and table_num in tables[2]:
        valid_table = True
        tables[2].remove(table_num)
    elif ppl == 4 and table_num in tables[4]:
        valid_table = True
        tables[4].remove(table_num)
    elif ppl == 6 and table_num in tables[6]:
        valid_table = True
        tables[6].remove(table_num)
    elif ppl == 8 and table_num in tables[8]:
        valid_table = True
        tables[8].remove(table_num)
    else:
        print("selected table is not available . Please enter a valid table number.")
    
print("\nYou can proceed to order food now :)")

#Taking order and appending its cost to the bill
bill = 0
ordered_items = dict() #{dish_code: dish_name}
quantity_items = dict() #{dish_code: quantity_of_dish}
n = 1
while n != 0:
    print("\nChoose a category from below:")
    print("\n1. Beverages - 100")
    print("2. Sandwiches and Wraps - 200")
    print("3. Mocktails and Shakes - 300")
    print("4. Desserts - 400")
    print("5. Appetizers - 500")
    print("6. Pizza and Pastas - 600")
    print("7. Soups - 700")

    category_code = input("\nEnter category code: ")
    new_d=dict()
    
    if category_code in menu:
        print("\nItems available in this category :")
        item_code = int(category_code) + 1
        for item, cost in menu[category_code].items(): 
            print(f"Code: {item_code} - {item} - Rs.{cost}")
            new_d[item_code] = item
            item_code += 1
        print("\n\nAfter you are done choosing food items, enter 0\n")
    else:
        print("\nWRONG CATEGORY CODE!!\nRestart the program")
        exit()
            
    dish_code=1
    while(dish_code!=0):
        dish_code=int(input("Enter dish code: \n"))
        if dish_code in price.keys():
            bill=bill+price[dish_code]
            print(f"{dish_code} - Rs{price[dish_code]} is added to your bill\n")
            ordered_items[dish_code] = new_d[dish_code]
            if dish_code not in quantity_items:
                quantity_items[dish_code] = 1
            else:
                quantity_items[dish_code]+=1
        elif dish_code==0:
            continue
        else:
            print("Invalid dish code.\n")


    print("\nEnter 0 if you want to proceed for billing")
    n=int(input("Enter 1 if you want to go back to category menu again\n"))

bottle=input("\nDo you need a water bottle?   ")
if bottle in "1YESyes":
    num_bottles=int(input("How many bottles do you need?   "))
else:
    num_bottles=0

def generate_token():
    l=[121,345,647]
    x=random.randint(100, 999) 
    while x in l:
        x=random.randint(100,999)
    l.append(x)
    return x
token = generate_token()
gst = round(bill * 0.06, 2)
service_charges = round(bill * 0.02, 2)

print(f"\n\n     ********  {token}  ********\n")
print("#   \t  DISH NAME  \t\t\tPRICE \tQTY\tTOTAL")
a=0
for dish in ordered_items.keys():
    a+=1
    s1 = str(a) + '.\t' + str(ordered_items[dish])
    s1=s1 + ' '*(36-len(s1))
    s2 = str(price[dish]) +'\t '+ str(quantity_items[dish]) +'\t'+ str(price[dish]*quantity_items[dish])
    print(s1+s2)
print(f"\nCost of food items is: Rs.{bill}")
print(f"Cost of water bottles is: Rs.{num_bottles * 20} \n")
print(f"*GST on the food items is: {gst}")
print(f"*Applicable service charges: {service_charges}")
bill = round(bill + gst + service_charges + num_bottles * 20, 2)
print(f"\nTotal after additional charges is: {bill}\n")
print(f"{table_num} is your table number")
print("You can go to bill desk for the payment")
print(f"Your token no. is {token}\n")
print(f"     ********  {token}  ********")
print("\n\tTHANK YOU!\n\tPLEASE VISIT AGAIN :)\n\n")