"""
try:
    <comandos>
except:
    <caso haja erro>
else:
    <comandos q haja erro>
finally:
    <comandos independentemente de existir erro ou não>
"""
try:
    valor1=float(input(";Digite o primeiro valor:"))
    valor2=float(input(";Digite o segundo valor:"))
    resp= valor1/valor2
    print(resp)
except ValueError:
    print("Digite um valor numerico")
except ZeroDivisionError as erroDivisao:
    print(erroDivisao)
except:
    print("Mano moio, chame o ADM")
else:
    print("operacao executada com sucesso")
finally:
    print("Obrigado por utilizar nosso sistema")



