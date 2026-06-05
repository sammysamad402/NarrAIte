from .base_provider import BaseProvider

class OfflineProvider(BaseProvider):

    def generate(self, prompt):
        return f'Offline Story:\n{prompt[:300]}'