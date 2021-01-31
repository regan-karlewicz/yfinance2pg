import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='yfinance2pg',  # Replace with your own username
    version='1.0.0',
    author='Regan Karlewicz',
    author_email='yfinance2pg@karlewr.net',
    description='Download finance data from yfinance to postgres database',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/regan-karlewicz/yfinance2pg',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    scripts=['bin/yfinance2pg'],
    install_requires=[
        'yfinance>=0.1.55',
        'psycopg2>=2.8.6',
        'requests>=2.25.1',
        'html5lib>=1.1',
        'bs4>=0.0.1',
        'multitasking>=0.0.9'
    ],
    python_requires='>=3.6',
)
