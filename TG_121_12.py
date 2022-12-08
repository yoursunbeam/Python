purchased_shares=int(input('Введите количество приобретенных акций '))
cost_purchased_shares=float(input('Введите стоимость приобретенных акций за шт '))
commission_purchase=int(input('Введите комиссию при покупке в % '))

shares_sold=int(input('Введите количество проданных акций '))
cost_shares_sold=float(input('Введите стоимость проданных акций за шт '))
commission_sale=int(input('Введите комиссию при продаже в % '))

money_purchase_shares=purchased_shares*cost_purchased_shares
amount_commission_purchase=money_purchase_shares*commission_purchase/100

money_shares_sold=shares_sold*cost_shares_sold
amount_commission_sale=money_shares_sold*commission_sale/100

rest_money=(money_shares_sold-amount_commission_sale)-(money_purchase_shares-amount_commission_purchase)

print('Сумма денег на покупку акций=',money_purchase_shares)
print('Сумма комиссии брокеру при покупке=',amount_commission_purchase)
print('Сумма денег при продаже акций=',money_shares_sold)
print('Сумма комиссии брокеру при продаже=',amount_commission_sale)
print('Сумма денег,которая осталась=',rest_money)
