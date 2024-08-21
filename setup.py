from setuptools import setup, find_packages
import os

# Leer el archivo README.md de forma segura
this_directory = os.path.abspath(os.path.dirname(__file__))
long_description = ""
readme_path = os.path.join(this_directory, 'README.md')

if os.path.exists(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        long_description = f.read()

setup(
    name="Larva_lib",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "Jetson.GPIO>=2.0.0",
        "pynput>=1.7.3",
        "opencv-python>=4.5.3.56",
    ],
    author="HectorVR-Dev",
    author_email="hectordaniel1112@gmail.com",
    description="A library for controlling stepper motors and lighting for larva motion experiments",
    long_description=long_description,  # Usamos el contenido del README si existe
    long_description_content_type='text/markdown',
    url="https://github.com/HectorVR-Dev/larva_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
