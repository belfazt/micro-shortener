from flask import Flask, url_for, request, jsonify, Response, render_template, redirect
from shortcut import Shortcut
from uuid import uuid4

app = Flask(__name__)

shortened_urls = dict()

def create_shortcut():
  return str(uuid4())[:6]

@app.route('/api')
def api_welcome():
  data = dict()
  data['author'] = 'dicamargov [at] gmail [dot] com'
  data['version'] = 0.01
  return jsonify(data)

@app.route('/api/stats')
def api_show_stats():
  urls = shortened_urls.copy()
  for key in urls.keys():
    urls[key] = urls[key].to_JSON()
  return jsonify(urls)

@app.route('/<key>')
def go_to(key):
  if key in shortened_urls:
    dst = str(shortened_urls[key].get_url())
    if not dst.startswith('http'):
      dst = 'http://' + dst
    return render_template('redir.html', url = dst)
  else:
    return page_not_found()

@app.route('/api/shorten', methods = ['POST'])
def api_shorten():
  if request.headers['Content-Type'] == 'application/json' and request.json['url'] != None:
    global shortened_urls
    shortcut = create_shortcut()
    shortened_urls[shortcut] = Shortcut(request.json['url'])
    return jsonify({'shortened_url' : shortcut})
    else:
      return "Unsupported Media Type ;)", 415

@app.errorhandler(404)
def page_not_found():
  return 'You got lost mate', 404

if __name__ == '__main__':
  app.run(debug=True)