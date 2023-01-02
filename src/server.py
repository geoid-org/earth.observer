# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides a Basic HTTP Server for Earth Observer maintenance
===========================================================

...

Todo:
-----

Links:
------

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Dict, List, Union
from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler,
)
import sqlite3

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

# create the sqlite3 connection object
connection = sqlite3.connect("earth.db")

# verify we successfully created our connection object.
print(connection.total_changes)


# =============================================================================
# Functions
# =============================================================================

def server_run(
    server_class = HTTPServer,
    handler_class = BaseHTTPRequestHandler
):
    """
    Run Server Function
    ===================

    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def main():
    try:
        server_run()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
