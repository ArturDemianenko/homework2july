# import googletrans

# TRANSLATOR = googletrans.Translator()

# def translate_game():
#     with open('my_file_translate_game.txt', mode = 'w') as my_file:
#         my_file.write("""Моя улюблена гра це тягати залізо у залі""")
#     with open('my_file_translate_game.txt', mode = 'r') as my_file:
#         my_file = TRANSLATOR.translate(my_file.readlines() , dest='uk')
#         for row in my_file:
#             print(row.text)
# translate_game()



# from googletrans import Translator

# TRANSLATOR = Translator()

# a = TRANSLATOR.translate('I play a game called gym', src='en',dest='uk')

# print(a.text)




import googletrans

TRANSLATOR = googletrans.Translator()

def translate1():
    test = TRANSLATOR.translate("I play a game called gym", src='en', dest='uk')

    print(test.text)


# translate1()

def with_file_opening():
    with open("translate.txt", mode="r") as file:
        test = TRANSLATOR.translate(file.readlines(), dest='uk')
        
    for line in test:
        print(f'{line.origin} -> {line.text}')


with_file_opening()