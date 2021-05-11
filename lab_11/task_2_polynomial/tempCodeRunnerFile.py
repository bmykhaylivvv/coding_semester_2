data_file = open("data2.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly2._append_term(float(degree), float(coefficient))