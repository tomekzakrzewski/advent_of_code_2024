def read_file():
    l = []
    r = []
    with open('input.txt', 'r') as file:
        for line in file:
            txt = line.split()
            l.append(int(txt[0]))
            r.append(int(txt[1]))

    return sorted(l), sorted(r)


def calculate_distances():
    l, r = read_file()
    total_distance = 0

    for i in range(len(l)):
        dist = l[i] - r[i]
        if dist < 0:
            dist = dist * -1
        total_distance += dist

    return total_distance

total = calculate_distances()
print(total)
