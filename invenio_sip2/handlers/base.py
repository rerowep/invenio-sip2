# -*- coding: utf-8 -*-
#
# INVENIO-SIP2
# Copyright (C) 2020 UCLouvain
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Handlers for customizing sip2 api."""

from ..proxies import current_sip2 as acs_system


def base_selfcheck_login_handler(remote, login, password, *kwargs):
    """Handle selfcheck login functionality.

    :param remote: remote ils
    :param login: The usename to login
    :param password: The password of tu user
    returns: login response
    """
    handler = acs_system.sip2_handlers.login_handler[remote]
    return handler(login, password, *kwargs)


def base_system_status_handler(remote, message, **kwargs):
    """Handle automatic circulation system status functionality.

    :param remote: remote ils
    :param message: The message object
    returns: login response
    """
    handler = acs_system.sip2_handlers.system_status_handler[remote]
    return handler(message.dumps(), **kwargs)


def base_validate_patron_handler(remote, patron_identifier, **kwargs):
    """Handle validate patron functionality.

    :param remote: remote ils
    :param patron_identifier: Identifier of the patron (e.g. id, barcode,...)
    returns: True if patron is valid else False
    """
    handlers = acs_system.sip2_handlers.patron_handlers[remote]
    return handlers['validate'](patron_identifier, **kwargs)


def base_authorize_patron_handler(remote, patron_identifier, password,
                                  **kwargs):
    """Handle authorize patron functionality.

    :param remote: remote ils
    :param patron_identifier: Identifier of the patron (e.g. id, barcode,...)
    :param password: The password of the patron
    returns: True if patron password is valid else False
    """
    handlers = acs_system.sip2_handlers.patron_handlers[remote]
    return handlers['authorize'](patron_identifier, password, **kwargs)


def base_enable_patron_handler(remote, patron_identifier, **kwargs):
    """Handle enable patron functionality.

    :param remote: remote ils
    :param patron_identifier: Identifier of the patron (e.g. id, barcode,...)
    returns: login response
    """
    handlers = acs_system.sip2_handlers.patron_handlers[remote]
    return handlers['enable'](patron_identifier, **kwargs)


def base_patron_handler(remote, patron_identifier, **kwargs):
    """Handle patron information functionality.

    :param remote: remote ils
    :param patron_identifier: Identifier of the patron (e.g. id, barcode,...)
    returns: Patron information
    """
    handlers = acs_system.sip2_handlers.patron_handlers[remote]
    return handlers['account'](patron_identifier, **kwargs)


def base_item_handler(remote, patron_identifier, item_identifier,  **kwargs):
    """Handle item information functionality.

    :param remote: remote ils
    :param item_identifier: Identifier of the item (e.g. id, barcode,...)
    returns: Item information
    """
    handlers = acs_system.sip2_handlers.item_handlers[remote]
    return handlers['item'](patron_identifier, item_identifier, **kwargs)


def base_circulation_handlers(remote, handler, patron_identifier,
                              item_identifier, **kwargs):
    """Handle checkout functionality.

    :param remote: remote ils
    :param handler: circulation handler (e.g.: checkin, checkout,...)
    :param patron_identifier: Identifier of the patron (e.g. id, barcode,...)
    :param item_identifier: Identifier of the item (e.g. id, barcode,...)
    returns: Circulation handler
    """
    handlers = acs_system.sip2_handlers.circulation_handlers[remote]
    return handlers[handler](patron_identifier, item_identifier, **kwargs)
