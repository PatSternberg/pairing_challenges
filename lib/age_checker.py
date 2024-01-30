import datetime
def age_checker(date):
    try:
        date_of_birth = datetime.datetime.strptime(date,"%Y-%m-%d")
    except:
        if type(date) == str:
            raise Exception('Wrong format')
        else:
            raise Exception('Wrong type')
    date_now = datetime.date.today()
    current_age = date_now.year - date_of_birth.year
    if current_age >= 16:
        return f'Access granted - you are {current_age}!'
    else:
        return f'You are {current_age} and are required to be 16 - access denied!'