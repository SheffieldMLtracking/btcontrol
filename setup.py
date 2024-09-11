from distutils.core import setup
setup(
  name = 'btcontrol',
  packages = ['btcontrol'],
  version = '0.2',
  description = 'Tool for controlling the tracking systems.',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/SheffieldMLtracking/btcontrol.git',
  download_url = 'https://github.com/SheffieldMLtracking/btcontrol.git',
  keywords = ['bumblebees','ecology','tracking','retroreflectors'],
  classifiers = [],
  install_requires=['numpy'],
  scripts=['bin/btcontrol'],
)
