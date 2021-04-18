'''
Module for testing zip quality of lzw_compression() method.
'''


from grayscale_adt import GrayscaleImage


def compression_test(path):
    '''
    Function for testing compression.
    '''
    img1 = GrayscaleImage()
    img1.from_file(path)

    print('\033[1mCompressing ...\033[0m')
    img1.lzw_compression()

    print('↓↓↓')

    print('\033[1mDecompressing ...\033[0m')
    img1.lzw_decompression()

    print()
    print('\033[1mCheck if image before compression is identical to image after compression.\
\033[0m')
    res = []
    for row in range(img1.height):
        for col in range(img1.width):
            # print(img1.image[row, col], img1.decompressed_image[row, col])
            res.append(img1.image[row, col] ==
                       img1.decompressed_image[row, col])

    # Check whether before and after compressing images are the same
    print(f'\033[1mResult:\033[0m {all(res)}')

    print()
    print('Size of image BEFORE compressing: ')
    print('\033[1m' + str(len(img1.before_compress_string)) + '\033[0m')

    print('Size of image AFTER compressing: ')
    print('\033[1m' + str(len(img1.after_compress_string)) + '\033[0m')

    print()

    print('Coefficient of compression: ')
    print('\033[1m' + str(round((len(img1.before_compress_string) /
                                 len(img1.after_compress_string)), 1)) + '\033[0m')


def main():
    '''
    Main function for test image compression.
    '''
    print('Enter file name fith extesion: ')
    path = input('> ')
    print()
    compression_test(path)


if __name__ == "__main__":
    main()
