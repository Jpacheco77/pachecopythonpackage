from setuptools import setup

setup(name='pacheco python package',
      version='0.1',
      description='Subset a matrix and do a BLAST search',
      url='TBD',
      author='Juan Pacheco',
      author_email='juan.pacheco@selu.edu',
      license='MIT',
      packages=['pachecopythonpackage'],
      install_requires=[
          'dendropy',
          'pandas',
          'biopython'
      ],
      long_description=open('README.txt').read(),
      zip_safe=True)