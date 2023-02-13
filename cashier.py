import pandas as pd
from tabulate import tabulate

#Function for class Transaction
class Transaction:
    
    def __init__(self):
        #dict_txn (dict) = dictionary to store transaction data
        self.dict_txn = dict()
        
    #Function for adding items to shopping cart
    def add_item(self, name, quantity, price):
        '''Where rule is applied:
        name = (String, key)
        quantity = (int), and
        price = (int)
        '''
        #Therefore, first we need to check if the input is correct
        if type(quantity)!=int:
            print("Please input quantity in numbers only")
            
        elif type(price)!=int:
            print("Please input price in numbers only")
            
        #When data input is correct, then it will add data to dict 
        else:
            dict_add = {name: [quantity, price, quantity*price]}
            self.dict_txn.update(dict_add)
            print(f"Thank you. Your shopping cart is as follows: {name} = {quantity} pc with total price of Rp {quantity*price}.")
            
    #Function for showing all items and price in shopping cart 
    def print_item(self):
        
        header = ["Item Name", "Item Quantity", "Price per Item", "Total Price"]
        print(tabulate([[k,] + v for k,v in self.dict_txn()], 
                       header, tablefmt = "github"))

    #Function for changing item names in shopping cart        
    def update_item_name(self, name, new_name):
        '''Where rule is applied:
        name (String) = original item name
        new_name (String) = new item name'''
        
        temp = self.dict_txn[name]
        self.dict_txn.pop(name)
        self.dict_txn.update({temp: new_name})
        
        #Showing items in shopping cart that has been updated
        print(f"Item name has been succesfully changed from {name} to {new_name}.")
        
    #Function for changing item quantities in shopping cart   
    def update_item_quantity(self, name, new_quantity):
        
        #Where rule is applied:
        #name (String) = item name
        #new_quantity (Int) = new item quantity
        
        #Therefore, first we need to check if the input is correct
        if type(new_quantity)!=int:
            print("Please input quantity in numbers only")
            
        #When data input is correct, then it will update data to dict
        else:
            self.print_order()
            print(f"You have succesfully changed {name} quantity to {new_quantity}.")
        
    #Function for changing item price in shopping cart 
    def update_item_price(self, name, new_price):
        
        #Where rule is applied:
        #name (String) = item name
        #new_price (Int) = new item price
        
        #Therefore, first we need to check if the input is correct
        if type(new_price)!=int:
            print("Please input price in numbers only")
            
        #When data input is correct, then it will update data to dict
        else:
            self.dict_txn[name][0] = new_price
            self.dict_txn[name][2] = new_price*self.dict_txn[name][1]
            
            print(f"You have succesfully changed {name} price to {new_price}.")    
    
    #Function for deleting an item in shopping cart 
    def delete_item(self, name):
        try:
            self.dict_txn.pop(name)
            print(f"You have successfully deleted {name} from your cart")
        except:
            print('Please reset transaction')
            
    #Function for resetting transaction
    def reset_transaction(self):
        
        self.dict_txn = {}
        print(f"You have successfully removed all your items in shopping cart") 
    
    #Function to check if the order in shopping cart is correct        
    def check_order(self):
        correct_item = 0
        item_quantity = 0
        for key in self.dict_txn:
            if key != " " and type(self.dict_txn[key][0]) == int and type(self.dict_txn[key][1]) == int:
                correct_item += 1
            item_quantity += 1
        if correct_item == item_quantity:
            print(f"Thank you. You have successfully added items to shopping cart")
            print(Transaction.print_item(self))
        else:
            print("Please input item data correctly")
   
    #Function to print total price in shopping cart
    def total_price(self):
        self.calculate_total_price()
        self.check_order()
        print("")
        print(f"Congratulations! Your order of Rp {self.total_price}")
        print(f"gets a discount for: {self.discount}%")
        print(f"So your order price is now: Rp {self.total_price - (self.total_price * self.discount / 100)}")
    
    def calculate_discount(self):
        if self.total_price > 200_000 and self.total_price <= 300_000:
            self.discount = 5
        elif self.total_price > 300_000 and self.total_price <= 500_000:
            self.discount = 8
        elif self.total_price > 500_000:
            self.discount = 10
        else:
            self.discount = 0