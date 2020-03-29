import json as json
from datetime import date

import pandas as pd

from currency_converter import CurrencyConverter

# Globals
SOURCE = 'EUR'
AMOUNT = 1

JSON_FILE_NAME = './currency.json'
CSV_FILE_NAME = './currency.csv'

# Initialization
counter = 0
converter = CurrencyConverter()

# List of Destination currencies
currencies = ["NOK", "QAR", "SGD", "JOD", "DKK", "MYR", "ALL", "HUF", "HRK", "GBP", "CHF", "RUB", "BRL", "CZK", "EGP",
              "IDR", "TRY", "CAD", "AED", "CNY", "RSD", "THB", "ZAR", "ISC", "ILS", "AUD", "JPY", "RON", "HKD", "MXN",
              "MAD", "BGN", "PLN", "USD", "SEK", "UAH"]

# List of dates
dates = [date(2019, 7, 1),
         date(2019, 7, 15),
         date(2019, 7, 31),
         date(2019, 8, 1),
         date(2019, 8, 15),
         date(2019, 8, 29),
         date(2019, 9, 2),
         date(2019, 9, 16),
         date(2019, 9, 30),
         date(2019, 10, 1),
         date(2019, 10, 15),
         date(2019, 10, 31)]

base_currency_dict = {}

currency_column = {}

# Creating currency column...
for currency in currencies:
    currency_column[counter] = currency
    counter += 1

# Adding Currency column in the base dict
base_currency_dict['Currencies'] = currency_column

for instance in dates:
    # Reset of the counter
    counter = 0
    # Reset of the column dict to add
    date_currency_dict = {}

    for currency_destination in currencies:
        try:
            # Get the currency value by the given args
            currency_value = converter.convert(AMOUNT, SOURCE, currency_destination, date=instance)
            # Add the value in a row
            date_currency_dict[counter] = currency_value
        except:
            date_currency_dict[counter] = None

        # Update the index
        counter += 1

    base_currency_dict[instance.strftime('%y-%b-%d')] = date_currency_dict

print(base_currency_dict)

# Save the dict in a JSON for future use...
with open(JSON_FILE_NAME, 'w') as json_file:
    json.dump(base_currency_dict, json_file)

# Export in a CSV for future use...
data_frame = pd.read_json(JSON_FILE_NAME)
exported = data_frame.to_csv(CSV_FILE_NAME, index=None, header=True)
