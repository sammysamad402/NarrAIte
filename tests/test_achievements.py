
from src.game.achievement_system import AchievementManager

def test_achievement():
    a=AchievementManager()
    a.unlock('Explorer')
    assert 'Explorer' in a.get_all()
