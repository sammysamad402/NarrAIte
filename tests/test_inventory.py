
from src.game.inventory import Inventory

def test_inventory():
    inv=Inventory()
    inv.add_item('Sword')
    assert 'Sword' in inv.list_items()
