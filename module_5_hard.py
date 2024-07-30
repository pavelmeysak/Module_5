import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __repr__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        else:
            return self.nickname == other

    def __contains__(self, item):
        return self.nickname == item


class Video:
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration, **kwargs):
        for keys, values in kwargs.items():
            setattr(self, keys, values)
        self.title = title
        self.duration = duration

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        else:
            return self.title == other

    def __contains__(self, item):
        return self.title == item

    def __repr__(self):
        return f'{self.title}'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = "None"

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i and hash(password) == i.password:
                self.current_user = i
                break
            else:
                print('Пользователь не найден. Пожалуйста, зарегистрируйтесь')

    def register(self, nickname, password, age):
        if self.users.__contains__(nickname):
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = User(nickname, password, age)

    def log_out(self):
        self.current_user = "None"

    def add(self, *args):
        for i in args:
            if not self.videos.__contains__(i):
                self.videos.append(i)
            else:
                break

    def get_videos(self, search_req):
        search_list = []
        for i in range(0, len(self.videos)):
            if self.videos[i].title.lower().__contains__(search_req.lower()):
                search_list.append(self.videos[i].title)
        return search_list

    def watch_video(self, title):
        if self.current_user == "None":
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for j in range(0, len(ur.videos)):
                if ur.videos[j].__contains__(title):
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(0, ur.videos[j].duration + 1):
                            ur.videos[j].time_now = i
                            print(ur.videos[j].time_now)
                            time.sleep(1)
                        print("Конец видео")
                        ur.videos[j].time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
