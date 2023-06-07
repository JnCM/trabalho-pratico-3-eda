import sys
from Knapsack import Knapsack

def read_file(filename: str) -> tuple[int, int, list, list]:
    input_file = open(filename, "r")
    lines = input_file.readlines()

    n = 0
    weights = []
    values = []
    for line in lines:
        if n == 0:
            W = int(line.replace("\n", ""))
        else:
            w_v = line.replace("\n", "").split(" ")
            weights.append(int(w_v[0]))
            values.append(int(w_v[1]))
        n += 1
    
    return W, n-1, weights, values

if __name__ == "__main__":
    filename = sys.argv[1]
    opt = int(sys.argv[2])

    W, n, weights, values = read_file(filename)
    knapsack = Knapsack(W, n, weights, values)
    
    if opt == 2:
        print("================= Busca Exaustiva ==================")
        subset, value = knapsack.exaustive_search()
        print("Item(ns) selecionado(s): {}".format(subset))
        print("Valor total do(s) item(ns): {}".format(value))
    elif opt == 4:
        print("========= Programação dinâmica - Bottom up =========")
        subset, value = knapsack.dynamic_programming_bottom_up()
        print("Item(ns) selecionado(s): {}".format(subset))
        print("Valor total do(s) item(ns): {}".format(value))
    elif opt == 5:
        print("========= Programação dinâmica - Top down ==========")
        subset, value = knapsack.dynamic_programming_top_down()
        print("Item(ns) selecionado(s): {}".format(subset))
        print("Valor total do(s) item(ns): {}".format(value))
    elif opt == 6:
        print("===================== Guloso =======================")
        subset, value = knapsack.greedy()
        print("Item(ns) selecionado(s): {}".format(subset))
        print("Valor total do(s) item(ns): {}".format(value))
