# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from .base import CalendarBase


class Calendars(CalendarBase):

    def list(self,
        sync_token: str = None,
        min_access_role: str = None,
        max_results: int = None,
        show_deleted: bool = None,
        show_hidden: bool = None,
        page_token: str = None,
        auto_pager: bool = False,
    ):
        retval = []
        arvs = {
            "maxResults": max_results,
            "minAccessRole": min_access_role,
            "showDeleted": show_deleted,
            "showHidden": show_hidden
        }
        request = self.service.calendarList().list(**arvs)
        results = request.execute()
        entries = results.get('items', [])
        retval.extend(entries)
        page_token = results.get('nextPageToken', None)

        while auto_pager:
            if not page_token:
                break
            arvs["pageToken"] = page_token
            request = self.service.calendarList().list(**arvs)
            results = request.execute()
            entries = results.get('items', [])
            retval.extend(entries)
            page_token = results.get('nextPageToken', None)

        return retval
