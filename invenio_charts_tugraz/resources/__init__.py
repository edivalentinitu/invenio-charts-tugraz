# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Resources module."""

from .config import RdmChartsResourceConfig
from .resource import RdmChartsResource

__all__ = (
    "RdmChartsResource",
    "RdmChartsResourceConfig",
)
