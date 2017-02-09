from setuptools import setup, find_packages

def read_license():
    with open("LICENSE") as f:
        return f.read()

setup(
    name='raguel',
    packages=find_packages(),
    version='0.1.0',
    description='Python implementation of Raguel',
    long_description="""Raguel description""",    
    license=read_license(),
    author='Dylan Whichard',
    author_email='dylan@whichard.com',
    url='https://github.com/WireShoutLLC/pyraguel',
    keywords=[
        'voting',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
    ],
    data_files=[
    ],
)
