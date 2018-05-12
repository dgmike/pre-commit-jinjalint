from setuptools import find_packages
from setuptools import setup

setup(
  name='dgmike_pre_commit_python',
  description=(
    'A pre-commit hook to run python instructions'
  ),

  url='https://github.com/dgmike/pre-commit-python',
  version='0.0.0',

  author='Michael Granados',
  author_email='contato@dgmike.com.br',

  packages=find_packages(exclude=('tests*', 'testing*')),

  package_data={
    'pre_commit': [
      'resources/*-tmpl',
      'resources/*.tar.gz',
      'resources/empty_template/*',
      'resources/empty_template/.npmignore',
    ],
  },
  install_requires=[
    'jinjalint',
  ],
)
