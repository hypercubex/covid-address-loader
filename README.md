# poc-covid-address-loader
load covid case address from API that https://chp-dashboard.geodata.gov.hk/covid-19/zh.html uses

## How to execute

1. poetry install
2. poetry run python3 [all | current | expired | last_7_days]/get_[all | count | locations].py

please note that the python files only get and print, you may want to add ` > <filename>.json` to save the result
