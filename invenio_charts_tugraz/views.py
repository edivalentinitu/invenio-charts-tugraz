# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Charts TUGraz views."""

from flask import Blueprint
from invenio_files_rest.app import Flask

blueprint = Blueprint(
    "invenio_charts_tugraz",
    __name__,
    template_folder="templates",
)


def create_rdm_charts_bp(app: Flask) -> Blueprint:
    """Create jobs blueprint."""
    ext = app.extensions["invenio-charts-tugraz"]
    return ext.rdm_charts_resource.as_blueprint()  # type: ignore[no-any-return]
