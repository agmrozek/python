#!/usr/bin/env python

import pickle

"""
Main methods used with pickle module for serialization of objects
pickle.dump()
pickle.dumps()
pickle.load()
pickle.loads()
"""

class example_class:
    a_number = 35
    a_string = "venus"
    a_list = [1,2,3]
    a_dict = {"first": "venus", "last": "mylove"}
    a_tuple = (100,200)

an_object = example_class()

my_pickled_object = pickle.dumps(an_object)   #Pickle takes object and dumps to local disk to preserve for later use
print(f"This is a serialized via pickle object:\n {my_pickled_object}") #Show binary/unreadable local serialied object
 
an_object.a_dict = None   #Change existing object attribute to demonstrate the already serialized object doesn't change

my_unpickled_object = pickle.loads(my_pickled_object)  # De-Serialize the object and see a_dict attribute didnt change
print(f" a_dict of unpickled object: \n {my_unpickled_object.a_dict} \n")

