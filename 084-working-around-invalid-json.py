>>> import ast
>>> import json
>>> a = "{u'person': u'Julian', u'token': u'abc123'}"
>>> type(a)
<class 'str'>
>>> json.loads(a)
...
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
>>> ast.literal_eval(a)
{'person': 'Julian', 'token': 'abc123'}
>>> b = ast.literal_eval(a)
>>> type(b)
<class 'dict'>
>>> b['token']
'abc123'

# also used in https://github.com/plone/plone.schema/blob/master/plone/schema/jsonfield.py

class JSONField(Field):
    ...
    def fromUnicode(self, value):
        ...
        try:
            v = json.loads(value)
        except JSONDecodeError:
            v = ast.literal_eval(value)