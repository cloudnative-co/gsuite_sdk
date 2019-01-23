# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from ..base import Base
from apiclient.discovery import build


# See, edit, create, and delete all of your Google Drive files
SCOPE_DRIVE = "https://www.googleapis.com/auth/drive"
# View and manage Google Drive files and folders that you have opened or created with this app
SCOPE_DRIVE_FILE = "https://www.googleapis.com/auth/drive.file"
# See and download all your Google Drive files
SCOPE_DRIVE_READONLY = "https://www.googleapis.com/auth/drive.readonly"
# View and manage your spreadsheets in Google Drive
SCOPE_SPREADSHEETS = "https://www.googleapis.com/auth/spreadsheets"
# View your Google Spreadsheets
SCOPE_SPREADSHEETS_READONLY = "https://www.googleapis.com/auth/spreadsheets.readonly"

SCOPES_MANAGE = [
    SCOPE_DRIVE,
    SCOPE_DRIVE_FILE,
    SCOPE_SPREADSHEETS
]


class SpreadSheetsBase(Base):
    service = None

    def __init__(
        self,
        credential_path: str,
        scopes: list,
        delegate_user: str = None
    ):
        """
        @params[in]     credentail_path GoogleのClient作成時のjsonのパス
        @params[in]     scopes          アクセスのスコープ一覧
        @params[in]     delegate_user   アクセスユーザーを指定
        """
        super(SpreadSheetsBase, self).__init__(
            credential_path,
            scopes,
            delegate_user
        )
        discoveryUrl = (
                'https://sheets.googleapis.com/$discovery/rest?'
                'version=v4'
        )
        self.service = build(
            'sheets',
            'v4',
            http=self.http,
            discoveryServiceUrl=discoveryUrl
        )
