# -*- coding: utf-8 -*-
#
# INVENIO-SIP2
# Copyright (C) 2021 UCLouvain
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

"""Common pytest fixtures and plugins."""

import pytest

from invenio_sip2.records.record import Server


@pytest.fixture(scope="module")
def server_data():
    """Server data."""
    return {
        'id': 'key_1',
        'host': '0.0.0.0',
        'port': 3006,
        'remote_app': 'test_ils',
        'server_name': 'server_sip2',
    }


@pytest.fixture(scope="module")
def server(app, server_data):
    """Load server record."""
    server = Server.create(
        server_data)
    return server
