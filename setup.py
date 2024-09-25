# setup.py
from setuptools import setup, find_packages

setup(
    name="compare_print",
    version="0.1",
    description="A decorator to display outputs side by side in Jupyter Lab",
    author="Shantam Raj",
    author_email="email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'IPython',  # Ensure IPython is installed for display functions
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
