import sys
from collections import Counter
import matplotlib.pyplot as plt
def plot(filename):
# =============================================================================
#     filename = sys.argv[1]
# =============================================================================
    with open(filename, "r") as f:
        dict_1 = {}
        for line in f:
            try:
                dict_1[line.split(" ")[0]] += 1
            except KeyError:
                dict_1[line.split(" ")[0]] = 1
    [plt.scatter(key,value,c="black") for key, value in (Counter(dict_1.values())).items()]
    axis = plt.axes()
    axis.set_xscale("log")
    axis.set_yscale("log")
    plt.xlabel("node degree for each node protein")
    plt.ylabel("frequency of each node degree")
    plt.title(filename[:-4])
    plt.show()
    
if __name__ == "__main__":
    print(plot("Nitrococcus_mobilis.txt"))