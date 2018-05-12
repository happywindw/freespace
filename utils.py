from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos


def get_duration_definition(video_name):
    """
    获取视频时长与清晰度
    :param video_name:
    :return:
    """
    video_info = ffmpeg_parse_infos(video_name)
    duration = int(video_info['duration'])   # 单位秒
    video_size = video_info['video_size']
    return duration, video_size

