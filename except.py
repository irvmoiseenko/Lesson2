
def ask_user(ask):

    vocabulary = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    if ask in vocabulary.keys():
        print(vocabulary[ask])

ask_user("Что делаешь?")

try:
    while True:
        answer = input('Как дела?: ')
        if answer == 'Хорошо':
            print('а у меня нет')
            break
except KeyboardInterrupt:
    print("Пока!")



