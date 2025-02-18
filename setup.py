from setuptools import setup


setup(
    name='owls_compress',
    version='1.0',
    description='An experiment in compression',
    author='SCSU CS Club',
    packages=['owls_compress'],
    entry_points={
        'console_scripts': [
            'owls_compress_evaluate = owls_compress.evaluate:main'
        ]
    }
)


