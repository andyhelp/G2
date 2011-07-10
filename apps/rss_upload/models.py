from django.db import models
from django.contrib.auth.models import User
import feedparser

# Create your models here.
class Rss(models.Model):
    user        = models.ForeignKey(User, related_name='rss')
    url         = models.CharField(max_length=255, unique=True)
    
    def refresh(self):
        feed = feedparser.parse(self.url)
        for entry in feed.entries: 
            rsse = RssEntry()
            rsse.rss = self
            if 'media_content' in entry.keys():
                rsse.track_url = entry.media_content[0]['url']
            else:
                for l in entry.links:
                    if l['type'] == 'audio/mpeg':
                        rsse.track_url = l['href']
                        break
            if 'title' in entry.keys():
                rsse.title = entry.title
            elif 'subtitle' in entry.keys():
                rsse.title = entry.subtitle
            else:
                rsse.title = ''
            rsse.updated_parsed = entry.updated_parsed
            fentry = RssEntry.objects.filter(track_url=rsse.track_url)
            if not fentry:
                rsse.save()
                print 'Added new url', rsse.track_url
            else:
                print 'already fetched, url=', rsse.track_url
            

    
class RssEntry(models.Model):
    rss                 = models.ForeignKey(Rss)
    title               = models.CharField(max_length=255)
    track_url           = models.CharField(max_length=255)
    updated_parsed      = models.CharField(max_length=255)
