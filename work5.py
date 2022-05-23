debit = float(input('введите размер выручки:'))

credit = float(input('введите размер издержек:'))

no_profit = debit - credit

if debit > credit:
    cash = debit - credit
    print ('вы работаете с прибылью', cash)
    workman = int(input('введите количество работников:'))
    print(f'зарплата работника составляет:{(cash/workman):.2f}')

elif debit == credit:
    print('вы работаете в ноль')

else:
    
    print('у вас убытки:', no_profit)
    
        
