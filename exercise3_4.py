month_dict = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}
def decode_date(date):
    day, month, year = date.split("-")
    month = month_dict[month]
    if len(year) == 2:

        year = "20" + year 
    else:
        year= year
    return (year, month, day)

print(decode_date("8-MAR-85"))
