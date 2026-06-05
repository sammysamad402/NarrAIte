
def build_prompt(character,history,choice,genre):
    return f'''Genre:{genre}
Character:{character}
History:{history}
Choice:{choice}
Continue the story.'''
