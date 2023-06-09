import matplotlib.pyplot as plt

paradigms = {
    1: "Força-Bruta",
    2: "Busca Exaustiva",
    3: "Backtracking",
    4: "Programação Dinâmica - Bottom up",
    5: "Programação Dinâmica - Top down",
    6: "Guloso"
}

for key, value in paradigms.items():
    input_file = open("outputs/{}_analysis.txt".format(key), "r")
    lines = input_file.readlines()
    if key == 1:
        x = []
        y = []
        y_n = []
        for line in lines:
            data = line.replace("\n", "").split(": ")
            x.append(int(data[0]))
            y_n.append(pow(2, int(data[0])))
            y.append(int(data[1]))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        plt.ylim(min(y), max(y))
        ax.plot(x, y, label="Algoritmo")
        ax.plot(x, y_n, '-.', label="2^n")

        ax.set(xlabel='n', ylabel='2^n', title=value)
        plt.legend()
        ax.grid()

        fig.savefig("graphs/Gráfico {}.png".format(value))
        plt.show()
    elif key == 2:
        x = []
        y = []
        y_n = []
        for line in lines:
            data = line.replace("\n", "").split(": ")
            x.append(int(data[0]))
            y_n.append(pow(2, int(data[0])))
            y.append(int(data[1]))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, label="Algoritmo")
        ax.plot(x, y_n, '-.', label="2^n")

        ax.set(xlabel='n', ylabel='2^n', title=value)
        plt.legend()
        ax.grid()

        fig.savefig("graphs/Gráfico {}.png".format(value))
        plt.show()
    elif key == 3:
        x = []
        y = []
        y_n = []
        for line in lines:
            data = line.replace("\n", "").split(": ")
            x.append(int(data[0]))
            y_n.append(pow(2, int(data[0])))
            y.append(int(data[1]))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        plt.ylim(min(y), max(y))
        ax.plot(x, y, label="Algoritmo")
        ax.plot(x, y_n, '-.', label="2^n")

        ax.set(xlabel='n', ylabel='2^n', title=value)
        plt.legend()
        ax.grid()

        fig.savefig("graphs/Gráfico {}.png".format(value))
        plt.show()
    elif key == 4:
        x = []
        y = []
        z = []
        z_n = []
        for line in lines:
            data = line.replace("\n", "").split(": ")
            x_axis = data[0].split("x")
            x.append(int(x_axis[0]))
            y.append(int(x_axis[1]))
            z_n.append(int(x_axis[0])*int(x_axis[1]))
            z.append(int(data[1]))
        
        ax = plt.figure().add_subplot(projection='3d')
        ax.plot(x, y, z, label="Algoritmo")
        ax.plot(x, y, z_n, '-.', label="n*W")

        ax.set(xlabel='n', ylabel='W', zlabel='n*W', title=value)
        plt.legend()

        plt.savefig("graphs/Gráfico {}.png".format(value))
        plt.show()
    elif key == 5:
        x = []
        y = []
        z = []
        z_n = []
        for line in lines:
            data = line.replace("\n", "").split(": ")
            x_axis = data[0].split("x")
            x.append(int(x_axis[0]))
            y.append(int(x_axis[1]))
            z_n.append(int(x_axis[0])*int(x_axis[1]))
            z.append(int(data[1]))
        
        ax = plt.figure().add_subplot(projection='3d')
        ax.plot(x, y, z, label="Algoritmo")
        ax.plot(x, y, z_n, '-.', label="n*W")

        ax.set(xlabel='n', ylabel='W', zlabel='n*W', title=value)
        plt.legend()

        plt.savefig("graphs/Gráfico {}.png".format(value))
        plt.show()
    elif key == 6:
        x = []
        y = []
        y_n = []
        for line in lines:
            data = line.replace("\n", "").split(": ")
            x.append(int(data[0]))
            y_n.append(int(data[0])*int(data[0]))
            y.append(int(data[1]))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, label="Algoritmo")
        ax.plot(x, y_n, '-.', label="n^2")

        ax.set(xlabel='n', ylabel='n^2', title=value)
        plt.legend()
        ax.grid()

        fig.savefig("graphs/Gráfico {}.png".format(value))
        plt.show()