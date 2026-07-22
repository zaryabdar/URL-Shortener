class Config:
    SECRET_KEY = "Shortener_14"

    SQLALCHEMY_DATABASE_URI = "sqlite:///shortener.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = "zdar2005@gmail.com"
    MAIL_PASSWORD = "gnwwkdzmmwodsgcn"