from setuptools import setup

setup(name='chow_test',
      version='0.1',
      description='Package to calculate Chow break statistics.',
      url='http://github.com/jtloong/chow_test',
      author='Joshua Loong',
      author_email='joshua.t.loong@gmail.com',
      license='MIT',
      packages=['chow_test'],
      install_requires=[
          'sklearn',
          'pandas',
          'numpy'
      ],
      zip_safe=False)
