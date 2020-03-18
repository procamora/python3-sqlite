from distutils.core import setup

setup(
    name='procamora-sqlite3',  # How you named your package folder (MyLib)
    packages=['procamora_sqlite3'],  # Chose the same as "name"
    version='0.1',  # Start with a small number and increase it with every change you make
    license='gpl-3.0',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Library to manage a sqlite database',  # Give a short description about your library
    author='procamora',  # Type in your name
    author_email='pablojoserocamora@gmail.com',  # Type in your E-Mail
    url='https://github.com/procamora/python3-sqlite',  # Provide either the link to your github or to your website
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    keywords=['sqlite', 'sql', 'sqlite3'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'sqlite3',
        'colorlog',
        'Werkzeug',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Databases',
        'License :: OSI Approved :: GNU General Public License v3.0',  # Again, pick a license
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    #py_modules=["interface_sqlite"],  # Required
    python_requires='<4, >=3.4',
)
