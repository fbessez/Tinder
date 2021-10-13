import setuptools

with open('README.md') as desc_file:
      long_desc = desc_file.read().strip()

setuptools.setup(
      name='Tinder',
      version='2021.1',
      description='Tinder API for Python',
      long_description=long_desc,
      author='Fabien Bessez',
      url='https://github.com/fbessez/Tinder',
      license='MIT License',
      zip_safe=False,
      keywords=['tinder-api', 'tinder', 'python-3', 'robobrowser'],
      classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
      ],
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src")
)
