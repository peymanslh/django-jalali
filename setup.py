from setuptools import setup, find_packages

setup(
    name='django-jalali',
    version='3.2.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    description=("Jalali Date support for Django model and admin interface"),
    url='http://github.com/slashmili/django-jalali',
    download_url='http://github.com/slashmili/django-jalali/tarball/master',
    author='Milad Rastian',
    author_email='eslashmili@gmail.com',
    keywords="django jalali",
    license='Python Software Foundation License',
    platforms='any',
    install_requires=["jdatetime>=2.0", "django>=2.0"],
    long_description=open('README.rst', encoding="utf-8").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
