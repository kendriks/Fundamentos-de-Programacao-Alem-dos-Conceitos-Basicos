arquivoN = open('valores.txt', 'rt')
arquivoS = open('valores_totais.txt', 'wt')
print('<<Processando entrada>>')
soma = 0
for linha in arquivoN:
    soma += int(linha)
    print(linha.rstrip(), file=arquivoS)
print('\nTotal: ' + str(soma), file=arquivoS)
arquivoS.close()
print('Saída completa')