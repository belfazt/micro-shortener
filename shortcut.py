from copy import deepcopy
from time import strftime

class Shortcut(object):
  """This class represents an Shortcut"""
  def __init__(self, uid, url):
    super(Shortcut, self).__init__()
    self.url = url
    self.id = uid
    self.usages = []

  def use_once(self):
    self.usages.append(strftime("%Y-%m-%d %H:%M:%S"))

  def to_dict(self):
    return {'id': self.id, 'url': self.url, 'usages': self.usages, 'usage_count': len(self.usages)}

  def copy(self):
    return deepcopy(self)