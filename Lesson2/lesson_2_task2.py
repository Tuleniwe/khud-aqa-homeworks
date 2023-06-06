def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False
    
year = 1995
leap_year = is_year_leap(year)
print(f"Год {year}: {leap_year}")