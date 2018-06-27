

class TaskCenter(object):
    def __init__(self):
        # self.movie_task = MovieTask()
        pass


class MovieTask(TaskCenter):
    def __init__(self):
        super().__init__()
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

    def get_movie_rider_pics(self, filter_dict, pics_num, start_num=0):
        import random
        return [('sss', './temp/test.jpg')] * random.randint(1, pics_num * 5)
