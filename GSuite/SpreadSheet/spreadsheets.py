# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from .base import SpreadSheetsBase
from .sheet import Sheet


class SpreadSheets(SpreadSheetsBase):

    spreadsheet_id: str = None

    def load(self, spreadsheet_id: str):
        return self.get(spreadsheet_id)

    def get(
        self,
        spreadsheet_id: str,
        ranges=None,
        include_grid_data=None,
        x__xgafv=None
    ):
        self.spreadsheet_id = spreadsheet_id
        return self.service.spreadsheets().get(
            spreadsheetId=spreadsheet_id,
            ranges=ranges,
            includeGridData=include_grid_data,
            x__xgafv=x__xgafv
        ).execute()

    def sheet(self, sheet_name: str = None):
        return Sheet(
            spreadsheet_id=self.spreadsheet_id,
            sheet_name=sheet_name,
            client=self.service
        )
