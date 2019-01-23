from __future__ import print_function
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaIoBaseUpload
from .base import DriveBase
from .metadata import Metadata
import io
import os


class Files(DriveBase):
    GAPI_MEDIA_IO_CHUNK_SIZE = 1024 * 1024

    def list(self, **argv):
        retval = []
        page_token = None
        while True:
            if page_token is not None:
                argv["pageToken"] = page_token
            request = self.service.files().list(**argv)
            results = request.execute()
            entries = results.get('files', [])
            retval.extend(entries)
            page_token = results.get('nextPageToken', None)
            if not page_token:
                break
        return retval

    def create(
        self,
        metadata: Metadata,
        file_path: str,
        original_mime_type: str= None
    ):
        if metadata.mimeType is None:
            raise Exception("MIME-TYPE Missing")
        if metadata.name is None:
            raise Exception("Name Missing")

        mimetype = metadata.mimeType
        if original_mime_type is not None:
            mimetype = original_mime_type

        if file_path is not None:
            file_stream = open(file_path, "rb")
        file_stream.seek(0)
        media = MediaIoBaseUpload(
            file_stream,
            mimetype=mimetype,
            chunksize=self.GAPI_MEDIA_IO_CHUNK_SIZE,
            resumable=True
        )
        request = self.service.files().create(
            body=metadata,
            media_body=media
        ).execute()
        file_stream.close()
        return dict(response.items())

    def insert(
        self,
        metadata: Metadata,
        file_stream: io.BytesIO,
        original_mime_type: str= None
    ):
        if metadata.mimeType is None:
            raise Exception("MIME-TYPE Missing")
        if metadata.name is None:
            raise Exception("Name Missing")

        mimetype = metadata.mimeType
        if original_mime_type is not None:
            mimetype = original_mime_type

        file_stream.seek(0)
        media = MediaIoBaseUpload(
            file_stream,
            chunksize=self.GAPI_MEDIA_IO_CHUNK_SIZE,
            resumable=True,
            mimetype=mimetype
        )
        response = self.service.files().create(
            body=metadata,
            media_body=media
        ).execute()
        return dict(response.items())


    def create_folder(self, name: str, parents_id: str = None):
        metadata = Metadata()
        metadata.name = name
        metadata.mimeType = 'application/vnd.google-apps.folder',
        if parents_id is not None:
            metadata.parents.append(parents_id)
        file = self.service.files().create(body=file_metadata).execute()
        return dict(file.items())

    def get(
        self,
        file_id: str,
        supports_team_drives = None,
        acknowledge_abuse = None
    ):
        file = self.service.files().get(
            fileId=file_id,
            supportsTeamDrives=supports_team_drives,
            acknowledgeAbuse=acknowledge_abuse
        ).execute()
        print ('File ID: %s' % file.get('id'))
        return dict(file.items())


    def delete(self, file_id: str, supports_team_drives: bool = False):
        file = self.service.files().delete(
            fileId=file_id,
            supportsTeamDrives=supports_team_drives
        ).execute()
        return file_id

    def get_media(
        self,
        file_id: str,
        supports_team_drives: bool = None,
        acknowledge_abuse: bool = None,
        retry_count: int = 5
    ):
        request = self.service.files().get_media(
            fileId=file_id,
            supportsTeamDrives=supports_team_drives,
            acknowledgeAbuse=acknowledge_abuse
        )
        stream = io.BytesIO()
        downloader = MediaIoBaseDownload(stream, request)
        done = None
        for retry in range(1, retry_count):
            try:
                while done is False:
                    status, done = downloader.next_chunk()
                return stream.getvalue()
            except Exception as e:
                print(e)
                if retry >= retry_count:
                    raise e
                continue
