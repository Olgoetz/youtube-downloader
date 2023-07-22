from pytube import YouTube
import ffmpeg
import os
from pathlib import Path

# Get the home directory
home = str(Path.home())


def download(link: str):
    """Downloads the best mp4 version from YouTube

    Args:
        link (str): YouTube URL
    """

    print("Download started...")
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True,
                 on_complete_callback=onCompleted)
    stream = yt.streams.filter(only_audio=True, subtype="mp4").order_by(
        'bitrate').desc().first()
    print("Title:   ", yt.title)
    print("Artist : ", yt.author)
    try:
        stream.download()
    except Exception as e:
        print(e)


def onCompleted(stream: str, path: str):
    """Executed afte download has finished

    Args:
        stream (str): Name of the YouTube stream
        path (str): Filename with path
    """

    print("Download is completed successfully")
    print("----------------------------------------")
    convertToMp3(path)


def convertToMp3(path: str):
    """Converts a mp4 to a mp3 file.

    Args:
        path (str): Path of the mp4 file
    """

    print("Converting to mp3...")
    file_without_path = os.path.basename(path)
    file_without_extension = os.path.splitext(file_without_path)[0]
    output = f'{home}/Music/{file_without_extension}.mp3'
    (
        ffmpeg.input(path)
        .output(output, **{'c:a': 'libmp3lame', 'q:a': 0, 'c:v': 'copy'})
        .global_args('-loglevel', 'error')
        .global_args('-y')
        .run()
    )
    print("Converting completed!")
    os.remove(path)
    print("----------------------------------------")
    print("File location: ", output)


input = input("Please enter the URL: ")
print("----------------------------------------")


def main():
    download(input)
