# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from .__init__ import Directory


class User(Directory):

    def list(self, **argv):
        if "domain" not in argv:
            argv["domain"] = self.domain

        retval = []
        page_token = None
        while True:
            if page_token is not None:
                argv["pageToken"] = page_token
            request = self.service.users().list(**argv)
            results = request.execute()
            entries = results.get('users', [])
            retval.extend(entries)
            page_token = results.get('nextPageToken', None)
            if not page_token:
                break
        return retval
