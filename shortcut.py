from copy import deepcopy

class Shortcut(object):
  """docstring for Shortcut"""
  def __init__(self, url):
    super(Shortcut, self).__init__()
    self.url = url
    self.usages = 0
    
  def get_usages(self):
    return self.usages

  def get_url(self):
    self.usages += 1
    return self.url;

  def to_JSON(self):
    return {'url': self.url, 'usages': self.usages}
  
  def copy(self):
    return deepcopy(self)