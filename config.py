DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = '54647135708' # Set this to something random
OTP_SECRET = '90046434246' # Set this to something else random
PAGE_SIZE = 25
SQLALCHEMY_DATABASE_URI  = 'sqlite:////usr/local/slick/slick.db'
#SQLALCHEMY_DATABASE_URI = 'postgresql://slick:slick@localhost/slick'
#SQLALCHEMY_DATABASE_URI = 'mysql://slick:slick@localhost/slick'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')