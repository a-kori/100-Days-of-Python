# Retrieves letters and special characters (symbols) from the ASCII table, 
# generates a string list of digits 0 to 9
import string
from itertools import chain

letters = string.ascii_letters
numbers = [str(x) for x in range(0, 10)]
symbols = [chr(i) for i in chain(range(33, 48), range(58, 65), range(91, 97), range(123, 127))]
