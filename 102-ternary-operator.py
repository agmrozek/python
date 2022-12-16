>>> my_list = []
>>> my_list[0] if my_list else None
>>> ret = my_list[0] if my_list else None
>>> ret is None
True
>>> my_list = [1, 2, 3]
>>> ret = my_list[0] if my_list else None
>>> ret
1