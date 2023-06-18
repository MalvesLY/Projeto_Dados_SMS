import pandas as pd

from twilio.rest import Client

account_sid = 'AC292fb5538122953aae97351783aa984e'
auth_token = 'f119a1942dbc0aab60c3bd6243de8ec6'
client = Client(account_sid, auth_token)

# Abrir todos as tabelas - ok
# Procurar por faturamentos maiores do que R$55000 - ok
# Se o vendedor fizer mais de R$55000 em vendas (o primeiro que fizer)
    # Enviar SMS com o nome do vendedor e o faturamento das vendas - ok

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in meses:
    tabela = pd.read_excel(f'{mes}.xlsx')
    #print(mes)
    #print(tabela)
    if (tabela['Vendas'] > 55000).any():
        vendas = tabela.loc[tabela['Vendas'] > 55000, 'Vendas'].values[0]
        vendedor = tabela.loc[tabela['Vendas'] > 55000, 'Vendedor'].values[0]
        print(f'O vendedor {vendedor} bateu a meta com um faturamento de R${vendas:.2f} no mês {mes}.')

        message = client.messages.create(
            to="+5521984507274",
            from_="+5521984507274",
            body=f'O vendedor {vendedor} bateu a meta com um faturamento de R${vendas:.2f} no mês {mes}.')

        print(message.sid)
