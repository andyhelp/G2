# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/jonnty/")
import os.path
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp3 import HeaderNotFoundError
import hashlib
from django.core.management import setup_environ
from pydj import settings
setup_environ(settings)
from pydj.playlist.models import *
from django.contrib.auth.models import User

class UnsupportedFormatError(Exception): pass
class CorruptFileError(Exception): pass

class UploadedFile:
  supported_types = set(['mp3']) #TODO: ogg (and m4a?)
  def __init__(self, file, realname=None, filetype=None):
    
    self.type = filetype
    
    if realname is None:
      realname = os.path.basename(file)
    self.realname = realname
    
    if self.type is None:
      self.type = os.path.splitext(realname)[1].strip('.')
      
    self.type = self.type.lower()  
    
    if self.type not in self.supported_types:
      raise UnsupportedFormatError, "%s not supported" % self.type
    
    self.info = {}
    self.file = file
    self.getHash()
    self.getTags()
    
    
    
  def getHash(self):
    """Populates self.sha_hash with sha1 hash of uploaded file."""
    f = open(self.file)
    self.info['sha_hash'] = hashlib.sha1(f.read()).hexdigest()
    f.close()
    
  def store(self):
    """Store song in a usable directory using SongDir
    and record it in the database. Return the Song object created."""
    storage = SongDir.objects.getUsableDir()
    storage.storeSong(self.file, self.info)
    self.info['location'] = storage
    # Filter out any attributes that aren't part of the model
    fields = set()
    for f in Song._meta.fields:
        fields.add(f.name)
    info = dict(self.info)
    for key in info.keys():
        if key not in fields:
            del info[key]
    s = Song(**info)
    s.full_clean()
    s.save()
    return s
  
  def getTags(self):
    """Run correct tagging method. 
    
    Method name format: get<type in uppercase>Tags"""
    getattr(self, 'get'+self.type.upper()+'Tags')()
    
  def getMP3Tags(self):
    """Returns dict with tags and stuff"""
    tags = {}
    
    try:
      song = MP3(self.file, ID3=EasyID3)
    except HeaderNotFoundError:
      raise CorruptFileError
    
    tags.update(song)
    
    for value in tags.keys():
      try:
        tags[value] = tags[value][0] #list to string (first element)
      except IndexError:
        tags[value] = ""
        
      
    tags['length'] = round(song.info.length)
    tags['bitrate'] = song.info.bitrate/1000 #b/s -> kb/s
    if "title" not in tags or not tags['title'].strip():
      tags['title'] = self.realname
    if 'artist' in tags and tags['artist'].strip():
      tags['artist'] = Artist.objects.get_or_create(name=tags['artist'])[0]
    else:
      tags['artist'] = Artist.objects.get_or_create(name='(unknown)')[0]
    if 'album' in tags and tags['album'].strip():
      tags['album'] = Album.objects.get_or_create(name=tags['album'])[0]
    else: 
      tags['album'] = Album.objects.get_or_create(name='(empty)')[0]
    
    for x in ["version", "date"]:
      if x in tags.keys():
        del tags[x] #not stored
        
    if "tracknumber" in tags:
      try:
        tags['track'] = int(tags['tracknumber'])
      except ValueError:
        #handle tracknumbers like 11/12 meaning 'track eleven of twelve'
        tags['track']  = ""
        for char in tags['tracknumber']:
          try:
            tags['track'] += str(int(char))
          except ValueError:
            break
            
      del tags['tracknumber']
        
    # Fix garbled or blank track numbers in tags
    try:
      tags['track'] = int(tags['track'])
    except ValueError:
      tags['track'] = None
    except KeyError:
      pass

    tags['format'] = "mp3"
    
    self.info.update(tags)

#if __name__ == "__main__":
  #u = UploadedFile("/home/jadh/mus/Collection/06 - Weight Of My Words.mp3")
  #print u.info
  ##User.objects.get(username='jj').get_profile().uploadSong(u)
    
    
