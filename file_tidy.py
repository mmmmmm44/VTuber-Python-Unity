# file tidying
# obsoleted

filename = "model.txt"

list_points = []

with open(filename) as file:
    for line in file:
        # print(line)

        line_arr = line.split()

        for pt in line_arr[1:]:
            list_points.append(pt)

print(list_points)

with open("model_tidied.txt", "w") as file:
    for pt in list_points:
        file.write(pt + "\n")
