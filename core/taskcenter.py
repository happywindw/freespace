

class TaskCenter(object):
    def __init__(self):
        pass

    def get_movie_rider_tabs(self):
        import random
        tabs = ['o', 'yes', 'environment', 'no', 'how', 'apple', ] * random.randint(1, 20)
        actor = ['1', '23', '9999', '7', '66', '87654321', '000'] * random.randint(1, 20)
        return {'tabs': tabs, 'actor': actor}

    def get_movie_rider_pics(self, num=30):
        import random
        return ['./temp/test.jpg'] * random.randint(1, num)
