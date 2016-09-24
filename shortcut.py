from copy import deepcopy

class Shortcut(object):
  """This class represents an Shortcut"""
  def __init__(self, uid, url):
    super(Shortcut, self).__init__()
    self.url = url
    self.id = uid
    self.usages = 0

  def use_once(self):
    self.usages += 1

  def to_dict(self):
    return {'id': self.id, 'url': self.url, 'usages': self.usages}

  def copy(self):
    return deepcopy(self)