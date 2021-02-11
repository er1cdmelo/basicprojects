altura = input('Qual é a sua altura?')
peso = input('Qual é o seu peso?')
imc = float(altura)
imc1= float(altura)*float(imc)
imcc = float(peso)/float(imc1)
print('Aqui estão os resultados! Seu IMC é de:', imcc, 'kg/m2')
if imcc < 18.5:
    print('MAGREZA')
if 24.9>imcc > 18.5:
    print('NORMAL')
if 29.9 > imcc>25.0:
    print('SOBREPESO')
if 39.9> imcc > 30.0:
    print('OBESIDADE')
if imcc > 40.0:
    print('OBESIDADE GRAVE')
