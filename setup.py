from setuptools import setup, find_packages

setup(
    name='Telegram bot',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        "aiohttp==3.8.6",
        "aiosignal==1.3.1",
        "alembic==1.12.1",
        "annotated-types==0.5.0",
        "anyio==3.7.1",
        "async-timeout==4.0.3",
        "asynctest==0.13.0",
        "attrs==23.2.0",
        "Babel==2.9.1",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "colorama==0.4.6",
        "et-xmlfile==1.1.0",
        "exceptiongroup==1.2.0",
        "fastapi==0.103.2",
        "frozenlist==1.3.3",
        "greenlet==3.0.3",
        "h11==0.14.0",
        "idna==3.6",
        "importlib-metadata==6.7.0",
        "importlib-resources==5.12.0",
        "lxml==5.1.0",
        "magic-filter==1.0.12",
        "MarkupSafe==2.1.5",
        "multidict==6.0.5",
        "psycopg2==2.9.9",
        "pydantic==2.5.3",
        "pydantic_core==2.14.6",
        "pypng==0.20220715.0",
        "python-dotenv==0.21.1",
        "pytz==2024.1",
        "pyzbar==0.1.9",
        "qrcode==7.4.2",
        "sniffio==1.3.1",
        "starlette==0.27.0",
        "tqdm==4.66.2",
        "typing_extensions==4.7.1",
        "uvicorn==0.22.0",
        "yarl==1.9.4",
        "zipp==3.15.0",
    ],
    authors='Akrom Amirov',
    license='MIT',
)
