from .prompt_builder import build_prompt

class StoryEngine:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)

    def next_chapter(self, character, history, choice, genre):
        prompt = build_prompt(
            character,
            history,
            choice,
            genre
        )

        return self.provider.generate(prompt)