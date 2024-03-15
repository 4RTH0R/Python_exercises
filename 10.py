nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
residencia = input("Insira sua residência: ")
resposta = input("Seus dados estão corretos? (s/n): ")
dados = nome + " " + idade + " " + residencia
if resposta == "s":
    print(f"Estes são seus dados: {dados}" )
else:
    print("Só lamento filho(a) :/")