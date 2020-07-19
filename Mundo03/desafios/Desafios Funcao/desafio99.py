# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(vet):
    
    if not vet: 
        mVlr = 0
    else:
        mVlr = vet[0]
        
    print(f'{vet} Foram informados {len(vet)} valores ao todo')
    for i in vet:
        if(i >= mVlr):
            mVlr = i
    
    print(f'O maior valor informado é {mVlr}')


vet = [2,3,7,8,1,9]
maior(vet)
vet = [1,2,5,7,3]
maior(vet)
vet = [8,3,5]
maior(vet)

vet = []
maior(vet)
