from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from dateutil.parser import parse
from django.core.cache import cache
import urllib2
import logging

log = logging.getLogger('django')

def code(request):
    cached_key = 'git-projects'
    commits = cache.get(cached_key)
    commits = None
    if not commits:
        commits = get_latest_commit('MacDroidSync', 'email', 'dlib', 'checkreg')
        cache.set(cached_key, commits, 300)

    return render(request, 'base/code.html', {'commits':commits})

def about(request):
    return render(request, 'base/about.html')

def music(request):
    return render(request, 'base/music.html')

def get_latest_commit(*project_names):
    commits = {}
    for project in project_names:
        json = None
        try:
            url = urllib2.urlopen('http://github.com/api/v2/json/commits/list/deanproxy/%s/master' % project)
            data = url.read()
            json = simplejson.loads(data)
        except ValueError:
            log.error('There was a problem parsing JSON data: %s' % json)
        except urllib2.URLError, error:
            log.error('A URLError exception was raised: %s ' % error)
        except urllib2.HTTPError, error:
            log.error('An HTTPError was raised: %s' % error)

        if json:
            most_recent = json['commits'][0]
            commits[project] = {}
            commits[project]['committed_date'] = parse(most_recent['committed_date'])
            commits[project]['message'] = most_recent['message']
            commits[project]['committer'] = most_recent['committer']['name']

    return commits
