from datetime import datetime


STORE_NAME = " SemiColon Stores"

STORE_LOCATION = "312, Herbert Macaulay Way , Sabo Yaba. Lagos."

phone_number = "07053531269"

customer_name = input("Enter customer's name : ")

product_name = input("Enter the name of product: ")

quantity = int(input("Enter the units sold: "))

price_per_unit = int(input("Enter the price of each unit: "))


total_sales = price_per_unit * quantity

cashier_name = input("Enter the name of cashier at point of sale :  ") 

today_date = datetime.now()

receipt = f"""
{STORE_NAME}
{STORE_LOCATION}
TEL: {phone_number}
Date :{today_date}
{customer_name}

=======================================================================
	ITEM		QTY		PRICE		TOTAL(NGN)
-----------------------------------------------------------------------
	{product_name}		{quantity}		{price_per_unit}		{total_sales}
------------------------------------------------------------------------

"""
print(receipt)
	

	  





