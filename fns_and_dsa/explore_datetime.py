from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:")
    print(current_date.strftime("%Y-%m-%d %H:%M:%S")) 

def calculate_future_date(number_of_days):
    future_date = datetime.now() + timedelta(days=number_of_days)
    print("Future date:")
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date:"))
calculate_future_date(number_of_days)