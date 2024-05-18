import telebot
import os


class TGBot:
    def __init__(self, token, model=None):
        self.token = token
        self.model = model
        self.bot = telebot.TeleBot(self.token)

        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.bot.send_message(
                message.chat.id,
                "Отправьте фотографию"
            )

        @self.bot.message_handler(content_types=['photo'])
        def load_img(message):
            user_id = message.from_user.id
            user_dir = str(user_id)
            if not os.path.exists(user_dir):
                os.makedirs(user_dir)
            file_id = message.photo[-1].file_id
            file_info = self.bot.get_file(file_id)
            file_path = file_info.file_path
            downloaded_file = self.bot.download_file(file_path)
            with open(os.path.join(user_dir, 'photo.jpg'), 'wb') as new_file:
                new_file.write(downloaded_file)
            score = self.model.predict(os.path.join(user_dir, 'photo.jpg'))
            self.bot.send_message(
                message.chat.id,
                str(score)
            )

    def run(self):
        self.bot.polling()
