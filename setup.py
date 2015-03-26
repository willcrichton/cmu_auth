from setuptools import setup

setup(name='cmu_auth',
      version='0.1.5',
      description='Simple python methods for authenticating to Carnegie Mellon Unversity services.',
      url='https://github.com/willcrichton/cmu_auth',
      author='Will Crichton',
      author_email='willcrichton@cmu.edu',
      license='MIT',
      packages=['cmu_auth'],
      install_requires=[
          'requests',
      ],
      scripts=['bin/cmu_auth'],
      zip_safe=False)
