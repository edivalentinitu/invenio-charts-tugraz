# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Charts TUGraz resources."""

from typing import Any

from flask import g
from flask_resources import Resource, resource_requestctx, response_handler, route
from invenio_records_resources.resources.errors import ErrorHandlersMixin
from invenio_records_resources.resources.records.resource import (
    request_search_args,
)

from ..services import RdmChartsService
from . import RdmChartsResourceConfig


class RdmChartsResource(ErrorHandlersMixin, Resource):
    """Rdm charts resource."""

    def __init__(
        self,
        config: RdmChartsResourceConfig,
        service: RdmChartsService,
    ) -> None:
        """Constructor."""
        super().__init__(config)
        self.service = service

    def create_url_rules(self) -> list:
        """Create the URL rules for the OAI-PMH server resource."""
        routes = self.config.routes
        return [
            route("GET", routes["list"], self.get_rdm_records_chart_data),
        ]

    @request_search_args
    @response_handler(many=True)
    def get_rdm_records_chart_data(self) -> tuple[dict[str, Any], int]:
        """Perform a search."""
        identity = g.identity
        hits = self.service.get_rdm_records_chart_data(
            identity=identity,
            params=resource_requestctx.args,
        )
        return hits, 200
