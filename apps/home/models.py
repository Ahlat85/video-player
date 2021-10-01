import os
from os import walk
import json

from django.db import models


class VideoModel(models.Model):
  __path = 'static/data'

  def fetch(self, file):
    result = {}
    f = os.path.join(self.__path, file).strip()
     
    result["url"] = f
    result["size"] = round(os.path.getsize(f) / (1024 * 1024))
    
    try:
      data = json.load(open(f[:-4] + '.json', 'r'))
    except:
      fi = open(f[:-4] + '.json', 'w+')
      fi.close()
      data = {}
     
    result['file'] = file[:-4]
    result['data'] = data
    return result

  def fetch_all(self):
    result = []
    for (dirpath, dirnames, filenames) in walk(self.__path):
      for f in filenames:
        if f.endswith('.mp4'):
          path = os.path.join(dirpath, f)
          json_file = f'{path[:-4]}.json'

          try:
            data = json.load(open(json_file, 'r'))
          except:
            data = {}
          
          x = {
            'name': f[:-4],
            'file': f,
            'path': path,
            'size': round(os.path.getsize(path) / (1024 * 1024))
          }
          
          for k, v in data.items():
            x[k] = v

          result.append(x)
    result.sort(key=lambda video: video['name'])
    return result