# micro-shortener

This is a micro in-memory url shortener

## Usage

```bash
virtualenv venv
source venv/bin/activate
# ignore the lines above this one if you don't have virtualenv installed
pip install -r requirements.txt
python shortener.py

# on another terminal
curl -X POST -H "Content-Type: application/json" -d '{"url":"example.org"}' http://localhost:5000/api/shortcuts

# on your browser open the following url, note that id is the one that you got from the past request
http://localhost:5000/{id}
```

