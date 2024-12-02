def read_file():
    l = []
    r = []
    with open('input.txt', 'r') as file:
        for line in file:
            txt = line.split()
            l.append(int(txt[0]))
            r.append(int(txt[1]))

    return l, r

def calculate_similarity():
    l, r = read_file()
    hm = {}
    for i in l:
        if i not in hm.keys() and i in r:
            hm[i] = r.count(i)
   
    similarity = 0
    for i in hm.items():
        s = i[0] * i[1]
        similarity += s

    return similarity
    


print(calculate_similarity())
