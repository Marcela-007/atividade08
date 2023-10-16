# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;
valor = float(input("Insira o valor em reais: "))
desconto = float(input("insira o valor do desconto: "))
descontinho = (valor * desconto)/100
pagamento = valor - descontinho
print(f"""
      Valor da compra: R$ {valor}10
      Valor de desconto: {descontinho}%
      Valor final: {pagamento}
""")