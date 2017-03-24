from setuptools import setup

setup(
    name='discovermovies',
    author='Sidhin S Thomas',
    author_email='sidhin.thomas@gmail.com',
    description='Flask Rest api server for discovermovies',
    version='01dev',
    packages=['dicsovermovies','discovermovies.core'],
    license='GNU General Public License',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)