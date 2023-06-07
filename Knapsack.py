class Knapsack:
    """
    Classe que mapeia o problema da mochila para os
    diferentes tipos de paradigmas de programação.

    Parâmetros
    ----------
        - W (int): Capacidade da mochila;
        - n (int): Quantidade de itens disponíveis;
        - weights (list[int]): Lista de tamanho n, contendo os pesos de cada item;
        - values (list[int]): Lista de tamanho n, contendo os valores de cada item.
    """

    def __init__(self, W: int, n: int, weights: list[int], values: list[int]):
        self.__n = n
        self.__W = W
        self.__weights = weights
        self.__values = values
    
    def BFKnapsack(self, i, j):
        if i == 0 or j == 0:
            return 0
        
        if j < self.__weights[i-1]:
            value = self.BFKnapsack(i-1, j)
        else:
            value = max(self.BFKnapsack(i-1, j), self.BFKnapsack(i-1, j - self.__weights[i-1]) + self.__values[i-1])
        return value

    def brute_force(self):
        value = self.BFKnapsack(self.__n, self.__W)
        print(value)

    def generate_subsets(self) -> list[list[int]]:
        """
        Método que gera o conjunto potência dos itens
        para o algoritmo de busca exaustiva. Utiliza
        a abordagem de conjunto de partes.

        Retorno
        -------
            - subsets (list[list[int]]): Conjunto potênica dos itens.
        """

        # Inicializa o conjunto potência
        # com o conjunto vazio
        subsets = [[]]
        
        for i in range(self.__n):
            temp_subsets = []
            for subset in subsets:
                # Inclui no conjunto potência os subconjuntos já existentes,
                # mas com o item da iteração
                temp_subsets.append(subset + [i])
            subsets += temp_subsets
        
        return subsets

    def exaustive_search(self) -> tuple[list[int], int]:
        """
        Método que executa o paradigma de busca exaustiva.
        Utiliza a abordagem de verificar todos os subconjuntos
        possíveis do conjunto potência, descartando os subconjuntos
        inviáveis e mantendo o rastreio do melhor.

        Retorno
        -------
            - subset_winner (list[int]): Subconjunto de itens selecionados.
            - max_value (int): Valor total dos itens da mochila.
        """

        max_value = 0
        subset_winner = None
        # Lista todas as possíveis soluções
        subsets = self.generate_subsets()
        
        for subset in subsets:
            sum_of_weights = 0
            sum_of_values = 0
            
            # Passa por cada subconjunto somando
            # seus pesos e seus valores
            for item in subset:
                sum_of_weights += self.__weights[item]
                sum_of_values += self.__values[item]
            
            # Verifica se o total de pesos do subconjunto
            # atende a capacidade da mochila (descarta soluções inviáveis)
            if sum_of_weights <= self.__W:
                # Verifica se o total de valores dos itens é o maior
                # (Mantém o rastreio da melhor solução até o momento)
                if sum_of_values > max_value:
                    max_value = sum_of_values
                    subset_winner = subset
        
        return subset_winner, max_value

    def backtracking(self):
        pass

    def search_items_in_table(self) -> list[int]:
        """
        Método que constrói o subconjuntos de itens selecionados para serem
        inseridos na mochila no paradigma de programação dinâmica. Percorre
        a tabela de memorização a partir da última posição e verifica quais
        itens foram inseridos.

        Retorno
        -------
            - subset_winner (list[int]): Subconjunto de itens selecionados.
        """

        temp_w = self.__W
        subset_winner = []
        for i in range(self.__n, 0, -1):
            # Verifica se o item atual, com o peso atual da mochila
            # possui valor maior que o item anterior, significando que
            # ele foi inserido na mochila, caso houver essa variação
            if self.__F[i][temp_w] > self.__F[i-1][temp_w]:
                subset_winner.append(i-1)
                temp_w -= self.__weights[i-1]
        subset_winner.reverse()

        return subset_winner

    def dynamic_programming_bottom_up(self) -> tuple[list[int], int]:
        """
        Método que executa o paradigma de programação dinâmica (bottom-up).
        Utiliza a abordagem de preencher a tabela de memorização de maneira
        iterativa, resolvendo todos os subproblemas de forma ótima, até chegar
        no problema da solução final.

        Retorno
        -------
            - subset_winner (list[int]): Subconjunto de itens selecionados.
            - max_value (int): Valor total dos itens da mochila.
        """

        # Inicializa a tabela de memorização dos valores dos itens
        # F[i][0] e F[0][j] possuem valores iguais a 0
        self.__F = [[0 for j in range(self.__W+1)] for i in range(self.__n+1)]
        
        for i in range(1, self.__n+1):
            for j in range(1, self.__W+1):
                # Avalia se o item possui peso que caiba na mochila de capacidade j
                if self.__weights[i-1] <= j:
                    # Se o item tem peso adequado, verifica se vale a pena inseri-lo na mochila
                    # ou manter a mochila com os itens que já estão nela
                    self.__F[i][j] = max(self.__F[i-1][j], self.__F[i-1][j - self.__weights[i-1]] + self.__values[i-1])
                else:
                    # Se o item não possui peso adequado,
                    # mantém a mochila com os itens que já estão nela
                    self.__F[i][j] = self.__F[i-1][j]
        
        return self.search_items_in_table(), self.__F[self.__n][self.__W]

    def MFKnapsack(self, i: int, j: int) -> int:
        """
        Método recursivo utilizado no paradigma de programação dinâmica
        (top-down). Resolve apenas os subproblemas necessários para atingir
        a solução final. A cada chamada recursiva, resolve o problema da mochila
        para i itens e capacidade da mochila j.

        Retorno
        -------
            - max_value (int): Valor total para o problema da mochila com
            i itens e capacidade da mochila j.
        """

        # Verifica se o problema não foi verificado ainda
        # para i itens e capacidade da mochila j
        if self.__F[i][j] < 0:
            # Verifica se o item possui peso que caiba na mochila
            # Caso contrário, não insere o item na mochila e o valor
            # continua sendo o dos itens anteriores que couberam na mochila
            if j < self.__weights[i-1]:
                value = self.MFKnapsack(i-1, j)
            else:
                # Caso a mochila suporte o peso do item, verifica se vale a pena manter
                # a mochila com os itens anteriores ou inserir o item atual na mochila
                value = max(self.MFKnapsack(i-1, j), self.MFKnapsack(i-1, j - self.__weights[i-1]) + self.__values[i-1])
            
            # Atualiza a tabela de memorização com o valor da mochila na posição i,j após as chamadas recursivas
            self.__F[i][j] = value
        
        # Retorna o valor da tabela de memorização na posição i,j,
        # ou seja, a solução para i itens e capacidade de mochila j
        return self.__F[i][j]

    def dynamic_programming_top_down(self) -> tuple[list[int], int]:
        """
        Método que executa o paradigma de programação dinâmica (top-down).
        Utiliza a abordagem de preencher a tabela de memorização de maneira
        recursiva, começando do problema final, e resolvendo apenas os
        subproblemas necessários para atingir essa solução final.

        Retorno
        -------
            - subset_winner (list[int]): Subconjunto de itens selecionados.
            - max_value (int): Valor total dos itens da mochila.
        """

        # Inicializa a tabela de memorização dos valores dos itens
        # F[i][0] e F[0][j] possuem valores iguais a 0 e o restante -1
        self.__F = [[0 if i == 0 or j == 0 else -1 for j in range(self.__W+1)] for i in range(self.__n+1)]

        # Chamada inicial do método recursivo, passando toda a
        # quantidade de itens e toda a capacidade da mochila
        max_value = self.MFKnapsack(self.__n, self.__W)

        return self.search_items_in_table(), max_value

    def greedy(self) -> tuple[list[int], int]:
        """
        Método que executa o paradigma guloso.
        Utiliza a abordagem de a cada iteração, selecionar o item de maior
        valor que caiba na mochila. Essa escolha é irreversível, portanto
        uma vez que não haja itens que caibam na mochila após selecionar o
        de maior valor, o algoritmo para sua execução (e, por isso, não garante
        a solução ótima).

        Retorno
        -------
            - subset_winner (list[int]): Subconjunto de itens selecionados.
            - max_value (int): Valor total dos itens da mochila.
        """

        w = self.__W
        max_value = 0
        subset_winner = []
        
        while True:
            local_max_value = -1
            item = -1
            # Enquanto a capacidade da mochila não for atingida
            # verifica se há itens que caibam nela
            for i in range(self.__n):
                # Verifica se o item possui o maior valor, se cabe na mochila e não está na solução ainda
                if self.__values[i] > local_max_value and self.__weights[i] <= w and i not in subset_winner:
                    local_max_value = self.__values[i]
                    item = i
            
            # Condição de parada: Nenhum item foi encontrado,
            # ou seja, não há itens que caibam na mochila mais
            if local_max_value == -1 and item == -1:
                break
            
            # Adiciona o item selecionado no conjunto-solução
            # Incrementa o valor dos itens selecionados com o valor do novo item
            # Reduz a capacidade da mochila com o peso do novo item após inseri-lo
            subset_winner.append(item)
            max_value += self.__values[item]
            w -= self.__weights[item]
        
        return subset_winner, max_value
    