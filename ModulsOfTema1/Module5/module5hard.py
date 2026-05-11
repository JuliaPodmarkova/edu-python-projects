import hashlib as hl
import time as t

class User:
    def __init__(self, nickname: str, password: hash(int), age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.age == other.age

    def __hash__(self, password):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}, {self.age} лет'

    def __repr__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return f"Video(title{self.title}, duration = {self.duration}, adult_mode={self.adult_mode})"

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(self.password):
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
            print("Ошибка входа: неверный логин или пароль.")

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        for user in self.users:
           if user.nickname == nickname:
               print(f'Пользователь {nickname} уже существует')
               return False
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошёл в систему.")

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_video: str):
        search_video_lower = search_video.lower()
        title = []
        for video in self.videos:
            if search_video.upper() in video.title.upper():
                title.append(video.title)
        return title

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтоб смотреть видео.")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(video.time_now, video.duration):
            print(f"Секунда: {second + 1}")
            t.sleep(1)

        video.time_now = 0
        print("Конец видео")

    def log_out(self):
        self.current_user = None


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
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