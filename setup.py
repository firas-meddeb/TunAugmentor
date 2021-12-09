from setuptools import find_packages,setup

setup(
    name='TunAugmentor',
    packages=find_packages(include=['TunAugmentor']),
    version='0.1.0',
    description='Python library for image data augmentation',
    author='Ahmed Belgacem, Firas Meddeb',
    author_email = 'ahmedbelgaacem@gmail.com',
    url="https://github.com/ahmedbelgacem/TunAugmentor",
    license='MIT',
    install_requires=['numpy,opencv-python'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Data Science :: Image Augmentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9.7',
    ],
)