from distutils.core import setup
setup(name='emva1288',
      packages=['emva1288'],
      version='0.1',
      description='EMVA1288 reference implementation',
      author='Federico Ariza',
      author_email='ariza.federico@gmail.com',
      url='https://github.com/EMVA1288/emva1288',
      keywords=['sensors', 'cameras'],
      classifiers=[],
      install_requires=['matplotlib',
                        'numpy',
                        'pillow',
                        'lxml',
                        'scipy'],
      )
