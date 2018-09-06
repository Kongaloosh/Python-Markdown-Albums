from distutils.core import setup

setup(
    name="MarkdownAlbums",
    version=0.1,
    packages=['markdown-albums'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n'),
)
