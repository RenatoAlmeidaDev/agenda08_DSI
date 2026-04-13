# Programa de pesquisa de opinião - Tudo Web

print("===== Queremos saber sua opinião sobre nosso atendimento 😀 =====")

# Contadores para a respostas
qtde_excelente = 0
qtde_ruim = 0

# Quantidade de pessoas entrevistadas
num_intrevistados = 50

for i in range(num_intrevistados):
    print(f"\nEntrevistado {i + 1}:")

    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))

    print("Deixe sua opinião sobre nosso atendimento:")
    print("1 - EXCELENTE 😃")
    print("2 - BOM 😊")
    print("3 - RUIM 😡")
    opiniao = int(input("Digite sua opinião (1/2/3): "))

# Estrutura de decisão para verificar a opinião dos entrevistados.
    if opiniao == 1:
        qtde_excelente += 1
    elif opiniao == 3:
        qtde_ruim += 1 

#Exibição do resultado final
print("\nRESULTADO DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {qtde_excelente}")
print(f"Quantidade de respostas RUIM: {qtde_ruim}")