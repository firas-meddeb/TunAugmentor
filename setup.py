from setuptools import find_packages,setup

setup(
    name='TunAugmentor',
    packages=find_packages(include=['TunAugmentor']),
    version='0.1.0',
    description='Python library for image data augmentation',
    author='Ahmed Belgacem, Firas Meddeb',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)