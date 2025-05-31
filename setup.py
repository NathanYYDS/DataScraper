# setup.py
from setuptools import setup, find_packages

setup(
    name="DataScraper",
    version="0.1.0", 
    author="NathanYYDS", 
    author_email="2200394635@qq.com",
    description="A web data scraper package of Python",
    packages=find_packages(), 
    install_requires=["requests", "click"],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "datascraper=datascraper.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Intended Audience :: Developers",
    ],
)