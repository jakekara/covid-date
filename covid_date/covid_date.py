import datetime

def covid_year(date):
    covid_epoch =  datetime.date(2020, 3, 18)

    covid_years = (date - covid_epoch).days
    return covid_years

def covid_year_now():
    current_date = datetime.datetime.now().date()
    return covid_year(current_date)
