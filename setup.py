import setuptools

setuptools.setup(
            name = 'powerpuff',
         version = '0.0.1',
         license = 'MIT',
          author = 'Artur Tamborski',
    author_email = 'ar@tur.ski',
     description = 'My silly collection of random utils',
             url = 'https://github.com/arturtamborski/powerpuff',
    download_url = 'https://github.com/arturtamborski/powerpuff/archive/0.0.1.tar.gz',
        keywords = 'utility collection',
     classifiers = [
        'Development Status :: 4 - Beta',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ], 

    long_description = open('readme.md').read(),
    long_description_content_type = 'text/markdown',
    zip_safe = False,
    include_package_data = True,
    packages = setuptools.find_packages(),
)
