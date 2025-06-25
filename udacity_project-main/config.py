import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Flask secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b7d!@Ud4c1tyCMS#2025'

    # Storage account info
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsimages1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'vuB888EcHU4GV1L0xhCsMn4iafotaGXx5IPA8mjQtD3F3MY+utqcW2bLZqdorbcm90QFzp1zmZD7+ASttlBwGw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # SQL Server info
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-sql-server123.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsdb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'Admin1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Lolo1010'
    # SQLAlchemy connection string
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME + '@' + SQL_SERVER + ':'
        + SQL_PASSWORD + '@' + SQL_SERVER
        + ':1433/' + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication (Azure Entra ID)
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'emr8Q~TYGaCA4plZpVqfYM8DGv3lbHiEKnFWXdhm'
    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/2c86bbfc-8d04-41ff-a83a-942f075e0f60"  # Your Tenant ID
    CLIENT_ID = os.environ.get('CLIENT_ID') or "40166806-5f52-4e3d-acc5-3885db607cb6"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
