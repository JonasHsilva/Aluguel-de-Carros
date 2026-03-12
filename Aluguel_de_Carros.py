#valor da diária R$50,00
#Valor do Km R$0,20

dias = int(input('Dias Locados: '))
km = float(input('Km rodados: '))
valor = (dias * 50) + (km * 0.20)
print(' ')
print('O total a ser pago será de === R${:.2f} ==='.format(valor))
