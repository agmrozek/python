$ more script.py
def func():
    print("Hello from function")


if __name__ == "__main__":
    func()

# main block gets invoked

$ python script.py
Hello from function

$ python
>>> import script  # main block does not get invoked
>>> script.func()
Hello from function