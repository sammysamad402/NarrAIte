
from src.ai.offline_provider import OfflineProvider
from src.core.story_engine import StoryEngine
def test_story():
    assert 'Offline' in StoryEngine(OfflineProvider()).generate('hello')
