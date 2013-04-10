from distutils.core import setup

setup(name='pycrowd',
      version='0.1',
      description='Python Crowdsourcing',
      author='Bryan Marty',
      author_email='bxm156@case.edu',
      url='http://pycrowd.bryanmarty.com',
      packages=['pycrowd','pycrowd.evaluator','pycrowd.executor','pycrowd.hits','pycrowd.jobs',
          'pycrowd.prediction','pycrowd.query','pycrowd.workers'],
      classifiers=[
          #Status
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Programming Language :: Python',
          ],
     )
