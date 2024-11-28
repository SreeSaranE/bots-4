from setuptools import setup, find_packages

setup(
    name="zoho-salesiq-chatbot",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        'flask>=2.0.1',
        'python-dotenv>=0.19.0',
        'requests>=2.26.0',
        'tensorflow>=2.7.0',
        'numpy>=1.19.5',
        'nltk>=3.6.3',
        'scikit-learn>=0.24.2',
        'transformers>=4.11.3',
        'python-i18n>=0.3.9',
        'schedule>=1.1.0',
        'python-dateutil>=2.8.2',
        'pyOpenSSL>=20.0.1',
        'flask-cors>=3.0.10',
    ],
)