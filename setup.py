from setuptools import setup, find_packages

SOURCE_DIR_NAME = 'src'

setup(
    name='3d_modeller',
    version='0.0.1',
    description='A useful module',
    license="MIT",
    author='Man Foo',
    author_email='foomail@foo.com',
    url="http://www.foopackage.com/",
    packages=find_packages(SOURCE_DIR_NAME),
    package_dir={'': SOURCE_DIR_NAME},
    install_requires=[],
    entry_points={
        'console_scripts': [
            '3d_modeller = 3d_modeller.__main__:main'
        ],
    },
)
