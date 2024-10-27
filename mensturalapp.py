from datetime import datetime, timedelta

user_age = int(input("Please enter your age :  "))

user_start_date = input("please the date in this format yyyy-mm-dd:  ")
	
user_end_date = input("please the date in this format yyyy-mm-dd: ")

start_date = datetime.strptime(user_start_date,"%Y-%m-%d")

end_date = datetime.strptime(user_end_date,"%Y-%m-%d")

flow_days = end_date.day - start_date.day

next_flow_date = start_date + timedelta(days=28)

safe_period = next_flow_date + timedelta(days=5)

year = start_date.year
month= start_date.month
day = start_date.day
print(f"Hello bestie your flow days are:  " ,flow_days)
print(f"Hello bestie your next flow date: ",next_flow_date)
print(f"Hello bestie your safeperiod are:  ",safe_period)
 




