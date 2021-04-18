'''
Module for coding encoding string into
'''


# def to_ascii_list(word):
#     move = 22.5

#     final_ascii_list = []
#     for char in word:
#         ascii_list = list(hex(ord(char))[2:])
#         res = []

#         for num in ascii_list:
            
#             try:
#                 res.append(int(num))
#             except ValueError:
#                 if num == 'a':
#                     res.append(10)
#                 if num == 'b':
#                     res.append(11)
#                 if num == 'c':
#                     res.append(12)
#                 if num == 'd':
#                     res.append(13)
#                 if num == 'e':
#                     res.append(14)
#                 if num == 'f':
#                     res.append(15)
#         final_ascii_list.append(res) 
#     flattened_lst = [move*item for sublist in final_ascii_list for item in sublist]
#     return flattened_lst

# a = to_ascii_list('hello')



# for i in a:
#     print(i)
# print()

# coordinates = []

# coordinates.append(a[0])


# for position in range(0, len(a)-1):
#     if a[position+1]-a[position] == 0.0:
#         coordinates.append(360.0)
#     else:
#         coordinates.append(a[position+1]-a[position])

# print(coordinates)


# "hello" [135.0, 45.0, -45.0, -22.5, 22.5, 135.0, -135.0, 135.0, -135.0, 202.5]
# "1 січня" [67.5, -45.0, 22.5, -45.0, 90.0, 360.0, -67.5, 67.5, 22.5, 22.5, -45.0, 360.0, 67.5, -67.5, -22.5, 225.0, -202.5, 360.0, 247.5]
#           [67.5, -45.0, 22.5, -45.0, 90.0, 360.0, -67.5, 67.5, 22.5, 22.5, -45.0, 360.0, 67.5, -67.5, -22.5, 225.0, -202.5, 360.0, 247.5]


class AngleADT:

    def __init__(self):
        pass


    @staticmethod
    def to_ascii_list(word):
        move = 22.5

        final_ascii_list = []
        for char in word:
            ascii_list = list(hex(ord(char))[2:])
            res = []

            for num in ascii_list:
                
                try:
                    res.append(int(num))
                except ValueError:
                    if num == 'a':
                        res.append(10)
                    if num == 'b':
                        res.append(11)
                    if num == 'c':
                        res.append(12)
                    if num == 'd':
                        res.append(13)
                    if num == 'e':
                        res.append(14)
                    if num == 'f':
                        res.append(15)
            final_ascii_list.append(res) 
        flattened_lst = [move*item for sublist in final_ascii_list for item in sublist]
        return flattened_lst

    @staticmethod
    def encode_message(message):
        ascii_list = AngleADT.to_ascii_list(message)
        coordinates = []

        coordinates.append(ascii_list[0])


        for position in range(0, len(ascii_list)-1):
            if ascii_list[position+1] - ascii_list[position] == 0.0:
                coordinates.append(360.0)
            else:
                coordinates.append(ascii_list[position+1] - ascii_list[position])

        return coordinates


print(AngleADT.encode_message('1 січня'))




