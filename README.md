# Development

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

# Testing

```
pytest
flake8 *.py
black *.py
```

# Running

```
python3 app.py

curl "http://localhost:5000/api/v1/knight/a1"
curl "http://localhost:5000/api/v1/knight/a1/b3"
curl "http://localhost:5000/api/v1/queen/a5"
curl "http://localhost:5000/api/v1/queen/A5/A10"

```