import requests
import sys

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        number = sys.argv[1]
        try:
            number = float(number)
            if float(number):
                r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
                data = r.json()
                bitcoin = data['bpi']['USD']['rate_float']
                amount = bitcoin * number
                print(f"${amount:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()
