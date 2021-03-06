import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='VEnCode',
    version='0.0.2',
    description='Package to get VEnCodes as in Macedo and Gontijo, 2019',
    author='Andre Macedo',
    author_email='andre.lopes.macedo@gmail.com',
    url='https://github.com/AndreMacedo88/VEnCode',
    packages=setuptools.find_packages(),
    install_requires=[
        "biopython",
        "tqdm",
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",
        "pyvisa",
        "pylab"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
    ]
)
