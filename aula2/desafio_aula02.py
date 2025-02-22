x = [1, 2, 3, 4, 5] 
y = [2, 4, 5, 4, 5]

xMedia = sum(x) / len(y)
yMedia = sum(y) / len(y)

#print(xMedia)  #testando se realmente estava somando e dividindo pelo número de indices
#print(yMedia)

somatorioXY = 0
somatorioXX = 0

for i in range(len(x)): #acessa cada posição do indice
    somatorioXY += (x[i] - xMedia) * (y[i] - yMedia) #resultado de indice menos a media(x)  X  resultado de indice menos media(y)  - (multiplicando as diferenças) 
    somatorioXX += (x[i] - xMedia) ** 2 #resultado do indice menos a media ao quadrado

    #print(f'resultado do x - media e y - media: {somatorioXY}')  #testando se estava imprimindo corretamente
    #print(f'resultado do x - media ao quadrado: {somatorioXX}')

beta1 = somatorioXY / somatorioXX
beta0 = yMedia - beta1 * xMedia

print(f'BETA 1: {beta1}')
print(F'BETA 0: {beta0}')


