from setuptools import setup, find_packages

setup(
    name='studentGHrepo',
    version='0.1.0',
    description='A demo package to learn PyPI publishing',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/studentGHrepo',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        'gpu': ['tensorflow-gpu']
    },
)
