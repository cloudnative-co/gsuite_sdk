# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
import httplib2
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class Base(object):
    user = None
    http = None

    def __init__(
        self, credential_path: str, scopes: list, delegate_user: str = None
    ):
        """
        @params[in]     credentail_path GoogleのClient作成時のjsonのパス
        @params[in]     scopes          アクセスのスコープ一覧
        @params[in]     delegate_user   アクセスユーザーを指定
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credential_path,
            scopes=scopes
        )
        if delegate_user is not None:
            self.user = delegate_user
            credentials = credentials.create_delegated(delegate_user)
        self.http = credentials.authorize(httplib2.Http())
