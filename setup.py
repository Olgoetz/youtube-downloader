from setuptools import setup
setup(
    name='youtube-downloader',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'youtube-downloader=yt:main'
        ]
    }
)