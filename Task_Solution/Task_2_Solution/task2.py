import datetime as dt
injection_dates=[dt.datetime(2023, 1, 3),dt.datetime(2023, 2, 3)]
withdrawal_dates=[dt.datetime(2023, 9, 30),dt.datetime(2023, 10, 30)]
buy_price=[10.3,10.5]
sell_price=[12.3,12.5]
buy_volumn=[1000,0]
sell_volumn=[700,400]
injection_rate = 0.5
withdrawal_rate = 0.5
storage_cost_per_month = 2
events=[]
Max_volumn = 1000
def price_contract(injection_dates,withdrawal_dates,buy_price,sell_price,buy_volumn,sell_volumn,injection_rate,withdrawal_rate,storage_cost_per_month):
    purchase_cost=0
    injection_cost=0
    current_volumn = 0
    for date, price, volume in zip(injection_dates,buy_price,buy_volumn):
        purchase_cost += price*volume
        injection_cost += injection_rate*volume
        current_volumn += volume
        if current_volumn > Max_volumn:
            raise ValueError("Current volume exceeds maximum volume limit.",current_volumn)
        events.append((date, volume))
    revenue_after_sale=0
    withdrawal_cost=0
    for date, price, volume in zip(withdrawal_dates,sell_price,sell_volumn):
        revenue_after_sale += price*volume
        withdrawal_cost += withdrawal_rate*volume
        current_volumn -= volume
        if current_volumn < 0:
            raise ValueError("Current volume cannot be negative.",current_volumn)
        events.append((date,-volume))
    storage_cost=0    
    storage_cost = storage_cost_per_month * (withdrawal_dates[-1].month - injection_dates[0].month)
    total = revenue_after_sale - purchase_cost - injection_cost - withdrawal_cost - storage_cost
    return total 
value = price_contract(injection_dates,withdrawal_dates,buy_price,sell_price,buy_volumn,sell_volumn,injection_rate,withdrawal_rate,storage_cost_per_month)
print(value)
events.sort(key=lambda x: x[0])
print(events)
