>>> number1 = 1000000000
>>> number2 = 1_000_000_000
>>> number3 = 10_00_00_00_00
>>> number1 == number2 == number3
True

# other use case example from PEP 515:
# grouping bits into nibbles in a binary literal
flags = 0b_0011_1111_0100_1110