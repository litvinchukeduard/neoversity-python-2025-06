python3 -m venv .venv

source ./.venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt
