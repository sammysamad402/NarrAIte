
from src.game.quest_system import Quest, QuestManager

def test_quest():
    qm=QuestManager()
    q=Quest('Find Key','Locate ancient key')
    qm.add_quest(q)
    qm.complete_quest('Find Key')
    assert q.completed
