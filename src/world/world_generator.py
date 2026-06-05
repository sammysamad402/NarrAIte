
import random

class WorldGenerator:
    def generate_world(self):
        return {
            "kingdom": random.choice(["Aetheria","Drakoria","Lumina"]),
            "city": random.choice(["Ironhold","Moonhaven","Silverkeep"]),
            "region": random.choice(["Northlands","Shadow Woods","Crystal Plains"])
        }
