import os
from PIL import Image
from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos


def get_resize_picture(direction, size, pic_file):
    """
    resize and cut a picture that matches the given direction and size
    :param direction: left or right
    :param size: cut size
    :param pic_file: picture file
    :return:
    """
    if not os.path.exists(pic_file):
        return
    im = Image.open(pic_file)
    pic_size = im.size
    res_img = im.resize((int(size[1] / pic_size[1] * pic_size[0]), size[1]), Image.ANTIALIAS)
    if direction == 'left':
        region = (0, 0, size[0], size[1])
        res_img = res_img.crop(region)
    return res_img


def get_duration_definition(video_name):
    """
    获取视频时长与清晰度
    :param video_name:
    :return:
    """
    video_info = ffmpeg_parse_infos(video_name)
    duration = int(video_info['duration'])   # unit second
    video_size = video_info['video_size']
    return duration, video_size

