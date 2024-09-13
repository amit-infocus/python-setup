from setuptools import setup, find_packages

setup(
    name='my-flask-app',                  # Your project name
    version='0.1',                        # Version of your project
    description='A simple Flask app',     # A short description
    author='Your Name',                   # Your name or organization
    author_email='your.email@example.com',# Your email
    packages=find_packages(),             # Automatically find your packages
    include_package_data=True,            # Include non-code files specified in MANIFEST.in
    install_requires=[
        'Flask',                          # Dependencies
    ],
)
