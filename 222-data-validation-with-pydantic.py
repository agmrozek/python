>>> from datetime import datetime
>>> from typing import Optional
>>> from pydantic import BaseModel, EmailStr  # pip install pydantic[email]
>>> class User(BaseModel):
...     id: int
...     username: str
...     email: EmailStr
...     added: Optional[datetime] = datetime.now()
...
>>> User(id=1, username='pybob', email='bob@pybit.es')
User(id=1, username='pybob', email='bob@pybit.es', added=datetime.datetime(2020, 12, 30, 9, 42, 6, 570021))
>>> User(id=2, username='pybob')
Traceback (most recent call last):
...
pydantic.error_wrappers.ValidationError: 1 validation error for User
email
  field required (type=value_error.missing)
>>> User(id=2, username='pybob', email='pybit.es')
...
pydantic.error_wrappers.ValidationError: 1 validation error for User
email
  value is not a valid email address (type=value_error.email)
>>> User(id=2, username='pybob', email='bob@pybit.es')
User(id=2, username='pybob', email='bob@pybit.es', added=datetime.datetime(2020, 12, 30, 9, 42, 6, 570021))