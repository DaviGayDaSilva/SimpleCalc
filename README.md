# SimpleCalc

SimpleCalc é uma calculadora simples em Python que roda no terminal. Pergunta dois números ao usuário e exibe operações básicas: soma, subtração, multiplicação, divisão, potência, módulo, raiz quadrada e um cálculo de "porcentagem" (produto dividido por 100). O programa usa `time.sleep(2)` para criar um efeito de suspense.

Como executar

1. Tenha Python 3 instalado.
2. No terminal, rode:

   python3 calc.py

Observações

- O programa atualmente lê números com `int()` (apenas inteiros).
- Divisão ou módulo por zero causará erro na versão atual; tome cuidado ao usar 0 como segundo número.
- A raiz quadrada de números negativos não é tratada (usa `math.sqrt`).

Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o projeto (ex.: aceitar floats, tratar erros, adicionar menus).
