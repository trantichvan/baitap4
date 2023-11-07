"""
debai thi https://docs.google.com/document/d/1uOEkOhBTY2hliH7_rlWQNdb566ZDvdfoT35-H-vqjDI/edit#bookmark=id.d50jkmfjzp4
"""

from flask import Flask, jsonify
import os
#
from src.helper import github_request


app = Flask(__name__)


'''
00   đầu gọi endpoint GET / trả về json rỗng {}
'''
@app.route('/')
def index():
  return jsonify({})


#region too complicated @ skip
'''
01a đầu gọi endpoint GET /publicrepo  trả về danh sách các kho git công khai trên github
ref endpoint for public repo  https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-public-repositories

ref endpoint for repo topic search  https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-topics
'''
@app.route('/pythondevops')
def pythondevops():
  #TODO why query param not working as guided in https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-public-repositories
  # hint query in ?q=  ref https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#example
  #                        =                                     ?type=       sort=        direction=     page=  per_page=
  # url                    = 'https://api.github.com/repositories?type=public&sort=updated&direction=desc&page=2&per_page=3'
  # l_origin,  status_code = github_request(url)
  # d                      = [i['full_name'] for i in l_origin]

  # query param build in py  ref https://stackoverflow.com/a/18558040/248616

  # search github topics
  # q = [('python'), ('devops')]
  # q   = [('python')]
  # url = f'https://api.github.com/search/topics?q={q}'
  # d_origin,  status_code = github_request(url)
  # d                      = [i['full_name'] for i in d_origin['items'] ]

  _='skipped as too complicated' # return jsonify(d), status_code
  '''
  l_origin[0]
  {
    'id': 1, 'node_id': 'MDEwOlJlcG9zaXRvcnkx', 
    'name': 'grit', 'full_name': 'mojombo/grit', 
    'private': False, 
    'owner': {'login': 'mojombo', 'id': 1, 'node_id': 'MDQ6VXNlcjE=', 'avatar_url': 'https://avatars.githubusercontent.com/u/1?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/mojombo', 'html_url': 'https://github.com/mojombo', 'followers_url': 'https://api.github.com/users/mojombo/followers', 'following_url': 'https://api.github.com/users/mojombo/following{/other_user}', 'gists_url': 'https://api.github.com/users/mojombo/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/mojombo/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/mojombo/subscriptions', 'organizations_url': 'https://api.github.com/users/mojombo/orgs', 'repos_url': 'https://api.github.com/users/mojombo/repos', 'events_url': 'https://api.github.com/users/mojombo/events{/privacy}', 'received_events_url': 'https://api.github.com/users/mojombo/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/mojombo/grit', 'description': '**Grit is no longer maintained. Check out libgit2/rugged.** Grit gives you object oriented read/write access to Git repositories via Ruby.', 'fork': False, 'url': 'https://api.github.com/repos/mojombo/grit', 'forks_url': 'https://api.github.com/repos/mojombo/grit/forks', 'keys_url': 'https://api.github.com/repos/mojombo/grit/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/mojombo/grit/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/mojombo/grit/teams', 'hooks_url': 'https://api.github.com/repos/mojombo/grit/hooks', 'issue_events_url': 'https://api.github.com/repos/mojombo/grit/issues/events{/number}', 'events_url': 'https://api.github.com/repos/mojombo/grit/events', 'assignees_url': 'https://api.github.com/repos/mojombo/grit/assignees{/user}', 'branches_url': 'https://api.github.com/repos/mojombo/grit/branches{/branch}', 'tags_url': 'https://api.github.com/repos/mojombo/grit/tags', 'blobs_url': 'https://api.github.com/repos/mojombo/grit/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/mojombo/grit/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/mojombo/grit/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/mojombo/grit/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/mojombo/grit/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/mojombo/grit/languages', 'stargazers_url': 'https://api.github.com/repos/mojombo/grit/stargazers', 'contributors_url': 'https://api.github.com/repos/mojombo/grit/contributors', 'subscribers_url': 'https://api.github.com/repos/mojombo/grit/subscribers', 'subscription_url': 'https://api.github.com/repos/mojombo/grit/subscription', 'commits_url': 'https://api.github.com/repos/mojombo/grit/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/mojombo/grit/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/mojombo/grit/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/mojombo/grit/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/mojombo/grit/contents/{+path}', 'compare_url': 'https://api.github.com/repos/mojombo/grit/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/mojombo/grit/merges', 'archive_url': 'https://api.github.com/repos/mojombo/grit/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/mojombo/grit/downloads', 'issues_url': 'https://api.github.com/repos/mojombo/grit/issues{/number}', 'pulls_url': 'https://api.github.com/repos/mojombo/grit/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/mojombo/grit/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/mojombo/grit/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/mojombo/grit/labels{/name}', 'releases_url': 'https://api.github.com/repos/mojombo/grit/releases{/id}', 'deployments_url': 'https://api.github.com/repos/mojombo/grit/deployments'
  }
  
  return d
  ['mojombo/grit', 'wycats/merb-core', 'rubinius/rubinius', 'mojombo/god', 'vanpelt/jsawesome', 'wycats/jspec', 'defunkt/exception_logger', 'defunkt/ambition', 'technoweenie/restful-authentication', 'technoweenie/attachment_fu', 'caged/microsis', 'anotherjesse/s3', 'anotherjesse/taboo', 'anotherjesse/foxtracs', 'anotherjesse/fotomatic', 'mojombo/glowstick', 'defunkt/starling', 'wycats/merb-more', 'macournoyer/thin', 'jamesgolick/resource_controller', 'jamesgolick/markaby', 'jamesgolick/enum_field', 'defunkt/subtlety', 'defunkt/zippy', 'defunkt/cache_fu', 'KirinDave/phosphor', 'bmizerany/sinatra', 'jnewland/gsa-prototype', 'technoweenie/duplikate', 'jnewland/lazy_record', 'jnewland/gsa-feeds', 'jnewland/votigoto', 'defunkt/mofo', 'jnewland/xhtmlize', 'ruby-git/ruby-git', 'ezmobius/bmhsearch', 'uggedal/mofo', 'mmower/simply_versioned', 'abhay/gchart', 'benburkert/schemr', 'abhay/calais', 'mojombo/chronic', 'sr/git-wiki', 'queso/signal-wiki', 'drnic/ruby-on-rails-tmbundle', 'danwrong/low-pro-for-jquery', 'wayneeseguin/merb-core', 'sr/dst', 'mojombo/yaws', 'KirinDave/yaws', 'sr/tasks', 'mattetti/ruby-on-rails-tmbundle', 'grempe/amazon-ec2', 'wayneeseguin/merblogger', 'wayneeseguin/merbtastic', 'wayneeseguin/alogr', 'wayneeseguin/autozest', 'wayneeseguin/rnginx', 'wayneeseguin/sequel', 'bmizerany/simply_versioned', 'peterc/switchpipe', 'hornbeck/arc', 'up_the_irons/ebay4r', 'wycats/merb-plugins', 'up_the_irons/ram', 'defunkt/ambitious_activeldap', 'atmos/fitter_happier', 'brosner/oebfare', 'up_the_irons/credit_card_tools', 'jnicklas/rorem', 'cristibalan/braid', 'jnicklas/uploadcolumn', 'simonjefford/ruby-on-rails-tmbundle', 'leahneukirchen/rack-mirror', 'leahneukirchen/coset-mirror', 'drnic/javascript-unittest-tmbundle', 'engineyard/eycap', 'leahneukirchen/gitsum', 'wayneeseguin/sequel-model', 'kevinclark/god', 'hornbeck/blerb-core', 'brosner/django-mptt', 'technomancy/bus-scheme', 'caged/javascript-bits', 'caged/groomlake', 'sevenwire/forgery', 'technicalpickles/ambitious-sphinx', 'lazyatom/soup', 'josh/rails', 'cdcarter/backpacking', 'jnewland/capsize', 'bs/starling', 'sr/ape', 'collectiveidea/awesomeness', 'collectiveidea/audited', 'collectiveidea/acts_as_geocodable', 'collectiveidea/acts_as_money', 'collectiveidea/calendar_builder', 'collectiveidea/clear_empty_attributes', 'collectiveidea/css_naked_day']  
  '''
#endregion too complicated @ skip


#region release
def get_all_release():
  #                     =                         /repos OWNER/REPO /releases
  url                   = f'https://api.github.com/repos/pyenv/pyenv/releases'
  r_origin, status_code = github_request(url)

  if status_code != 200: return jsonify(r_origin), status_code

  d = [
    {
      'created_at' : i['created_at'],
      'tag_name'   : i['tag_name'],
      'body'       : i['body'],
    }
    for i in r_origin
  ]

  return d, 200

@app.route('/release')
def release():
  """
  01a đầu gọi endpoint GET /release  trả về danh sách các xuất bản / release - mỗi kết quả có trường created_at, tag_name, và body

  ref endpoint for repo release
  https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#list-releases
  """
  d, status_code = get_all_release()
  return jsonify(d), status_code
  '''
  r_origin[0]
  {
    'created_at' : '2023-10-22T09:35:53Z', 
    'tag_name'   : 'v2.3.31', 
    'body'       : "## What's Changed\r\n* Add new anaconda and miniconda definitions by @aphedges in https://github.com/pyenv/pyenv/pull/2824\r\n\r\n\r\n**Full Changelog**: https://github.com/pyenv/pyenv/compare/2.3.30...v2.3.31", 'reactions': {'url': 'https://api.github.com/repos/pyenv/pyenv/releases/126144174/reactions', 'total_count': 3, '+1': 3, '-1': 0, 'laugh': 0, 'hooray': 0, 'confused': 0, 'heart': 0, 'rocket': 0, 'eyes': 0}, 
  }
  '''
#endregion release

@app.route('/most_3_recent/release')
def most_3_recent__release():
  """
  01b đầu gọi endpoint  GET /most_3_recent/release trả về 3 xuất bản / release mới nhất của 01a
  """
  d_origin, status_code = get_all_release()

  if status_code != 200: return jsonify(d_origin), status_code

  d = sorted(d_origin, key=lambda i: i['created_at'], reverse=True)
  d = d[:3]
  return jsonify(d), 200


if __name__=='__main__':
  app.run(debug=True, port=os.environ.get('PORT', 5000) )
