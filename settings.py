import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_DICT = {
    'username': 'root',
    'password': 'root123',
    'host': 'localhost',
    'db_name': 'free_space',
    'charset': 'utf8mb4'
}

PICTURE_SIZE = {  # (width, height)
    'rider': (250, 356)
}

PICTURE_GAP = {  # (HGap, VGap)
    'rider': (5, 2)
}
