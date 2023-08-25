from ctypes import CDLL

so_file = "./functions.so"
my_functions = CDLL(so_file)

print(my_functions.square(10))

