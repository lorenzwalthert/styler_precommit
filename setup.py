from setuptools import setup

setup(name='styler_precommit',
      version='0.1.1',
      license='MIT',
      packages=['styler_precommit'],
      entry_points = {
        'console_scripts': ['style-files=styler_precommit.main:main']
      }
      )