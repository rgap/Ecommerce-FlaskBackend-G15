class Config:
    SECRET_KEY = "customsecretkey"
    # db
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/beautipol"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
