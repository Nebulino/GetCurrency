import csv
import json as json
from datetime import date

from currency_converter import CurrencyConverter

# Globals
SOURCE = 'EUR'
AMOUNT = 1

# List of Destination currencies
destination = ["NOK", "QAR", "SGD", "JOD", "DKK", "MYR", "ALL", "HUF", "HRK", "GBP", "CHF", "RUB", "BRL", "CZK", "EGP",
               "IDR", "TRY", "CAD", "AED", "CNY", "RSD", "THB", "ZAR", "ISC", "ILS", "AUD", "JPY", "RON", "HKD", "MXN",
               "MAD", "BGN", "PLN", "USD", "SEK", "UAH"]

dates = [date(2019, 7, 1),
         date(2019, 7, 15),
         date(2019, 7, 31),
         date(2019, 8, 1),
         date(2019, 8, 15),
         date(2019, 8, 31),
         date(2019, 9, 1),
         date(2019, 9, 15),
         date(2019, 9, 30),
         date(2019, 10, 1),
         date(2019, 10, 15),
         date(2019, 10, 31)]

converter = CurrencyConverter()

base_currency_dict = {}

for instance in dates:
    print('#######################', instance, '#######################')

    for currency_destination in destination:
        counter = 0
        date_currency_dict = {}
        try:
            currency_value = converter.convert(AMOUNT, SOURCE, currency_destination, date=instance)
            # print(currency_value, currency_destination)
            date_currency_dict[currency_destination] = currency_value
            counter += 1
        except:
            # print(currency_destination, 'not supported')
            date_currency_dict[currency_destination] = None

        base_currency_dict[instance.strftime('%a-%b-%d')] = date_currency_dict
        print('Done', counter)

print(base_currency_dict)

with open('./currency.json', 'w') as json_file:
    json.dump(base_currency_dict, json_file)
