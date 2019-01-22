# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from ..base import Base
from apiclient.discovery import build

# See, edit, create, and delete all of your Google Drive files
SCOPE_DRIVE = "https://www.googleapis.com/auth/drive"
# View and manage Google Drive files and folders that you have opened or created with this app
SCOPE_DRIVE_FILE = "https://www.googleapis.com/auth/drive.file"
# See, edit, share, and permanently delete all the calendars
# you can access using Google Calendar
SCOPE_CALENDAR = "https://www.googleapis.com/auth/calendar"
# View and edit events on all your calendars
SCOPE_CALENDAR_EVENTS = "https://www.googleapis.com/auth/calendar.events"
# View events on all your calendars
SCOPE_CALENDAR_EVENTS_READONLY = "https://www.googleapis.com/auth/calendar.events.readonly"
# View your calendars
SCOPE_CALENDAR_READONLY = "https://www.googleapis.com/auth/calendar.readonly"
# View your Calendar settings
SCOPE_CALENDAR_SETTINGS_READONLY = "https://www.googleapis.com/auth/calendar.settings.readonly"


SCOPES_MANAGE = [
    SCOPE_DRIVE,
    SCOPE_CALENDAR,
    SCOPE_CALENDAR_EVENTS,
    SCOPE_CALENDAR_SETTINGS_READONLY
]


class CalendarBase(Base):
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
        super(CalendarBase, self).__init__(
            credential_path,
            scopes,
            delegate_user
        )
        self.service = build('calendar', 'v3', http=self.http)
