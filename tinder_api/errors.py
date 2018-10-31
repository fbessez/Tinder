#!/usr/bin/env python3
"""
errors.py - API Client
"""


class StatusCodes(object):
    OK = 200
    MOVED_PERMANENTLY = 301
    BAD_REQUEST_ERROR = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404


class ClientError(Exception):
    """API Client"""
    pass


class AuthenticationError(ClientError):
    """Authentication error"""
    pass


class RequestError(ClientError):
    """Request error"""
    pass


class FBSuspiciousActivityError(AuthenticationError):
    """Unable to get Facebook access token due to blocked request

    See: https://github.com/fbessez/Tinder/issues/47
    """
    pass
