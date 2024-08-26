## Api de Pets

Esse código em Python é responsável por coletar informações sobre um animal de estimação, como o nome, a idade e o peso. Ele utiliza loops while para garantir que as entradas do usuário sejam válidas, ou seja, que a idade e o peso sejam números não negativos.

Descrição do funcionamento:
Nome do Pet:

O código solicita ao usuário que insira o nome do pet por meio do input(), armazenando a informação na variável nome.
Idade do Pet:

Em um loop while, o código pede ao usuário para inserir a idade do pet.
Utiliza um bloco try-except para capturar erros de tipo, garantindo que o usuário insira um número inteiro válido.
Caso o usuário insira um valor negativo, o código exibe uma mensagem de erro e solicita uma nova entrada.
Peso do Pet:

Similar ao processo de idade, o código solicita ao usuário que insira o peso do pet em um loop while.
O código também usa try-except para capturar entradas inválidas e garantir que o valor seja um número positivo.
Exibição das Informações:

Após coletar e validar todas as informações, o código exibe os detalhes do pet, incluindo nome, idade e peso.
Função sugerida: coletar_informacoes_pet()
Essa função poderia encapsular todo o processo de coleta e validação de dados, facilitando o uso e a reutilização do código em diferentes partes de um programa.