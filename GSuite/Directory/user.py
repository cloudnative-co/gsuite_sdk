# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from .base import DirectoryBase


class User(DirectoryBase):

    def list(
        self,
        order_by: str = None,
        domain: str = None,
        projection: str = None,
        query: str = None,
        event: str = None,
        show_deleted: bool = None,
        page_token: str = None,
        sort_order: str = None,
        max_results: int = None,
        customer: str = None,
        custom_field_mask: str = None,
        view_type: str = None,
        auto_pager: bool = False,
    ):
        retval = []
        if domain is None:
            domain = self.domain
        args = {
            "orderBy": order_by,
            "domain": domain,
            "projection": projection,
            "query": query,
            "event": event,
            "showDeleted": show_deleted,
            "pageToken": page_token,
            "sortOrder": sort_order,
            "maxResults": max_results,
            "customer": customer,
            "customFieldMask": custom_field_mask,
            "viewType": view_type
        }
        request = self.service.users().list(**args)
        results = request.execute()
        entries = results.get('users', [])
        retval.extend(entries)
        page_token = results.get('nextPageToken', None)
        while auto_pager:
            if not page_token:
                break
            argv["pageToken"] = page_token
            request = self.service.users().list(**args)
            results = request.execute()
            entries = results.get('users', [])
            retval.extend(entries)
            page_token = results.get('nextPageToken', None)
            if not page_token:
                break
        return retval

