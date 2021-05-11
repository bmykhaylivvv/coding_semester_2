from polynomial import Polynomial

poly1 = Polynomial()
poly2 = Polynomial()

data_file = open("data1.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly1._append_term(float(degree), float(coefficient))

data_file = open("data2.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly2._append_term(float(degree), float(coefficient))

#print(poly1)
#print(poly2)


print(poly1.degree())
print(poly2.degree())

print(poly1[2.0])

new_p = poly1 + poly2
print(new_p[3.0], new_p[2.0],new_p[1.0],new_p[0.0])

print(poly1 + poly2)
print(poly1 - poly2)
print(poly1 * poly2)


poly1 = Polynomial()

poly1._append_term(19, 10)
poly1._append_term(7, 2)
poly1._append_term(4, 1)
poly1._append_term(3, 3)



poly2 = Polynomial()

poly2._append_term(10, 9)
poly2._append_term(4, 2)
poly2._append_term(3, 5)
poly2._append_term(2, 2)

poly3 = poly1 + poly2
poly4 = poly1 - poly2
poly5 = poly1 * poly2
 

print(poly1)
print(poly2)
print(poly3)
print(poly4)
print(poly5)