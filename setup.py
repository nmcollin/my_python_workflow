from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension('my_python_workflow.cy_work',
              sources=['my_python_workflow/cy_work.pyx'])
] # Include additional libraries to link to if you must


setup(
    name='my_python_workflow',
    version='',
    packages=['my_python_workflow'],
    url='',
    license='',
    author='Bryan Weinstein',
    author_email='bweinstein@seas.harvard.edu',
    description='For AC274, teaching students my python workflow'
)
