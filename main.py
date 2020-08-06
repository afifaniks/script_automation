from automator import Automator

# Loading scripts to execute in the list sequentially
scripts = ['script.py', 'zip_extractor.py']

# Initializing Automator with time paramaeters
Automator(scripts, 'thursday', '14:00').start()
