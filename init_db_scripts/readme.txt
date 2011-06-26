Directory with scirpts that initialise database content.
Useful to get quickly system up and running for development.

How to run scripts:

cd init_db_scripts
epxort PYTHONPATH=.
python ../manage.py shell
...
>>> import init_playlist
>>> init_db_playlist.run()
>>> import init_forums
>>> init_forums.run()
>>> etc...
