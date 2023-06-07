import sys, random

def generate_tests() -> list[str]:
    data = []

    W = random.randint(10, 100)
    data.append("{}\n".format(W))
    
    n = random.randint(3, 10)
    for i in range(n):
        w_i = random.randint(1, W)
        v_i = random.randint(10, 70)
        data.append("{} {}\n".format(w_i, v_i))
    
    return data

if __name__ == "__main__":
    for i in range(1, 101):
        out_file = open("tests/test_{}.txt".format(i), "w")
        out_file.writelines(generate_tests())
        out_file.close()
