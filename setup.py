from distutils.core import setup

setup (
    name = "mobile-agents",
    version= "0.0.1",
    author = "Santosh Suresh",
    author_email= "santosh.s@telibrahma.com",
    packages = ['mobile-agents'],
    license = 'MIT',
    description='A library to identify devices (phones, tablets) and their capabilities by parsing (browser) user agent strings',
    zip_safe = False,
    include_package_data = False,
    install_requires = ['pyyaml','ua-parser'],
)