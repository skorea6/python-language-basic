import urllib
import json
import re
import requests
from edgeauth import EdgeAuth, EdgeAuthError
from flask import Flask, Blueprint, request, Response, redirect, session

ET_HOSTNAME = 'tqfukkcnerea5481819.cdn.ntruss.com'
ET_ENCRYPTION_KEY = '3f534982667c55f2e3e2'
DEFAULT_WINDOW_SECONDS = 3600 # seconds

#import logging
from flask_cors import CORS
#from gevent.pywsgi import WSGIServer

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)


#wavve_credential = ''
session = requests.session()
config = {'base_url': 'https://apis.pooq.co.kr',
 'base_parameter': {'apikey': 'E5F3E0D30947AA5440556471321BB6D9',
                    'credential': 'none',
                    'device': 'pc',
                    'partner': 'pooq',
                    'pooqzone': 'none',
                    'region': 'kor',
                    'drm': 'wm',
                    'targetage': 'auto'},
 'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}}

def get_baseparameter():
    try:
        return config['base_parameter'].copy()
    except Exception as e:
        pass
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())

def do_login(id, pw, json_return = False):
    try:
        body = {'type': 'general',
         'id': id,
         'pushid': '',
         'password': pw,
         'profile': '0',
         'networktype': '',
         'carrier': '',
         'mcc': '',
         'mnc': '',
         'markettype': 'unknown',
         'adid': '',
         'simoperator': '',
         'installerpackagename': ''}
        url = '%s/login?%s' % (config['base_url'], urllib.parse.urlencode(config['base_parameter']))
        response = session.post(url, json=body, headers=config['headers'])
        data = response.json()
        if 'credential' in data:
            if json_return:
                return data
            else:
                return data['credential']
        #else:
            #logger.debug('login fail!!')
            #if 'resultcode' in data:
                #logger.debug(data['resultmessage'])
    except Exception as e:
        pass
        #print(e)
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())


def streaming(contenttype, contentid, quality, credential, action = 'hls', ishevc = 'y', isabr = 'y', proxy = None):
    if contenttype == 'live':
        ishevc = 'n'
        isabr = 'n'
    if credential is None:
        credential = 'none'
    try:
        param = get_baseparameter()
        param['credential'] = credential
        if contenttype == 'general':
            contenttype = 'vod'
        elif contenttype == 'onair':
            contenttype = 'onairvod'
        param['contenttype'] = contenttype
        param['contentid'] = contentid
        param['action'] = action
        param['quality'] = quality
        param['guid'] = ''
        param['deviceModelId'] = 'Windows 10'
        param['authtype'] = 'url'
        param['isabr'] = isabr
        param['ishevc'] = ishevc
        param['lastplayid'] = 'none'
        url = '%s/streaming?%s' % (config['base_url'], urllib.parse.urlencode(param))
        proxies = None
        if proxy is not None:
            proxies = {'https': proxy,
             'http': proxy}
        response = session.get(url, headers=config['headers'], proxies=proxies)
        data = response.json()
        if response.status_code == 200:
            try:
                if data['playurl'].startswith('https://event.pca.wavve.com'):
                    #logger.debug('playurl startswith https://event.pca.wavve.com!!!!!')
                    return streaming_imsi(contenttype, contentid, quality, credential, action=action, ishevc=ishevc, isabr=isabr)
            except:
                pass
                #logger.debug('https://event.pca.wavve.com error')

            return data
        if 'resultcode' in data:
            pass
    except Exception as e:
        pass
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())

    return


def streaming_imsi(contenttype, contentid, quality, credential, action = 'hls', ishevc = 'y', isabr = 'y', proxy = None):
    if contenttype == 'live':
        ishevc = 'n'
        isabr = 'n'
    if credential is None:
        credential = 'none'
    try:
        param = get_baseparameter()
        param['credential'] = credential
        if contenttype == 'general':
            contenttype = 'vod'
        elif contenttype == 'onair':
            contenttype = 'onairvod'
        param['contenttype'] = contenttype
        param['contentid'] = contentid
        param['action'] = action
        param['quality'] = quality
        param['guid'] = ''
        param['authtype'] = 'url'
        param['isabr'] = isabr
        param['ishevc'] = ishevc
        param['lastplayid'] = 'none'
        param['device'] = 'smarttv'
        url = '%s/streaming?%s' % (config['base_url'], urllib.parse.urlencode(param))
        response = session.get(url, headers=config['headers'])
        data = response.json()
        if response.status_code == 200:
            #logger.debug(data['playurl'])
            return data
        if 'resultcode' in data:
            pass
    except Exception as e:
        pass
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())

    return







wavve_credential = None

def get_login_data(source_id, source_pw):
    login_data = None
    global wavve_credential
    if wavve_credential == None:
        #if source_id != '' and source_pw != '':
        login_data = do_login(source_id, source_pw)
        wavve_credential = login_data
        #print(login_data)
    else:
        login_data = wavve_credential

    return login_data

def get_url(source_id, quality, mode, retry=True):
    try:
        try:
            g_login_data = get_login_data('', '')
            data = streaming('live', source_id, quality, g_login_data)
            surl = None
            if data is not None:
                surl = data['playurl']
            if surl is None:
                raise Exception('no url')
        except:
            #print("Plastic")
            if retry:
                #logger.debug('RETRY')
                global  wavve_credential
                wavve_credential = do_login('', '')
                return get_url(source_id, quality, mode, retry=False)

        #print("COK", surl)
        return 'return_after_read', surl
    except Exception as e:
        print('WOW2:', e)
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())


def get_return_data(source_id, url, mode):
    try:
        data = requests.get(url).content
        temp = url.split('live.m3u8')
        #print("1: ", type(data))
        new_data = data.decode()
        #print("2: ", type(new_data))
        new_data = new_data.replace('live_', '%slive_' % temp[0])
        #new_data = data.encode()
        #new_data = bytes(new_data, 'ascii')
        #print("3: ", type(new_data))
        #print("4: ", new_data)
        if mode == 'web_play':
            pass
        return change_redirect_data(new_data)
    except Exception as e:
        print('WOW1:', e)
        #pass
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())
    return data

def change_redirect_data(data):
    try:
        #logger.debug(data)
        #print("WOW0")
        #print(data)
        tmp = re.compile(r'http(.*?)$', re.MULTILINE).finditer(data)
        #print("WOW1")
        for m in tmp:
            u = m.group(0)

            #et = EdgeAuth(**{'key': ET_ENCRYPTION_KEY,'window_seconds': DEFAULT_WINDOW_SECONDS})
            #token = et.generate_acl_token("/api/*")
            #u2 = "http://{0}{1}?url={2}&{3}={4}".format(ET_HOSTNAME, "/api/redirect.ts", urllib.parse.quote(u), et.token_name, token)

            #u2 = "http://myip.abz.kr:8666/api/redirect.ts?url={0}".format(urllib.parse.quote(u))
            #print(u2);
            u2 = 'http://tqfukkcnerea5481819.cdn.ntruss.com/api/redirect.ts?url={url}'.format(url=urllib.parse.quote(u))
            #print(u2)
            #u2 = u2.replace('https', 'http')
            #if SystemModelSetting.get_bool('auth_use_apikey'):
            #    u2 += '&apikey={apikey}'.format(apikey=SystemModelSetting.get('auth_apikey'))
            data = data.replace(u, u2)
        #logger.debug(data)
        #print("WOW2")
        #data = data.replace('%5Cn%23EXTINF%3A2.0%2C%5Cn', '\\n#EXTINF:2.0,\\n')
        #data = data.replace('%5Cn%27', "\\n'")
        #print(data)
        #data.decode('ascii')
        #print(type(data))
        return data
    except Exception as e:
        print('WOW3:', e)
        #pass
        #logger.error('Exception:%s', e)
        #logger.error(traceback.format_exc())


app = Flask(__name__)
CORS(app)
#bp = Blueprint('stream', __name__)
#@bp.route('/api/<sub>', methods=['GET', 'POST'])

@app.route('/api/<sub>', methods=['GET', 'POST'])
def api(sub):
    if sub == 'url.m3u8':
        try:
            mode = request.args.get('m')
            #source = request.args.get('s')
            source_id = request.args.get('i')
            #cdn_token = request.args.get('token')
            #quality = request.args.get('q')
            # logger.debug('m:%s, s:%s, i:%s', mode, source, source_id)

            action, ret = get_url(source_id, 'HD', mode)
            # logger.debug('action:%s, url:%s', action, ret)
            #print("WOOOO", action, ret)
            if action == 'redirect':
                print('a')
                return redirect(ret, code=302)
            elif action == 'return_after_read':
                print('b')
                data = get_return_data(source_id, ret, mode)
                #print(data)
                # logger.debug('Data len : %s', len(data))
                return data, 200, {'Content-Type': 'application/vnd.apple.mpegurl'}
            elif action == 'return':
                print('c')
                return ret
            if ret == None:
                print('e')
                return
            if mode == 'url.m3u8':
                print('d')
                return redirect(ret, code=302)
            elif mode == 'lc':
                print('f')
                return ret
        except Exception as e:
            print(e)
            return
            #logger.error('Exception:%s', e)
            #logger.error(traceback.format_exc())

    elif sub == 'redirect.ts':
        try:
            print("test")
            url = request.args.get('url')
            url = urllib.parse.unquote(url)

            # logger.debug('REDIRECT:%s', url)
            res = requests.get(url)
            data = res.content
            return data, 200, {'Content-Type': res.headers['Content-Type']}
        except Exception as e:
            print(e)
            #logger.error('Exception:%s', e)
            #logger.error(traceback.format_exc())


if __name__ == '__main__':
    #http_server = WSGIServer(('0.0.0.0', 8666), app)
    #http_server.serve_forever()
    app.run(host='0.0.0.0', port=8666, threaded=True)