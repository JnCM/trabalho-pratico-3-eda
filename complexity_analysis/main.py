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
    options = [1,2,3,4,5,6]

    for opt in options:
        output_file = open("outputs/{}_analysis.txt".format(opt), "w")
        for i in range(1, 1000):
            filename = "tests/test_{}.txt".format(i)
            W, n, weights, values = read_file(filename)
            knapsack = Knapsack(W, n, weights, values)
            if opt == 1:
                if n > 110:
                    break
                print("Força-bruta: {}".format(n))
                value, count_ops = knapsack.brute_force()
                output_file.write("{}: {}\n".format(n, count_ops))
            elif opt == 2:
                if n > 25:
                    break
                print("Busca Exaustiva: {}".format(n))
                subset, value, count_ops = knapsack.exaustive_search()
                output_file.write("{}: {}\n".format(n, count_ops))
            elif opt == 3:
                if n > 100:
                    break
                print("Backtracking: {}".format(n))
                value, count_ops = knapsack.backtracking()
                output_file.write("{}: {}\n".format(n, count_ops))
            elif opt == 4:
                print("Programação dinâmica - Bottom up: {}".format(n))
                subset, value, count_ops = knapsack.dynamic_programming_bottom_up()
                output_file.write("{}x{}: {}\n".format(n, W, count_ops))
            elif opt == 5:
                print("Programação dinâmica - Top down: {}".format(n))
                subset, value, count_ops = knapsack.dynamic_programming_top_down()
                output_file.write("{}x{}: {}\n".format(n, W, count_ops))
            elif opt == 6:
                print("Guloso: {}".format(n))
                subset, value, count_ops = knapsack.greedy()
                output_file.write("{}: {}\n".format(n, count_ops))
        output_file.close()
