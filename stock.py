from trytond.pool import PoolMeta
from trytond.pyson import Eval, Id


class Assign(metaclass=PoolMeta):
    __name__ = 'stock.shipment.assign'

    @classmethod
    def __setup__(cls):
        super(Assign, cls).__setup__()
        invisible_shipment_assign_group = ~Id(
            'stock_assign_group_buttons', 'stock_shipment_assign_group').in_(
            Eval('context', {}).get('groups', []))
        partial_buttons = []
        for btn in cls.partial.buttons:
            if btn.string == 'Ignore':
                if 'invisible' in btn.states:
                    btn.states['invisible'] &= invisible_shipment_assign_group
                else:
                    btn.states['invisible'] = invisible_shipment_assign_group
            partial_buttons.append(btn)
        cls.partial.buttons = partial_buttons
