import inspect
from inspect import signature


class User(dict):
    __keys = {
        # Whether this user is the requesting user.
        "me": bool,
        # Identifies what kind of resource
        # this is. Value: the fixed string "drive
        "kind": str,
        # A plain text displayable name for this user.
        "displayName": str,
        # The user's ID as visible in Permission resources.
        "permissionId": str,
        # The email address of the user.
        # This may not be present in certain contexts
        # if the user has not made their email address visible to the requester
        "emailAddress": str,
        # A link to the user's profile photo, if available.
        "photoLink": str
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class Location(dict):
    __keys = {
        # The latitude stored in the image.
        "latitude": float,
        # The altitude stored in the image.
        "altitude": float,
        # The longitude stored in the image.
        "longitude": float
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class ImageMediaMetadata(dict):
    __keys = {
        # The exposure bias of the photo (APEX value).
        "exposureBias": float,
        # The length of the exposure, in seconds.
        "exposureTime": float,
        # The make of the camera used to create the photo.
        "cameraMake": str,
        # The smallest f-number of the lens at the focal length used to create the photo (APEX value).
        "maxApertureValue": float,
        # The width of the image in pixels.
        "width": int,
        # The focal length used to create the photo, in millimeters.
        "focalLength": float,
        # The exposure mode used to create the photo.
        "exposureMode": str,
        # The color space of the photo.
        "colorSpace": str,
        # Geographic location information stored in the image.
        "location": Location,
        # The distance to the subject of the photo, in meters.
        "subjectDistance": int,
        # The height of the image in pixels.
        "height": int,
        # The lens used to create the photo.
        "lens": str,
        # The ISO speed used to create the photo.
        "isoSpeed": int,
        # The metering mode used to create the photo.
        "meteringMode": str,
        # Whether a flash was used to create the photo.
        "flashUsed": bool,
        # The date and time the photo was taken (EXIF DateTime).
        "time": str,
        # The aperture used to create the photo (f-number).
        "aperture": float,
        # The rotation in clockwise degrees from the image's original orientation.
        "rotation": int,
        # The type of sensor used to create the photo.
        "sensor": str,
        # The white balance mode used to create the photo.
        "whiteBalance": str,
        # The model of the camera used to create the photo.
        "cameraModel": str
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class Thumbnail(dict):
    __keys = {
        # The MIME type of the thumbnail.
        "mimeType": str,
        # The thumbnail data encoded with URL-safe Base64 (RFC 4648 section 5).
        "image": str
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class ContentHints(dict):
    __keys = {
        # Text to be indexed for the file to improve fullText queries. This is limited to 128KB in length and may contain HTML elements.
        "indexableText": str,
        # A thumbnail for the file. This will only be used if Drive cannot generate a standard thumbnail.
        "thumbnail": Thumbnail
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class TeamDrivePermissionDetail(dict):
    __keys = {
        # The ID of the item from which this permission is inherited. This is an output-only field and is only populated for members of the Team Drive.
        "inheritedFrom": str,
        # The primary role for this user. While new values may be added in the future, the following are currently possible:
        # - organizer
        # - fileOrganizer
        # - writer
        # - commenter
        # - reader
        "role": str,
        # The Team Drive permission type for this user. While new values may be added in future, the following are currently possible:
        # - file
        # - member
        "teamDrivePermissionType": str,
        # Whether this permission is inherited. This field is always populated. This is an output-only field.
        "inherited": bool
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class TeamDrivePermissionDetails(list):
    def append(self, value: TeamDrivePermissionDetail):
        if isinstance(value, TeamDrivePermissionDetail):
            super(TeamDrivePermissionDetails, self).append(value)


class Permission(dict):
    __keys = {
        # The domain to which this permission refers.
        "domain": str,
        # A displayable name for users, groups or domains.
        "displayName": str,
        # Details of whether the permissions on this Team Drive item are inherited or directly on this item. This is an output-only field which is present only for Team Drive items.
        "teamDrivePermissionDetails": TeamDrivePermissionDetails,
        # Whether the permission allows the file to be discovered through search. This is only applicable for permissions of type domain or anyone.
        "allowFileDiscovery": bool,
        # Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions.
        "deleted": bool,
        # Identifies what kind of resource this is. Value: the fixed string "drive#permission".
        "kind": str,
        # The email address of the user or group to which this permission refers.
        "emailAddress": str,
        # A link to the user's profile photo, if available.
        "photoLink": str,
        # The role granted by this permission. While new values may be supported in the future, the following are currently allowed:
        # - owner
        # - organizer
        # - fileOrganizer
        # - writer
        # - commenter
        # - reader
        "role": str,
        # The time at which this permission will expire (RFC 3339 date-time). Expiration times have the following restrictions:
        # - They can only be set on user and group permissions
        # - The time must be in the future
        # - The time cannot be more than a year in the future
        "expirationTime": str,
        # The type of the grantee. Valid values are:
        # - user
        # - group
        # - domain
        # - anyone
        "type": str,
        # The ID of this permission. This is a unique identifier for the grantee, and is published in User resources as permissionId.
        "id": str
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class Permissions(list):
    def append(self, value: Permission):
        if isinstance(value, Permission):
            super(Permissions, self).append(value)


class Capabilities(dict):
    __keys = {
        # Whether the current user can restore this file from trash.
        "canUntrash": bool,
        # Whether the current user can move this Team Drive item within this Team Drive. Note that a request to change the parent of the item may still fail depending on the new parent that is being added. Only populated for Team Drive items.
        "canMoveItemWithinTeamDrive": bool,
        # Whether the current user can delete children of this folder. This is false when the item is not a folder. Only populated for Team Drive items.
        "canDeleteChildren": bool,
        # Whether the current user can move children of this folder within the Team Drive. This is false when the item is not a folder. Only populated for Team Drive items.
        "canMoveChildrenWithinTeamDrive": bool,
        # Whether the current user can list the children of this folder. This is always false when the item is not a folder.
        "canListChildren": bool,
        # Whether the current user can rename this file.
        "canRename": bool,
        # Whether the current user can add children to this folder. This is always false when the item is not a folder.
        "canAddChildren": bool,
        # Whether the current user can modify the sharing settings for this file.
        "canShare": bool,
        # Whether the current user can trash children of this folder. This is false when the item is not a folder. Only populated for Team Drive items.
        "canTrashChildren": bool,
        # Whether the current user can read the revisions resource of this file. For a Team Drive item, whether revisions of non-folder descendants of this item, or this item itself if it is not a folder, can be read.
        "canReadRevisions": bool,
        # Whether the current user can copy this file. For a Team Drive item, whether the current user can copy non-folder descendants of this item, or this item itself if it is not a folder.
        "canCopy": bool,
        # Whether the current user can move this item into a Team Drive. If the item is in a Team Drive, this field is equivalent to canMoveTeamDriveItem.
        "canMoveItemIntoTeamDrive": bool,
        # Whether the current user can move this Team Drive item outside of this Team Drive by changing its parent. Note that a request to change the parent of the item may still fail depending on the new parent that is being added. Only populated for Team Drive items.
        "canMoveItemOutOfTeamDrive": bool,
        # Whether the current user can comment on this file.
        "canComment": bool,
        # Deprecated
        "canChangeViewersCanCopyContent": bool,
        # Whether the current user can move this file to trash.
        "canTrash": bool,
        # Whether the current user can delete this file.
        "canDelete": bool,
        # Deprecated - use canMoveItemWithinTeamDrive or canMoveItemOutOfTeamDrive instead.
        "canMoveTeamDriveItem": bool,
        # Whether the current user can download this file.
        "canDownload": bool,
        # Whether the current user can change the copyRequiresWriterPermission restriction of this file.
        "canChangeCopyRequiresWriterPermission": bool,
        # Whether the current user can move children of this folder outside of the Team Drive. This is false when the item is not a folder. Only populated for Team Drive items.
        "canMoveChildrenOutOfTeamDrive": bool,
        # Whether the current user can remove children from this folder. This is always false when the item is not a folder. For Team Drive items, use canDeleteChildren or canTrashChildren instead.
        "canRemoveChildren": bool,
        # Whether the current user can read the Team Drive to which this file belongs. Only populated for Team Drive files.
        "canReadTeamDrive": bool,
        # Whether the current user can edit this file.
        "canEdit": bool
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class VideoMediaMetadata(dict):
    __keys = {
        # The width of the video in pixels.
        "width": int,
        # The duration of the video in milliseconds.
        "durationMillis": str,
        # The height of the video in pixels.
        "height": int
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]


class Owners(list):

    def append(self, value: User):
        if isinstance(value, User):
            super(Owners, self).append(value)


class Metadata(dict):
    __keys = {
        # Whether this file has a thumbnail. This does not indicate whether the requesting app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field.
        # Drive will attempt to automatically detect an appropriate value from uploaded content if no value is provided. The value cannot be changed unless a new revision is uploaded.
        # If a file is created with a Google Doc MIME type, the uploaded content will be imported if possible. The supported import formats are published in the About resource.
        "hasThumbnail": bool,
        # The MIME type of the file.
        "mimeType": str,
        # The last time the file was modified by the user (RFC 3339 date-time).
        "modifiedByMeTime": str,
        # A short-lived link to the file's thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file's content.
        "thumbnailLink": str,
        # The thumbnail version for use in thumbnail cache invalidation.
        "thumbnailVersion": str,
        # Whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder.
        "explicitlyTrashed": bool,
        # Whether the file was created or opened by the requesting app.
        "isAppAuthorized": bool,
        # ID of the Team Drive the file resides in.
        "teamDriveId": str,
        # Whether users with only writer permission can modify the file's permissions. Not populated for Team Drive files.
        "writersCanShare": bool,
        # Whether the user owns the file. Not populated for Team Drive files.
        "ownedByMe": bool,
        # The last time the file was viewed by the user (RFC 3339 date-time).
        "viewedByMeTime": str,
        # The ID of the file.
        "id": str,
        # Information about a Drive user. # The user who shared the file with the requesting user, if applicable.
        "sharingUser": User,
        # The size of the file's content in bytes. This is only applicable to files with binary content in Drive.
        "size": str,
        # Additional metadata about video media. This may not be available immediately upon upload.
        "videoMediaMetadata": VideoMediaMetadata,
        # Information about a Drive user. # The last user to modify the file.
        "lastModifyingUser": User,
        # The color for a folder as an RGB hex string. The supported colors are published in the folderColorPalette field of the About resource.
        # If an unsupported color is specified, the closest color in the palette will be used instead.
        "folderColorRgb": str,
        # A collection of arbitrary key-value pairs which are private to the requesting app.
        "appProperties": dict,
        # Capabilities the current user has on this file. Each capability corresponds to a fine-grained action that a user may take.
        "capabilities": Capabilities,
        # The time that the item was trashed (RFC 3339 date-time). Only populated for Team Drive files.
        "trashedTime": str,
        # A link for opening the file in a relevant Google editor or viewer in a browser.
        "webViewLink": str,
        # A monotonically increasing version number for the file. This reflects every change made to the file on the server, even those not visible to the user.
        "version": str,
        # The IDs of the parent folders which contain the file.
        "parents": list,
        # The time at which the file was shared with the user, if applicable (RFC 3339 date-time).
        "sharedWithMeTime": str,
        # Whether the file has been shared. Not populated for Team Drive files.
        "shared": bool,
        # Whether the options to copy, print, or download this file, should be disabled for readers and commenters.
        "copyRequiresWriterPermission": bool,
        # The full file extension extracted from the name field. May contain multiple concatenated extensions, such as "tar.gz". This is only available for files with binary content in Drive.
        # This is automatically updated when the name field changes, however it is not cleared if the new name does not contain a valid extension.
        "fullFileExtension": str,
        # The original filename of the uploaded content if available, or else the original value of the name field. This is only available for files with binary content in Drive.
        "originalFilename": str,
        # Deprecated - use copyRequiresWriterPermission instead.
        "viewersCanCopyContent": bool,
        # A short description of the file.
        "description": str,
        # The last time the file was modified by anyone (RFC 3339 date-time).
        # Note that setting modifiedTime will also update modifiedByMeTime for the user.
        "modifiedTime": str,
        # Whether the file has been viewed by this user.
        "viewedByMe": bool,
        # Whether the file has been modified by this user.
        "modifiedByMe": bool,
        # The owners of the file. Currently, only certain legacy files may have more than one owner. Not populated for Team Drive files.
        "owners": Owners,
        # The time at which the file was created (RFC 3339 date-time).
        "createdTime": str,
        # The number of storage quota bytes used by the file. This includes the head revision as well as previous revisions with keepForever enabled.
        "quotaBytesUsed": str,
        # Whether the user has starred the file.
        "starred": bool,
        # A collection of arbitrary key-value pairs which are visible to all apps.
        "properties": dict,
        # The MD5 checksum for the content of the file. This is only applicable to files with binary content in Drive.
        "md5Checksum": str,
        # A static, unauthenticated link to the file's icon.
        "iconLink": str,
        # Additional metadata about image media, if available.
        "imageMediaMetadata": ImageMediaMetadata,
        # Identifies what kind of resource this is. Value: the fixed string "drive#file".
        "kind": "drive#file",
        # The name of the file. This is not necessarily unique within a folder. Note that for immutable items such as the top level folders of Team Drives, My Drive root folder, and Application Data folder the name is constant.
        "name": str,
        # A link for downloading the content of the file in a browser. This is only available for files with binary content in Drive.
        "webContentLink": str,
        # Information about a Drive user. # If the file has been explicitly trashed, the user who trashed it. Only populated for Team Drive files.
        "trashingUser": User,
        # The list of spaces which contain the file. The currently supported values are 'drive', 'appDataFolder' and 'photos'.
        "spaces": list,
        # List of permission IDs for users with access to this file.
        "permissionIds": list,
        # Whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner may trash a file, and other users cannot see files in the owner's trash.
        "trashed": bool,
        # Additional information about the content of the file. These fields are never populated in responses.
        "contentHints": ContentHints,
        # The final component of fullFileExtension. This is only available for files with binary content in Drive.
        "fileExtension": str,
        # Whether any users are granted file access directly on this file. This field is only populated for Team Drive files.
        "hasAugmentedPermissions": bool,
        # The full list of permissions for the file. This is only available if the requesting user can share the file. Not populated for Team Drive files.
        "permissions": Permissions,
        # The ID of the file's head revision. This is currently only available for files with binary content in Drive.
        "headRevisionId": str,
    }

    def __setattr__(self, name, value):
        if name in self.__keys:
            value_type = self.__keys[name]
            if isinstance(value, value_type):
                self[name] = value

    def __getattr__(self, name):
        if name in self.__keys:
            if name in self:
                return self[name]
            else:
                self[name] = self.__keys[name]()
                return self[name]
