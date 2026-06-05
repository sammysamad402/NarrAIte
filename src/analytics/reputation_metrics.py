
class ReputationMetrics:
    def summarize(self,reputation):
        return {
            'factions': len(reputation),
            'total_reputation': sum(reputation.values())
        }
