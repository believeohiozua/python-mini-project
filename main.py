import os
import argparse
import sys
from src.utils import text_scraper_and_analyser

parser = argparse.ArgumentParser(description="This script scrapes and analyses website")
parser.add_argument("-rt", "--runtest", action="store_true", help="This runs the unittest script TDD support of the program")
parser.add_argument("-rs", "--runscrape", action="store_true", help="This runs a loop that scrapes and analyses a website")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.runtest:
        print("\nRunning TDD Implimentation Test by BELIEVE OHIOZUA...\n")
        if sys.platform.startswith('win'):
            os.system('cd tests && python test_initial.py')
        else:
            os.system('cd tests && python3 test_initial.py')
        print("\nThanks For Testing\n")
    if args.runscrape:
        text_scraper_and_analyser()

sys.stdout.flush()