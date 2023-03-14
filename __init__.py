# This file is part stock_assign_group_buttons module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import stock

def register():
    Pool.register(
        stock.Assign,
        module='stock_assign_group_buttons', type_='wizard')
