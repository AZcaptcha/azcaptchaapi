# -*- coding: utf8 -*-
from distutils.core import setup

setup(
    name='azcaptchaapi',
    version='0.1',
    packages=['twocaptchaapi'],
    url='https://github.com/azcaptcha/azcaptchaapi',
    license='MIT',
    author='AZCaptcha by Joel Höner (athre0z)',
    author_email='mail@azcaptcha.com',
    description='Python API implementation for AZCaptcha.com',
    download_url='https://github.com/azcaptcha/azcaptchaapi/archive/v0.1.tar.gz',
    install_requires=[
        'requests>=2.9',
    ],
)
