# Problem statement: https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import sys,csv

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments ")
elif not(sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv") ):
    sys.exit("Not a CSV file")
before_filename=sys.argv[1]

try:
    with open(before_filename,"r") as before:
            reader = csv.DictReader(before)
            with open(sys.argv[2], "w") as output:
                writer = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
except FileNotFoundError:
    sys.exit(f"Could not read {before_filename}")
