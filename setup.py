from setuptools import setup

setup(
    name='xontrib-voxvars',
    version='0.0.1',
    url='https://github.com/astronouth7303/xontrib-voxenv',
    license='MIT',
    author='Jamie Bliss',
    author_email='jamie@ivyleav.es',
    description='dotenv plus vox',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    install_requires=[
        'xonsh',
    ]
)
