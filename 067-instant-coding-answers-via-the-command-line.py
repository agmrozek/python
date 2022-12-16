$ mkdir ~/howdoi && cd $_
$ python -m venv venv && source venv/bin/activate
(venv) $ pip install howdoi

# I made a useful alias (you could also use vim-howdoi)
$ alias howdoi
alias howdoi='source $HOME/howdoi/venv/bin/activate && howdoi'

# enjoy!
$ howdoi zip enumerate
for index, (value1, value2) in enumerate(zip(data1, data2)):
    ...

$ howdoi argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a")
…

# or just get (and open) the link to the answer / code
$ howdoi decorator -l
https://stackoverflow.com/questions/2435764/how-to-differentiate-between-method-and-function-in-a-decorator
$ open `howdoi decorator -l`