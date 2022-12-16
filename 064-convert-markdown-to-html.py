(venv) $ pip install markdown  

# which creates this console entry script: venv/bin/markdown_py

(venv) $ markdown_py -h
Usage: markdown_py [options] [INPUTFILE]
       (STDIN is assumed if no INPUTFILE is given)

# let's try an example doc

(venv) $ more doc.md
## pybites
this is some markdown
here is a [link](http://example.com).

# bounce html to standard output

(venv) $ markdown_py < doc.md
<h2>pybites</h2>
<p>this is some markdown</p>
<p>here is a <a href="http://example.com">link</a>.</p>

# or save it to a file

(venv) $ markdown_py < doc.md > doc.html