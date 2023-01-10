# a dict for mock currencies EUR: 4.75
import argparse
import requests


def parser():
    parser = argparse.ArgumentParser(description='Exchange the currencies')

    parser.add_argument('amount', type=int, help='an integer for the currency')
    parser.add_argument('currency', type=str, help='currency type')

    args = parser.parse_args()

    return args


def fetch_currency_rate(currency: str) -> float:
    r = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/B/{currency}/')

    rates = r.json()
    if rates['code'] == currency:
        return rates['rates'][0]['mid']


def convert(value: float, currency: str) -> float:
    try:
        exchange_rate = fetch_currency_rate(currency)
        return round(value * exchange_rate, 2)
    except:
        print(f"no data available for {currency}")


if __name__ == '__main__':
    args = parser()
    output = convert(value=args.amount, currency=args.currency)
    if output is not None:
        print(f"{output} PLN")
