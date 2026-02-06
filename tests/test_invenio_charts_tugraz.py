# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology.
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from invenio_charts_tugraz import InvenioChartsTugraz, __version__


def test_version() -> None:
    """Test version import."""
    assert __version__


def test_init() -> None:
    """Test extension initialization."""
    app = Flask("testapp")
    InvenioChartsTugraz(app)
    assert "invenio-charts-tugraz" in app.extensions

    app = Flask("testapp")
    ext = InvenioChartsTugraz()
    assert "invenio-charts-tugraz" not in app.extensions
    ext.init_app(app)
    assert "invenio-charts-tugraz" in app.extensions
