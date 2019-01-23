# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from .base import SpreadSheetsBase
from apiclient.discovery import Resource


class Sheet(SpreadSheetsBase):

    spreadsheet_id: str = None
    sheet_name: str = None

    def __init__(
        self,
        spreadsheet_id: str,
        sheet_name: str,
        credential_path: str = None,
        scopes: list = None,
        delegate_user: str = None,
        client: Resource = None
    ):
        """
        @params[in]     credentail_path GoogleのClient作成時のjsonのパス
        @params[in]     scopes          アクセスのスコープ一覧
        @params[in]     delegate_user   アクセスユーザーを指定
        """
        if client is not None:
            self.service = client
        else:
            super(Sheet, self).__init__(
                credential_path,
                scopes,
                delegate_user
            )
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name

    def get(
        self,
        range: str,
        major_dimension: str = None,
        date_time_render_option: str = None,
        value_render_option: str = None,
        x__xgafv: str = None
    ):
        range = "{}!{}".format(self.sheet_name, range)
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=range,
            majorDimension=major_dimension,
            dateTimeRenderOption=date_time_render_option,
            valueRenderOption=value_render_option,
            x__xgafv=x__xgafv
        ).execute()
        return result
