
from src.npc.npc import NPC

def test_npc():
    npc=NPC('Elena','Merchant')
    assert npc.name=='Elena'
