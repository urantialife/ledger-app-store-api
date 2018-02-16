#!/usr/bin/env python3

import requests
import pprint
import fire
import sys
from soft_u2f import SoftU2FDevice

PP = pprint.PrettyPrinter(indent=4)

API_URL = 'http://localhost:8000'

FACET = 'http://www.example.com'


def _req(method, url, verify=False, **kwargs):
    resp = requests.request(method, url, verify=verify, **kwargs)
    if resp.status_code < 400:
        return resp.json()
    else:
        print('ERROR: ', resp.text)
        sys.exit()


class Cli:

    def fetch_all_users(self):
        r = _req('GET', API_URL + '/api/users')
        PP.pprint(r)

    def fetch_user(self, uid):
        url = '{}/api/user/{}'.format(API_URL, uid)
        r = _req('GET', url)
        PP.pprint(r)

    def update_user(self, uid, **kwargs):
        url = '{}/api/user/{}'.format(API_URL, uid)
        user_dict = {}
        for key, val in kwargs.items():
            if val:
                user_dict[key] = val
        _req('PUT', url, json=user_dict)

    def register_device(self, username, auth_token):
        u2f_key = SoftU2FDevice()

        resp = _req('GET', API_URL + '/api/key_registration',
                    headers={'Authorization': 'Token {}'.format(auth_token)})

        response = u2f_key.register(FACET, resp['appId'], resp['registerRequests'][0])
        resp = _req('POST', API_URL + '/api/key_registration',
                    headers={'Authorization': 'Token {}'.format(auth_token)},
                    json={'username': username, 'response': response})
        print('resp: ', resp)

    def login(self, username, password, u2f=False):
        print('authenticating member...')
        if not u2f:
            resp = _req('POST', API_URL + '/api/auth', json={'username': username, 'password': password})
            auth_token = resp['token']
            print('token: ', auth_token)
        else:
            u2f_key = SoftU2FDevice()
            resp = _req('POST', API_URL + '/api/auth', json={'username': username, 'password': password})
            response = u2f_key.getAssertion(
                FACET,
                resp['appId'],
                resp['challenge'],
                resp['registeredKeys'][0]
            )
            resp2 = _req('POST', API_URL + 'api//finish_authentication', json={'response': response})
            print('token: ', resp2['token'])


if __name__ == '__main__':
    fire.Fire(Cli)