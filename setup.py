from setuptools import setup

setup(name='Tinder',
      version='2018.6',
      description='Tinder API for Python',
      long_description=open('README.md').read().strip(),
      author='fabien bessez',
      #author_email='',
      url='https://github.com/fbessez/Tinder',
      py_modules=['tinder_api', 'tinder_api_sms', 'fb_auth_token'],
      install_requires=['requests',
                        'robobrowser',
                        'lxml'],
      license='MIT License',
      zip_safe=False,
      keywords=['tinder-api', 'tinder', 'python-3', 'robobrowser'],
      #classifiers=[]
     )
