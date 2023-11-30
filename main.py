import random
def game():
    words = ['anor', 'olma', 'shaftoli', 'dars', 'kitob', 'dushman', 'maktab', 'universitet', 'familya', 'matematika']

    playAgain = True

    word = random.choice(words)
    massiv = []
    count = 0
    result_text = ''
    for i in word:
        massiv.append('_')

    def isWin():
        return '_' in massiv

    def show_status():
        result_text = ''
        for i in massiv:
            result_text += i
            result_text += ' '
        print(result_text)
        print("")

    show_status()
    i = 0
    while playAgain:
        if isWin():
            input_letter = input('kiriting=')
            if input_letter in word:
                for i in range(0, len(word)):
                    if word[i] == input_letter:
                        massiv[i] = input_letter
                show_status()
            else:
                print('hato')
                count += 1
                if count >= 4:
                    print('siz yutqazdingiz')
                    user_want = input("yana o'ynashni xoxlaysizmi?  y=>ha  n=>yoq=> ")
                    if user_want == 'y':
                        game()
                    elif user_want == 'n':
                        print("o'yin uchun raxmat")
                        break

                else:
                    print(f"sizda {4 - count} ta imkoniyat qoldi")
                show_status()
        else:
            print('siz yutdingiz. ')
            user_want = input("yana o'ynashni xoxlaysizmi?  y=>ha  n=>yoq=> ")
            if user_want == 'y':
                game()
            elif user_want == 'n':
                print("o'yin uchun raxmat")
                break



game()