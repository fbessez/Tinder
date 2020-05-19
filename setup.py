from setuptools import setup

setup(name='tinder_api',
      version='2020.5',
      description='Tinder API for Python',
      long_description=open('README.md').read().strip(),
      author='fabien bessez',
      url='https://github.com/fbessez/Tinder',
      py_modules=['tinder_api', 'facebook_auth_token'],
      install_requires=['requests',
                        'robobrowser',
                        'lxml'],
      license='MIT License',
      zip_safe=False,
      keywords=['tinder-api', 'tinder', 'python-3', 'robobrowser'],
     )
