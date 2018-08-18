Python version: >=3.6 

Install modules (ddt):
pip install -r env/pip.txt

run tests:
python -m unittest tests.keyboard_tests
python -m unittest tests.data_cruncher_test

run main:
python main.py file.json
