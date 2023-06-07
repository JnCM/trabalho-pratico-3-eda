# Trabalho Avaliativo 3 - EDA
Repositório contendo os códigos do trabalho avaliativo 3, da disciplina INF610 - Estrutura de Dados e Algoritmos.

## Execução dos códigos

Para executar a implementação, basta digitar o seguinte comando no terminal:

```bash
python main.py nome_do_arquivo.txt opcao
```

Note que `nome_do_arquivo.txt` deve ser substituído pelo caminho do arquivo de teste com sua extensão. Já o parâmetro `opcao` significa selecionar qual método utilizar para resolver o teste. Abaixo está a lista das opções permitidas:

- 1: Paradigma Força-bruta;
- 2: Paradigma Busca Exaustiva;
- 3: Paradigma Backtracking;
- 4: Paradigma Programação Dinâmica (Bottom-up);
- 5: Paradigma Programação Dinâmica (Top-down);
- 6: Paradigma Guloso;

Para executar testes que não estão no diretório `/tests`, basta criar um arquivo seguindo a estrutura abaixo:

```txt
5
2 12
1 10
3 20
2 15
```

A primeira linha do arquivo indica a capacidade da mochila. A partir da segunda linha em diante, contém o par (w, v), indicando o peso de cada item e seus respectivos valores.

## Exemplo de execução

Comando para executar o arquivo de testes `tests/test_slide.txt`, utilizando o paradigma de busca exaustiva:

```bash
python main.py tests\test_slide.txt 2
```

Note que o caminho do arquivo deve ser passado de acordo com o seu sistema operacional.

Para o comando acima, o resultado esperado será exibido da seguinte maneira:

```txt
================= Busca Exaustiva ==================
Item(ns) selecionado(s): [0, 1, 3]
Valor total do(s) item(ns): 37
```
