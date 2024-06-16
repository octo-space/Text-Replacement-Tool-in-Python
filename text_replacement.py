def replaceWord():
    #Example text
    text = "The sun was setting over the ocean as I walked along the beach. The warm sand felt soft between my toes as I searched for interesting shells. The sound of the waves crashing against the shore was soothing, and I felt my worries slowly draining away. As I strolled, I noticed a few seagulls flying overhead, and I couldn't help but smile at their playful cries."

    exist_word = input('Which Word Do you want to replace: ')
    new_word = input('Give me the New Word: ')

    if exist_word in text:
        # Assign the result of text.replace() back to text
        text = text.replace(exist_word, new_word)
        print(text)
    else:
        print('Error')

replaceWord()
