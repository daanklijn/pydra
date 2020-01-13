from distutils.core import setup
setup(
  name = 'pydra',         
  packages = ['pydra'],   
  version = '1.0',
  license='MIT',        
  description = 'A visual synthesizer written in Python',   
  author = 'Daan Klijn',                   
  author_email = 'daanklijn0@gmail.com',      
  url = 'https://github.com/daanklijn/pydra',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['python', 'synthesizer', 'visual'],   
  install_requires=[            
          'numpy',
          'scipy',
          'pygame',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
