>>> from decimal import Decimal, localcontext, ROUND_UP
>>> def calculate_revenue(units_sold, price):
...     return units_sold * Decimal(price)
...
>>> calculate_revenue(47, 6.99)
Decimal('328.5300000000000100186525742')  # default 28 places

# use a different precision within the with statement:
>>> with localcontext() as ctx:
...     ctx.prec = 5
...     calculate_revenue(47, 6.99)
...
Decimal('328.53')

# use different precision and rounding
>>> with localcontext() as ctx:
...     ctx.prec = 5
...     ctx.rounding = ROUND_UP
...     calculate_revenue(47, 6.99)
...
Decimal('328.54')

# outside the with block context is restored:
>>> calculate_revenue(47, 6.99)
Decimal('328.5300000000000100186525742')