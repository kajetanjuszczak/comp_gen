def lines(filename):
    with open(filename, "r") as f:
        list_of_prot = []
        for lines in f:
            if lines.startswith("."):
                list_of_prot.append((lines.split("|")[4]).split("_")[0])
    return list_of_prot
def checkoverlap(filename, filename2):
    list_of_prot = lines(filename)
    with open(filename2, "r") as f:
        list_of_symbols = []
        for line in f:
            list_of_symbols.append((line.rstrip()).split(" "))
    list_of_overlaps = []
    for line in list_of_symbols:
        list_of_overlaps.append(len(set(list_of_prot).intersection(line)))
    print("1st best overlap: {} with overlap lenght of {}".format(list_of_symbols[list_of_overlaps.index(max(list_of_overlaps))], max(list_of_overlaps)))
    list_of_overlaps[list_of_overlaps.index(max(list_of_overlaps))] = 0
    print("2nd best overlap: {} with overlap lenght of {}".format(list_of_symbols[list_of_overlaps.index(max(list_of_overlaps))], max(list_of_overlaps)))

if __name__ == "__main__":
# =============================================================================
#     print(lines("lab8blast"))
# =============================================================================
    print(checkoverlap("lab8blast","experiments.txt"))