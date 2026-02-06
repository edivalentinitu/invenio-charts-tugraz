# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Resource configs."""

from typing import Final

from flask_resources import ResourceConfig
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema
from invenio_records_resources.services.base.config import ConfiguratorMixin

response_handlers = {
    **ResourceConfig.response_handlers,
    "application/vnd.inveniordm.v1+json": ResourceConfig.response_handlers[
        "application/json"
    ],
}


class RdmChartsResourceConfig(ResourceConfig, ConfiguratorMixin):
    """Runs resource config."""

    # Blueprint configuration
    blueprint_name: Final = "rdm_charts"
    url_prefix: Final = ""

    request_search_args: Final = SearchRequestArgsSchema

    # Response handling
    response_handlers: Final = response_handlers
    routes: Final = {
        "list": "/rdm-charts",
    }
