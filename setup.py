from setuptools import setup, find_packages

setup(
    name='get_contract',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        "aiogram~=2.14",
        "python-environ",
        "environs",
        "docx",
        "openpyxl~=3.0.7",
        "docx2pdf~=0.1.8",
        "pip~=22.0.4",
        "attrs~=23.1.0",
        "wheel~=0.37.1",
        "cryptography~=41.0.3",
        "Pillow~=9.1.1",
        "Jinja2~=2.11.3",
        "setuptools~=65.5.0",
        "packaging~=21.3",
        "pyparsing~=3.0.9",
        "SQLAlchemy~=1.4.41",
        "sqlmodel~=0.0.8",
        "Mako~=1.2.4",
        "xhtml2pdf~=0.2.11",
        "python-magic-0.4.27"
    ],
    authors='Akrom Amirov',
    license='MIT',
)
