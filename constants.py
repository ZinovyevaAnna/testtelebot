START_GREETING = 'Привет!'
WHAT_TO_DO_FIRST = 'С чего начнём?'
WHAT_TO_DO_LIST = ['Что теперь?', 'А теперь?', 'Куда сейчас?', 'Что дальше?', 'Следующий шаг?']
HELLO_STICKER_ID = 'CAACAgIAAxkBAAElIgVk4R0GA_kn4ncaw4uKRc4CiJgysQACLgADJHFiGojoNkNqQEMUMAQ'

ASK_TO_SHOW_PICS = 'Покажи фото'
ASK_WHICH_PIC = 'Какую хочешь увидеть?\n' \
                'P.S. Фотографироваться я не люблю'
ASK_TO_TELL_SMT = 'Расскажи мне что-нибудь'
TELL_ME_DESC_LIST = 'Могу спеть, могу на кофейной гуще погадать!\n' \
                    'Шучу...\n' \
                    'Выбирай из того, что есть 👀'.split('\n')
ASK_FOR_LOVE_STORY = 'Историю любви'
ABOUT_GPT = 'Внучок, что такое GPT? 👵'
ABOUT_SQL_NOSQL = 'Лучше про NoSQL давай'
ABOUT_HOBBY = 'Хочу послушать про хобби'
ASK_FOR_REPO_LINK = 'Ссылка на код'
ASK_FOR_FINISH = 'Пока-пока'

WRONG_COMMAND = 'Я не понимаю :(\nдавай по-другому?'
FINAL_GREETING = 'До встречи!'

MAIN_COMMANDS_LIST = [ASK_TO_SHOW_PICS, ASK_TO_TELL_SMT, ASK_FOR_REPO_LINK, ASK_FOR_FINISH]
STORY_LIST = [ASK_FOR_LOVE_STORY, ABOUT_GPT, ABOUT_SQL_NOSQL, ABOUT_HOBBY]


def _read_helper(path, mode='rb'):
    with open(path, mode) as file:
        return file.read()


SELFIE_PHOTO = _read_helper('files/selfie.jpg')
CHILD_PHOTO = _read_helper('files/child.jpg')
GPT_VOICE = _read_helper('files/about_gpt.ogg')
SQL_NOSQL_VOICE = _read_helper('files/about_sql_nosql.ogg')
LOVE_STORY = _read_helper('files/love_story.in')
HOBBY_POST = _read_helper('files/hobby_post.in')
