import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='yfinance2pg-karlewr',  # Replace with your own username
    version='0.0.1',
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
    install_requires=[
        'yfinance',
        'psycopg2',
        'requests',
        'html5lib',
        'bs4',
        'multitasking'
    ],
    python_requires='>=3.6',
)
