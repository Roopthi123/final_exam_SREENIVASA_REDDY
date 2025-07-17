# Task 6: Get Honduras population data (2010-2020) using wbdata

import wbdata         # Import wbdata package
import datetime       # Import datetime for date handling

country_code = "HND"  # ISO country code for Honduras
indicator = {"SP.POP.TOTL": "Population"}  # World Bank indicator for total population

data_date = (datetime.datetime(2010, 1, 1), datetime.datetime(2020, 12, 31))  # Date range

# Fetch data from World Bank
pop_data = wbdata.get_dataframe(indicator, country=country_code, data_date=data_date)

# Print results in readable format
for year, row in pop_data[::-1].iterrows():  # Reverse to print from 2010 to 2020
    print(f"Honduras, {year.year}: {int(row['Population'])}") 