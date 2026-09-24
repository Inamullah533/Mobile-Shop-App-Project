import json 
from pathlib import Path





class shop:
    database = 'data.json'
    data = []
    order_history = []

    def load_data(self):
        try:
            database_path = Path(self.database)
            if database_path.exists():
                with database_path.open('r', encoding='utf-8') as file:
                    shop.data = json.load(file)

        except Exception as err:
            print(f"The error occur as {err}")            

    def save_data(self):
        try:
            with Path(self.database).open('w', encoding='utf-8') as file:
                json.dump(shop.data, file, indent=4)

        except Exception as err:
            print(f"The error occur as {err}")        

    def Dataentry(self):
        try:
            self.load_data()
            info={
                "Product_Name": input("Product Name :- "),
                "Quantity": int(input("Quantity of Products :- ")),
                "Price": int(input("Price of Product :- "))
            }        
        except Exception as err:
            print(f"The error occur as {err}")


        shop.data.append(info)
        self.save_data()


    def Seeproducts(self):
        try:
            self.load_data()
            if not shop.data:
                print("Shop products List is Empty ! ") 
            else:
                print("The List of this Shop Product is :- \n\n\n")
                for product in shop.data:
                    for name, value in product.items():
                        print(f"{name}: {value}")
                    print()

        except Exception as err:
            print(f"The error occur as {err}")    



    def Addorder(self):
        try:
            self.load_data()
            if not shop.data:
                print("Shop products List is Empty ! ")
                return

            print("The List of this Shop Product is :- \n")
            for index, product in enumerate(shop.data, start=1):
                print(f"{index}. {product['Product_Name']} - Quantity: {product['Quantity']} - Price: {product['Price']}")
            print()

            product_name = input("Enter product name to order: ")
            quantity = int(input("How many items do you want: "))

            for product in shop.data:
                if product["Product_Name"].lower() == product_name.lower():
                    if quantity <= product["Quantity"]:
                        total = quantity * product["Price"]
                        product["Quantity"] -= quantity
                        self.save_data()
                        print(f"Your total is {total}")
                        print("Order completed successfully.")
                    else:
                        print("Not enough product in stock.")
                    return

            print("Product not found in the shop list.")

        except ValueError:
            print("Please enter a valid number.")
        except Exception as err:
            print(f"The error occur as {err}")  
          


    def Ordercancel(self):
        self.load_data()

        if not shop.order_history:
            print("No previous order list.")
            return

        print("Previous order list:")
        for i, order in enumerate(shop.order_history, start=1):
            print(f"{i}. {order['Product_Name']} - Quantity: {order['Quantity']} - Total: {order['Total']}")

        cancel_no = int(input("Enter order number to cancel: ")) - 1

        if 0 <= cancel_no < len(shop.order_history):
            order = shop.order_history.pop(cancel_no)

            for product in shop.data:
                if product["Product_Name"].lower() == order["Product_Name"].lower():
                    product["Quantity"] += order["Quantity"]
                    self.save_data()
                    break

            print("Order cancelled successfully.")
        else:
            print("Invalid order number.")










user = shop()
print("Press 1 for Data Enter of Mobile Accessories  ")
print("Press 2 for See Product of shop  ")
print("Press 3 for Add the order ")
print("Press 4 for cancel order " )

response = int(input(f"Tell ur response : "))

if response == 1:
    user.Dataentry()

if response ==2:
    user.Seeproducts()    

if response ==3:
    user.Addorder()   

if response ==4:
    user.Ordercancel()