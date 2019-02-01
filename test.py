import json
from GSuite.Drive import Files
from GSuite.Drive import Metadata
from GSuite.Drive import SCOPES_MANAGE as DRIVE_SCOPES
from GSuite.SpreadSheets import SCOPES_MANAGE as SHEET_SCOPES
from GSuite.SpreadSheets import SpreadSheets
import io
#import Box
import urllib.request

box_setting = {
    'client_id': '8igeta273q0sxrq11kfdw7bmpgvt7zwe',
    'client_secret': 'qv2z63vQh6XirPiaJRl4iBCS8iObQSug',
    'enterprise_id': '25458939',
    'jwt_key_id': '1x4zharz',
    'rsa_private_key_file_sys_path': './private_key.pem',
    'rsa_private_key_passphrase': b'tkai2451'
}

sheets = SpreadSheets(
    credential_path = "directory-backend-access.json",
    scopes = SHEET_SCOPES,
    delegate_user = "seba@cloudnative.co.jp"
)
"""
drive = Files(
    credential_path = "directory-backend-access.json",
    scopes = DRIVE_SCOPES,
    delegate_user = "seba@cloudnative.co.jp"
)
box = Box.File(**box_setting)
box.login("seba@cloudnative.co.jp")
buf = io.BytesIO(box.download(file_id="249362309160"))

metadata = Metadata()
metadata.name = "tempolary.gsheet"
metadata.mimeType = "application/vnd.google-apps.spreadsheet"

file = drive.insert(
    metadata=metadata,
    file_stream=buf,
    original_mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
id = file.get("id")
"""
id = "1hEkCjoRsvAL21iQWZFfjsrost-IhFj6yPmRnNhzhS00"
a = sheets.get(id)
#a = sheets.get('給料支払い実績!A2:A',id)
print(a)

#drive.delete(file_id=id)
