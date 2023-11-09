"""
00 fork this replit to your replit 

01a do your code
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp
"""

from flask import Flask, jsonify
import os
import requests
#
from src.helper import github_request


app = Flask(__name__)
github_repo = "pyenv/pyenv"
github_api_url = f"https://api.github.com/repos/{github_repo}"

# Hàm lấy danh sách tất cả các phiên bản release
def get_all_releases():
    response = requests.get(f"{github_api_url}/releases")
    if response.status_code == 200:
        releases = response.json()
        return releases
    return []
@app.route('/')
def index():
  return jsonify({})

@app.route('/release')
def release():
  releases = get_all_releases()
  if releases:
      return jsonify(releases)
  return jsonify({}), 404


@app.route('/most_3_recent/release')
def most_3_recent__release():
  releases = get_all_releases()
  if releases:
      most_recent_releases = sorted(releases, key=lambda x: x['created_at'], reverse=True)[:3]
      return jsonify(most_recent_releases)
  return jsonify({}), 404


if __name__=='__main__':
  app.run(debug=True, port=os.environ.get('PORT', 5000) )
