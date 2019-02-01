# -*- coding: utf-8 -*-
# import module snippets
from __future__ import print_function
from ..base import Base
from apiclient.discovery import build


# Scopes for devices
# Global scope for access to all Chrome device operations.
SCOPE_CHROME_DEVICE = "https://www.googleapis.com/auth/admin.directory.device.chromeos"
# Scope for only retrieving Chrome devices.
SCOPE_CHROME_DEVICE_READONLY = "https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly"
# Global scope for access to all mobile device operations.
SCOPE_MOBILE_DEVICE = "https://www.googleapis.com/auth/admin.directory.device.mobile"
# Scope for only retrieving mobile device
SCOPE_MOBILE_DEVICE_READONLY = "https://www.googleapis.com/auth/admin.directory.device.mobile.readonly"
# Scope for tasks that take an action on a mobile device.
SCOPE_MOBILE_DEVICE_ACTION = "https://www.googleapis.com/auth/admin.directory.device.mobile.action"

# Scopes for groups, group aliases, and group members
# Scope for access to all group member roles and information operations.
SCOPE_GROUP_MEMBER = "https://www.googleapis.com/auth/admin.directory.group.member"
# Scope for only retrieving group member roles and information.
SCOPE_GROUP_MEMBER_READONLY = "https://www.googleapis.com/auth/admin.directory.group.member.readonly"
# Global scope for access to all group operations, including group aliases and members.
SCOPE_GROUP = "https://www.googleapis.com/auth/admin.directory.group"
# Scope for only retrieving group, group alias, and member information.
SCOPE_GROUP_READONLY = "https://www.googleapis.com/auth/admin.directory.group.readonly"

# Scopes for organizational units
# Global scope for access to all organizational unit operations.
SCOPE_ORGANIZATION_UNIT = "https://www.googleapis.com/auth/admin.directory.orgunit"
# Scope for only retrieving organizational units.
SCOPE_ORGANIZATION_UNIT_READONLY = "https://www.googleapis.com/auth/admin.directory.orgunit.readonly"

# Scopes for users and user aliases
# Global scope for access to all user and user alias operations.
SCOPE_USER = "https://www.googleapis.com/auth/admin.directory.user"
# Scope for only retrieving users or user aliases.
SCOPE_USER_READONLY = "https://www.googleapis.com/auth/admin.directory.user.readonly"
# Scope for access to all user alias operations.
SCOPE_USER_ALIAS = "https://www.googleapis.com/auth/admin.directory.user.alias"
# Scope for only retrieving user aliases.
SCOPE_USER_ALIAS_READONLY = "https://www.googleapis.com/auth/admin.directory.user.alias.readonly"

# Scopes for user security features
# Scope for access to all application-specific password, OAuth token, and verification code operations.
SCOPE_USER_SECURITY = "https://www.googleapis.com/auth/admin.directory.user.security"

# Scopes for role management
# Scope for all roles management operations, including creating roles and role assignments.
SCOPE_ROLE = "https://www.googleapis.com/auth/admin.directory.rolemanagement"
# Scope for getting and listing roles, privileges, and role assignments.
SCOPE_ROLE_READONLY = "https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly"

# Scopes for custom user schemas
# Scope for access to all custom user schema operations.
SCOPE_USERSCHEMA = "https://www.googleapis.com/auth/admin.directory.userschema"
# Scope for only retrieving custom user schemas.
SCOPE_USERSCHEMA_READONLY = "https://www.googleapis.com/auth/admin.directory.userschema.readonly"

# Scopes for notifications
# Scope for access to all admin notification operations.
SCOPE_NOTIFICATION = "https://www.googleapis.com/auth/admin.directory.notifications"

# Scopes for customers
# Scope for access to all customer operations.
SCOPE_CUSTOMER = "https://www.googleapis.com/auth/admin.directory.customer"
# Scope for only retrieving customers.
SCOPE_CUSTOMER_READONLY = "https://www.googleapis.com/auth/admin.directory.customer.readonly"

# Scopes for domains
# Scope for access to all domain operations.
SCOPE_DOMAIN = "https://www.googleapis.com/auth/admin.directory.domain"
# Scope for only retrieving domains.
SCOPE_DOMAIN_READONLY = "https://www.googleapis.com/auth/admin.directory.domain.readonly"

#"Scopes for calendar resources
# Scope for access to all calendar resources operations.
SCOPE_CALENDAR = "https://www.googleapis.com/auth/admin.directory.resource.calendar"
# Scope for only retrieving calendar resources.
SCOPE_CALENDAR_READONLY = "https://www.googleapis.com/auth/admin.directory.resource.calendar.readonly"

SCOPES_GROUP = [
    SCOPE_GROUP_MEMBER,
    SCOPE_GROUP
]

SCOPES_USER = [
    SCOPE_USER,
    SCOPE_USER_ALIAS,
    SCOPE_USER_SECURITY,
    SCOPE_USERSCHEMA
]

SCOPES_READONLY = [
    SCOPE_CHROME_DEVICE_READONLY,
    SCOPE_MOBILE_DEVICE_READONLY,
    SCOPE_GROUP_MEMBER_READONLY,
    SCOPE_GROUP_READONLY,
    SCOPE_ORGANIZATION_UNIT_READONLY,
    SCOPE_USER_READONLY,
    SCOPE_USER_ALIAS_READONLY,
    SCOPE_ROLE_READONLY,
    SCOPE_USERSCHEMA_READONLY,
    SCOPE_CUSTOMER_READONLY,
    SCOPE_DOMAIN_READONLY,
    SCOPE_CALENDAR_READONLY
]


class DirectoryBase(Base):
    service = None
    domain = None

    def __init__(
        self,
        credential_path: str,
        scopes: list,
        domain: str,
        delegate_user: str = None
    ):
        """
        @params[in]     credentail_path GoogleのClient作成時のjsonのパス
        @params[in]     scopes          アクセスのスコープ一覧
        @params[in]     domain          アクセス対象となるドメイン名を指定
        @params[in]     delegate_user   アクセスユーザーを指定
        """
        super(DirectoryBase, self).__init__(
            credential_path,
            scopes,
            delegate_user
        )
        self.service = build('admin', 'directory_v1', http=self.http)
        self.domain = domain
