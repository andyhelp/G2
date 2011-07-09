from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from rss_upload.forms import RssUrlForm, RssRefreshForm
from rss_upload.models import Rss, RssEntry
from playlist.upload import UploadedFile
import urllib
import tempfile

def list(request):
    rss_list = Rss.objects.filter(user=request.user)
    form = RssUrlForm()
    return render_to_response('rss_upload/list.html', {'rss_list': rss_list, 'form': form}, context_instance=RequestContext(request))

def entries(request,rssid_str):
    rssid = int(rssid_str)
    rss_list = Rss.objects.filter(id=rssid)
    rss = None
    if rss_list:
        rss = rss_list[0]
    entry_list = RssEntry.objects.filter(rss=rssid)
    return render_to_response('rss_upload/rss_entry_list.html', {'rss': rss, 'entry_list': entry_list}, context_instance=RequestContext(request))
    


def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RssUrlForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            rss = Rss()
            rss.user = request.user
            rss.url = form.cleaned_data['url']
            rss.save();
    return HttpResponseRedirect('/rss/list')


def refresh(request):
    if request.method == 'GET': # If the form has been submitted...
        id = request.GET.get('id')
        rss = Rss.objects.filter(id=id)
        if rss:
            rss[0].refresh()
    return HttpResponseRedirect('/rss/list')


def upload(request, rssid_str, entryid_str):
    rssid = int(rssid_str)
    entryid = int(entryid_str)
    
    rssEntry_list = RssEntry.objects.filter(id=entryid)
    if rssEntry_list:
        rssEntry = rssEntry_list[0]
        f = tempfile.NamedTemporaryFile()
        urllib.urlretrieve(rssEntry.track_url, f.name )        
        request.user.get_profile().uploadSong(UploadedFile(f.name, filetype='mp3'))
        f.close()
    
    return HttpResponseRedirect('/rss/list')
