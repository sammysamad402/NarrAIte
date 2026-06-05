
from src.analytics.story_metrics import StoryMetrics

def test_metrics():
    m=StoryMetrics()
    m.update('hello world')
    assert m.summary()['words']==2
