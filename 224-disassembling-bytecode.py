>>> def hello(name=None):
...     name = 'Stranger' if name is None else name
...     return f"Hello {name}"
...
>>> import dis
>>> dis.dis(hello)
  2           0 LOAD_FAST                0 (name)
              2 LOAD_CONST               0 (None)
              4 IS_OP                    0
              6 POP_JUMP_IF_FALSE       12
              8 LOAD_CONST               1 ('Stranger')
             10 JUMP_FORWARD             2 (to 14)
        >>   12 LOAD_FAST                0 (name)
        >>   14 STORE_FAST               0 (name)

  3          16 LOAD_CONST               2 ('Hello ')
             18 LOAD_FAST                0 (name)
             20 FORMAT_VALUE             0
             22 BUILD_STRING             2
             24 RETURN_VALUE
>>> list(hello.__code__.co_code)
[124, 0, 100, 0, 117, 0, 114, 12, 100, 1, 110, ...]
>>> dis.opname[124]
'LOAD_FAST'