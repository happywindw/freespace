import math


class TaskCenter(object):
    def __init__(self):
        # self.movie_task = MovieTask()
        pass


class MovieTask(TaskCenter):
    def __init__(self):
        super().__init__()
        import random
        # self.ml = [('sss', './temp/test.jpg')] * random.randint(1, 30 * 5)
        num = random.randint(0, 200)
        i = 0
        self.ml = []
        while i < num:
            self.ml.append(('S' + str(i), './temp/test.jpg'))
            i += 1
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

    def get_movie_rider_pics(self, filter_dict, pics_per_page, current_page=0):
        return len(self.ml), math.ceil(len(self.ml) / pics_per_page), \
               self.ml[(current_page-1) * pics_per_page: (current_page-1) * pics_per_page + pics_per_page]
