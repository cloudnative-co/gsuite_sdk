# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from .base import CalendarBase


class Events(CalendarBase):

    def insert(self,
        calendar_id: str,
        body = dict,
        conference_data_version: int = 0,
        max_attendees: int = None,
        send_notifications: bool = False,
        send_updates: str = None,
        supports_attachments: bool = False
    ):
        argv = {
            "calendarId": calendar_id,
            "body": body,
            "conferenceDataVersion": conference_data_version,
            "sendNotifications": send_notifications,
            "supportsAttachments": supports_attachments,
            "maxAttendees": max_attendees,
            "sendUpdates": send_updates
        }
        request = self.service.events().insert(**argv)
        results = request.execute()
        return results

