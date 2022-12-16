$ cat MOCK_DATA.json
[{"id":1,"first_name":"Myrle","email":"mleport0@t.co"},
{"id":2,"first_name":"Lynnette","email":"lchurchward1@seattletimes.com"}]

$ python -m json.tool MOCK_DATA.json
[
    {
        "id": 1,
        "first_name": "Myrle",
        "email": "mleport0@t.co"
    },
    {
        "id": 2,
        "first_name": "Lynnette",
        "email": "lchurchward1@seattletimes.com"
    }
]

# validation error

$ echo '[{id: 1}]' | python -m json.tool
Expecting property name enclosed in double quotes: line 1 column 3 (char 2)