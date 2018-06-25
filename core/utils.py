import os
import wx
from PIL import Image
from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos


def get_fitted_bitmap(pic, size, direction='center'):
    """
    Resize the picture so that it can fit the given size and then return a wx.Bitmap object with the fitted picture.
    :param pic: the picture location
    :param size: resize size
    :param direction: crop the picture from the given direction while the picture size out of the given size,
    the direction should only be one of 'center', 'left', 'right', 'top' and 'bottom'.
    :return: return a wx.Bitmap object with the fitted picture
    """
    if not os.path.exists(pic):
        raise FileNotFoundError

    img = wx.Image(pic)
    ogl_size = img.GetSize()
    if ogl_size[0] / size[0] < ogl_size[1] / size[1]:
        img = img.Scale(size[0], int(ogl_size[1] * size[0] / ogl_size[0]), wx.IMAGE_QUALITY_HIGH)
    else:
        img = img.Scale(int(ogl_size[0] * size[1] / ogl_size[1]), size[1], wx.IMAGE_QUALITY_HIGH)
    if direction == 'center':
        bitmap = wx.Bitmap(img, wx.BITMAP_TYPE_JPEG)
    elif direction == 'left':
        bitmap = wx.Bitmap(img.Resize(size, 0, 0), wx.BITMAP_TYPE_JPEG)
    elif direction == 'right':
        bitmap = wx.Bitmap(img.Resize(size, wx.Point(size[0] - img.GetSize()[0], 0)), wx.BITMAP_TYPE_JPEG)
    elif direction == 'top':
        bitmap = wx.Bitmap(img.Resize(size, 0, 0), wx.BITMAP_TYPE_JPEG)
    elif direction == 'bottom':
        bitmap = wx.Bitmap(img.Resize(size, wx.Point(size[0] - img.GetSize()[0], 0)), wx.BITMAP_TYPE_JPEG)
    else:
        raise Exception
    return bitmap


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

