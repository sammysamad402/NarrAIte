
from src.world.world_generator import WorldGenerator

def test_world():
    w=WorldGenerator().generate_world()
    assert 'kingdom' in w
