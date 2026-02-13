from setuptools import setup, find_packages

setup(
    name="todo-evolution",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "sqlmodel>=0.0.16",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
        "python-dotenv>=1.0.0",
        "openai>=1.0.0",
    ],
    python_requires=">=3.11",
)