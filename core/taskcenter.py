

class TaskCenter(object):
    def __init__(self):
        self.movie_task = MovieTask()


class MovieTask(object):
    def __init__(self):
        pass

    def get_movie_rider_tabs(self, tab_name):
        import random
        if tab_name == 'tabs':
            tl = ['o', 'yes', 'environment', 'no', 'how', 'apple', ] * random.randint(1, 20)
        elif tab_name == 'actor':
            tl = ['1', '23', '9999', '7', '66', '87654321', '000'] * random.randint(1, 20)
        else:
            tl = []
        if tab_name != 'tabs':
            tl.insert(0, 'All')
        return tl

    def get_movie_rider_pics(self, filter_dict, start=0, num=30):
        import random
        return [('sss', './temp/test.jpg')] * random.randint(1, num)
