import sys, random

def generate_tests(n: int) -> list[str]:
    data = []

    W = random.randint(10, 100)
    data.append("{}\n".format(W))
    
    for i in range(n):
        w_i = random.randint(1, W)
        v_i = random.randint(10, 100)
        data.append("{} {}\n".format(w_i, v_i))
    
    return data

if __name__ == "__main__":
    for i in range(1, 1000):
        out_file = open("tests/test_{}.txt".format(i), "w")
        out_file.writelines(generate_tests(i))
        out_file.close()
