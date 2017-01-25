from flask import Flask, request, jsonify, Response
from shortcut import Shortcut
import string
import random

app = Flask(__name__)

shortcuts_dict = {}

def generate_id(size=7, chars=string.ascii_lowercase + string.digits):
  return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

@app.route('/api')
def api_welcome():
  return jsonify({'author': 'diego.camargo [at] openmailbox [dot] org', 'version': 0.01})

@app.route('/api/shortcuts', methods = ['GET'])
def show_shortcuts():
  urls = []
  for key in shortcuts_dict.keys():
    urls.append(shortcuts_dict[key].to_dict())
  return jsonify(urls)

@app.route('/api/shortcuts/<key>', methods = ['GET'])
def show_shortcut(key):
  if key in shortcuts_dict:
    return jsonify(shortcuts_dict[key].to_dict())
  else:
    return page_not_found()

@app.route('/<key>')
def go_to(key):
  if key in shortcuts_dict:
    shortcut = shortcuts_dict[key]
    shortcut.use_once()
    return str.format('<meta http-equiv="refresh" content="0; url={}" />', shortcut.url)
  else:
    return page_not_found()

@app.route('/api/shortcuts', methods = ['POST'])
def add_shortcut():
  global shortcuts_dict
  if request.headers['Content-Type'] == 'application/json' and request.json['url'] != None:
    dst = request.json['url']
    if not dst.startswith('http'):
      dst = 'http://' + dst
    shortcut = Shortcut(generate_id(), dst)
    shortcuts_dict[shortcut.id] = shortcut
    return jsonify(shortcut.to_dict())
  else:
    return "Unsupported Media Type ;)", 415

@app.route('/api/shortcuts/<id>', methods = ['DELETE'])
def remove_shortcut(id):
  global shortcuts_dict
  if id in shortcuts_dict:
    shortcut = shortcuts_dict[id]
    shortcuts_dict.pop(id)
    return jsonify(shortcut.to_dict())
  else:
    return page_not_found()

@app.errorhandler(404)
def page_not_found():
  return 'You got lost mate', 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)