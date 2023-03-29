# This file is part stock_assign_group_buttons module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.transaction import Transaction
from trytond.pool import Pool


class StockAssignGroupButtonsTestCase(ModuleTestCase):
    'Test Stock Assign Group Buttons module'
    module = 'stock_assign_group_buttons'

    @with_transaction()
    def test_stock_assign_group_buttons(self):
        Assign = Pool().get('stock.shipment.assign', type='wizard')
        btn_ignore, = [btn for btn in Assign.partial.buttons if btn.string == 'Ignore']
        assert str(btn_ignore.states) == "{'invisible': Not(In(Id('stock_assign_group_buttons', 'stock_shipment_assign_group'), Get(Eval('context', {}), 'groups', [])))}"

del ModuleTestCase
