def pig_it(text):
   
    return {letters: text.count(letters) for letters in text}

print(pig_it('aba'))