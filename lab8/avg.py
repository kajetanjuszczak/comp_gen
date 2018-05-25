import sys
def average(filename):
    filename = sys.argv[1]
    with open(filename, "r") as f:
        set_of_id = set()
        count = 0
        for line in f:
            set_of_id.add(line.split(" ")[0])
            count +=1
        avg = count / len(set_of_id) 
        return avg
    
if __name__ == "__main__":
    print(average("Nitrococcus_mobilis.txt"))