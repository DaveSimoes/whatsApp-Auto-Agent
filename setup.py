from setuptools import setup, find_packages

setup(
    name='whatsapp-autonomous-agent',
    version='0.1.0',
    author='Dave Simões',
    author_email='dspaiva12@gmail.com',
    description='An autonomous agent for WhatsApp that automates processes and offers personalized insights using AI.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask',
        'requests',  # Add any other dependencies required for WhatsApp API integration
        'numpy',     # Example dependency for data processing
        'pandas'     # Example dependency for data analysis
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)