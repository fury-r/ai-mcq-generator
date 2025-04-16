from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="fury-r",
    author_email="rajeev.dessai111@gmail.com",
    description="A mcq generator for any text",
    install_requires=["openai","langchain-community", "langchain", "streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)