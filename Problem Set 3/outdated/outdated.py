# Problem statement: https://cs50.harvard.edu/python/2022/psets/3/outdated/
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date: ").title().strip().split(" ")
        if len(date)>1 and date[1].endswith(","):
            mm,dd,yyyy=months.index(date[0])+1,int(date[1].replace(",","")),date[2]
        elif len(date)==1:
            mm,dd,yyyy=[int(x) for x in date[0].split("/")]
        if(mm>12 or dd>31):
            raise ValueError
        print(f"{yyyy}-{mm:02}-{dd:02}")
        break
    except (ValueError,NameError):
        pass