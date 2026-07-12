class Config:
    SECRET_KEY = "Shortener_14"

    SQLALCHEMY_DATABASE_URI = "sqlite:///shortener.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False