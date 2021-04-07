from setuptools import find_packages, setup

setup(
    name='elones',
    packages=find_packages(include=['elones']),
    version='0.0.2',
    description='An implementation of the Elo algorithm',
    author='Nestor Prieto',
    author_email='your.email@domain.com',
    url='https://github.com/nestorp/claim-diff_elones',
    download_url='https://github.com/nestorp/claim-diff_elones/archive/refs/tags/v0.0.2.tar.gz',
    license='MIT',
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)