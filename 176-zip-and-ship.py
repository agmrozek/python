# get the code (= adapted script from Tip #83)
$ curl https://gist.githubusercontent.com/pybites/c4b688fdf69a9f517086ac8cb2ba6b61/raw/0fb0c647b3329d8c2d04fbbfa4aa9fd56be5e839/amzlink.py --output amzlink.py

$ mkdir amz
# install required dependency
$ python -m pip install pyperclip --target amz
...

# create an entry point
$ cp amzlink.py amz/__main__.py

# make the zip executable
$ python -m zipapp -p "/usr/bin/env python3" amz -o amzlink

# copy this link to your clipboard:
# https://www.amazon.com/Essentialism-Disciplined-Pursuit-Greg-McKeown/dp/0804137382
# get your affiliation link
$ ./amzlink
# generated link on your clipboard: http://www.amazon.com/dp/0804137382/?tag=pyb0f-20