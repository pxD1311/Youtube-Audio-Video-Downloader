from os import getcwd
from os.path import join

VERSION = "1.4-A"
DEVELOPER_MODE = True

DEFAULT_DOWNLOAD_PATH = join(getcwd(), "Downloads")
DEFAULT_AUDIO_FOLDER = "audio"
DEFAULT_VIDEO_FOLDER = "video"
DEFAULT_AUDIO_PATH = join(DEFAULT_DOWNLOAD_PATH, "audio")
DEFAULT_VIDEO_PATH = join(DEFAULT_DOWNLOAD_PATH, "video")