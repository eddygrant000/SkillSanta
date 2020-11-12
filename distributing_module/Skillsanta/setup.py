from distutils.core import setup

setup(
    name='Skillsanta',
    version='1.0.0',
    author='Sachin Saini',
    author_email='sachin.saini@ap2v.com',
    packages=['skillsanta'],
    url='http://pypi.python.org/pypi/Skillsanta',
    license='LICENSE.txt',
    description= 'Test Module By Skillsanta Team',
    long_description=open('README.txt').read(),
    install_requires=[
        "excel",
        "gmail"
    ]
)