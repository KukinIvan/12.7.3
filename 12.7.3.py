money = int(input("Введите сумму:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
bank_deposit = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

TKB = money / 100 * per_cent['ТКБ']
SKB = money / 100 * per_cent['СКБ']
VTB = money / 100 * per_cent['ВТБ']
SBER = money / 100 * per_cent['СБЕР']

deposit = [TKB, SKB, VTB, SBER]

print("Сумму, которую Вы заработаете в банках :",TKB,"- ТКБ,",SKB,"- СКБ,",VTB,"- ВТБ,",SBER,"- СБЕР.")

bank_deposit['ТКБ'] = TKB
bank_deposit['СКБ'] = SKB
bank_deposit['ВТБ'] = VTB
bank_deposit['СБЕР'] = SBER

max_bank_deposit = max(bank_deposit)

print('Максимальная сумма, которую Вы можете заработать —', str(max(deposit)), 'В банке -', str(max_bank_deposit),)