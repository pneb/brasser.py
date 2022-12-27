from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='brasser',
    version='1.0.0',
    author='Bernward Sanchez',
    author_email='contact@bern.codes',
    description='A library for generating cryptographically random UUIDs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['brasser'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
