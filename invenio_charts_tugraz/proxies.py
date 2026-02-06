# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Charts TUGraz proxies."""

from typing import cast

from flask import current_app
from werkzeug.local import LocalProxy


def unproxy[T](obj: LocalProxy[T]) -> T:  # type: ignore[type-var]
    """Cast to the proxy bound object."""
    return cast(T, obj)


current_charts = LocalProxy(lambda: current_app.extensions["invenio-charts-tugraz"])
"""Proxy for the instantiated charts extension."""

current_rdm_charts_service = LocalProxy(lambda: current_charts.rdm_charts_service)
"""Proxy to the instantiated rdm-charts service."""
