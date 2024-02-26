total=desp_fix=desp_var=extras=renda=0

print ('----------- BEM VINDO AO SEU CONTROLE DE GASTOS ------------')
salario = float(input('Digite o seu salário: R$ '))
total_remu = float(input('Complemento de renda: R$ '))
planejamento = float(input('Digite o valor total planejado: '))
print('''Despesas fixas (F):
    Aluguel
    Conta de água 
    Conta de luz 
    Internet 
    Mercado
    Mensalidades 
Despesas variáveis (V):
    Medicamentos 
    Delivery
    Lazer 
    Beleza 
Extras (E) ''')

while True:
    nome = str(input('Digite a origem do gasto [F/V/E]:\n ')).strip().upper()
    valor = float(input('Digite o valor gasto:\n '))
    total += 1
    if nome in 'F':
        desp_fix += valor

    if nome in 'V':
        desp_var += valor

    if nome in 'E':
        extras += valor

    if nome not in 'FVE':
        print('Por favor, digite apenas as letras informadas.')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

total = desp_fix + desp_var + extras
renda = salario + total_remu

if planejamento >= total:
    diferença = planejamento - total

elif total > planejamento:
    diferença = total - planejamento

print('--------BALANÇO--------')
print(f'Renda total: {renda:.2f}')
print(f'Total despesas fixas: {desp_fix:.2f}')
print(f'Total despesas variáveis: {desp_var:.2f}')
print(f'Total de gastos extras: {extras}')
print(f'Total das despesas: {total:.2f}')
print(f'Total planejado: {planejamento:.2f}')
print(f'Diferença do planejamento para o total: {diferença:.2f}')
print('--------- FIM ----------')

if planejamento >= total:
    print('Parabéns! Você conseguiu cumprir com o seu planejamento mensal.')

elif total > planejamento:
    print('Poxa! Você não conseguiu cumprir com seu planejamento mensal.\n')
    print('''Conselhos que busquei da internet:
    -Corte os gastos desnecessários.
    -Invista seu dinheiro em uma conta digital.
    -Separe uma parte do salário todo mês.
    -Forme sua reserva de emergência.
    -Tenha cuidado com o cartão de crédito.''')