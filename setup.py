from setuptools import setup, find_packages

setup(
    name="TelegramBot",
    version="0.1.0",
    author="Chinmay Sanjay Raut",
    author_email="r.chinmay396@gmail.com",
    description="This is a LLM powered Telegram bot.",
    long_description=open("README.md").read(),
    url="https://github.com/chinmay396-indian/LLM-Powered-Telegram-Bot",
    packages=find_packages(),
    python_requires=">=3.9",
    license= "MIT",
)