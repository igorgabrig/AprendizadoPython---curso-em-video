try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b


except (ValueError, TypeError):
    print('Tivemos um problema os tipos de dados digitados')

except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')

except Exception as erro:
   print(f'Problema encontrado foi {erro.__class__}')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print("FIM!!!")
