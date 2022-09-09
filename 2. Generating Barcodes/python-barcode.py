from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcodes = int(input("How many barcodes do you want to generate? "))
numbers = range(num_of_barcodes)

for i in numbers:
    id = 0
    while id < 100000000000 or id >= 1000000000000:
        id = int(input("Give a 12-digit number to convert into barcode: "))
    idString = str(id)
    my_barcode = EAN13(idString, writer=ImageWriter)
    filename = input("Filename: ")
    my_barcode.save(filename)