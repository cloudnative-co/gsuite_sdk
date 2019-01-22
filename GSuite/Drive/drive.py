# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from ..base import Base
from apiclient.discovery import build


# See, edit, create, and delete all of your Google Drive files
SCOPE_DRIVE = "https://www.googleapis.com/auth/drive"
# View and manage its own configuration data in your Google Drive
SCOPE_DRIVE_APPDATA = "https://www.googleapis.com/auth/drive.appdata"
# View and manage Google Drive files and folders that you have opened or created with this app
SCOPE_DRIVE_FILE = "https://www.googleapis.com/auth/drive.file"
# View and manage metadata of files in your Google Drive
SCOPE_DRIVE_METADATA = "https://www.googleapis.com/auth/drive.metadata"
# View metadata for files in your Google Drive
SCOPE_DRIVE_METADATA_READONLY = "https://www.googleapis.com/auth/drive.metadata.readonly"
# View the photos, videos and albums in your Google Photos
SCOPE_DRIVE_PHOTOS_READONLY = "https://www.googleapis.com/auth/drive.photos.readonly"
# See and download all your Google Drive files
SCOPE_DRIVE_READONLY = "https://www.googleapis.com/auth/drive.readonly"
# Modify your Google Apps Script scripts' behavior
SCOPE_DRIVE_SCRIPTS = "https://www.googleapis.com/auth/drive.scripts"

SCOPES_MANAGE = [
    SCOPE_DRIVE,
    SCOPE_DRIVE_APPDATA,
    SCOPE_DRIVE_FILE,
    SCOPE_DRIVE_METADATA,
    SCOPE_DRIVE_PHOTOS_READONLY,
    SCOPE_DRIVE_SCRIPTS
]


class Drive(Base):
    service = None
    domain = None

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
        super(Drive, self).__init__(
            credential_path,
            scopes,
            delegate_user
        )
        self.service = build('drive', 'v3', http=self.http)

    def about(self):
        return self.service.about().get().to_json()
