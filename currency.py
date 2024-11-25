def currency_converter(amount,currency):
    rates={
        'USD_to_EUR':0.75,
        'EUR_to_USD':1.18,
        'USD-to_GBP':0.85,
        'GBP_to_USD':1.33
    }
    rate=rates.get(currency,None)
    if rate:
        return amount*rate
    else:
        return "Invalid Currency"
print(f"UDS to EUR : {currency_converter(100,'USD_to_EUR')}")
print(f"USD_to_IND : {currency_converter(100,'USD_to_IND')}")