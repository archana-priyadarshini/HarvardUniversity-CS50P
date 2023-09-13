#Problem Statement: https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import sys
import requests

if(len(sys.argv)<2):
    sys.exit("Missing command-line argument")
else:
    try:
        dollars=float(sys.argv[1])
        r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rate=r["bpi"]["USD"]["rate_float"]
        amount=dollars*rate
        print(f"${amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit()
