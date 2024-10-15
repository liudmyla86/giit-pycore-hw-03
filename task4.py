from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_difference = (birthday_this_year - today).days

        if 0 <= days_difference <= 7:
            if birthday_this_year.weekday()>=5:
                    next_monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                    congratulation_day = next_monday
            else:
                    congratulation_day = birthday_this_year
    

            upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_day": congratulation_day.strftime('%Y.%m.%d')
                })


    return upcoming_birthdays               
   
    
users = [
    {"name": "Liudmyla Munich","birthday": "1985.11.15" },
    {"name":"Daniel Gubich", "birthday": "1984.10.27"},
    {"name": "Oksana Loza", "birthday":"1991.10.16"},
    {"name":"Anatoliy Lyashch", "birthday": "2001.10.18"}

]
upcoming_birthdays = get_upcoming_birthdays(users)

print("This weeklist of birthdays:", upcoming_birthdays)