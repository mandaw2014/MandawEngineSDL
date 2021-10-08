from distutils.core import setup

setup(name='Mandaw',
      version='0.0.1',
      description='A 2D Python GameEngine Made With PySDL2',
      author='mandaw2014',
      keywords="python 2d game development",
      author_email='mandawbuisness@gmail.com',
      url='https://github.com/mandaw2014/MandawEngineSDL/tree/experimental',
      packages=['mandaw'],
      package_dir={'mandaw': 'mandaw'},
      install_requires=["pysdl2"]
      )
