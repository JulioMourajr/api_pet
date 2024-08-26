def coletar_informacoes_pet():
    nome = input("Nome do pet: ")

    while True:
        tipo = input("Tipo do pet (cao, gato, peixe, ave, outro): ").lower()
        if tipo in ["cao", "gato", "peixe", "ave", "outro"]:
            break
        else:
            print("Por favor, escolha um tipo válido (cao, gato, peixe, ave, outro).")

    while True:
        sexo = input("Sexo do pet (m, f): ").lower()
        if sexo in ["m", "f"]:
            break
        else:
            print("Por favor, escolha um sexo válido (m para masculino, f para feminino).")

    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Tipo: {tipo}")
    print(f"Sexo: {'Masculino' if sexo == 'm' else 'Feminino'}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

coletar_informacoes_pet()
