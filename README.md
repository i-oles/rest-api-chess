# About

This project is a simple REST API built with Flask.  
Users can:
1. check available moves by passing particular figure name and starting field
1. validate move from one field to another

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

python3 app.py

List available moves for given figure and field:  


`curl "http://127.0.0.1:5000/api/v1/knight/a1"`  

proper response:  
```
{
"availableMoves":["B3","C2"],
"currentField":"A1",
"error":null,
"figure":"knight"
}
```


`curl "http://127.0.0.1:5000/api/v1/queen/a5"`  

proper response:  
```
{
"availableMoves":["D8","A8","C7","A7","B6","A6","H5","G5","F5","E5","D5","C5","B5","B4","A4","C3","A3","D2","A2","E1","A1"],
"currentField":"A5",
"error":null,
"figure":"queen"
}
```


`curl "http://127.0.0.1:5000/api/v1/knight/a1/b3"`  

proper response:  
```
{
"currentField":"A1",
"destField":"B3",
"error":null,
"figure":"knight",
"move":"valid"
}
```


`curl "http://127.0.0.1:5000/api/v1/queen/A5/a10"`  

proper response:  
```
{
"currentField":"A5",
"destField":"A10",
"error":"Current move is not permitted.",
"figure":"queen",
"move":"invalid"
}
```
