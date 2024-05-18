from config import Config
from bot.tg import TGBot
from cnn.model import Model

if __name__ == '__main__':
    model = Model(
        path_to_model=Config.PATH_TO_MODEL,
        img_height=Config.IMG_HEIGHT,
        img_width=Config.IMG_WIDTH,
    )

    Tele = TGBot(Config.BOT_TOKEN, model)
    Tele.run()
