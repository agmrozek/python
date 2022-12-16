>>> user_scores = {'bob': '11', 'julian': '22', 'tim': '33', 'sara': '44'}
>>> user_scores.keys()
dict_keys(['bob', 'julian', 'tim', 'sara'])
>>> user_scores.values()
dict_values(['11', '22', '33', '44'])

# in one go using tuple unpacking:
>>> x_axis, y_axis = zip(*user_scores.items())
>>> x_axis
('bob', 'julian', 'tim', 'sara')
>>> y_axis
('11', '22', '33', '44')

# example with a list of 3 item tuples:
>>> x, y, z = zip(*[(i, k, v) for i, (k, v) in
...               enumerate(user_scores.items(), start=1)])
>>> x
(1, 2, 3, 4)
>>> y
('bob', 'julian', 'tim', 'sara')
>>> z
('11', '22', '33', '44')