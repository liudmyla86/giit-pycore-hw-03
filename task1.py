from datetime import datetime

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        today = datetime.today()
        difference = today - input_date
        return difference.days
    except ValueError:
    
        return 'Incorrect data format.Use the format "YYYY-MM-DD".'
print(get_days_from_today("2024-9-10"))
        

        