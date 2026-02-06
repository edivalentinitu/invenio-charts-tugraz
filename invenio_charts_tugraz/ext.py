# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Charts TUGraz extension."""

from flask import Flask
from invenio_rdm_records.proxies import current_rdm_records_service
from invenio_rdm_records.services import RDMRecordService

from .proxies import unproxy
from .resources import RdmChartsResource, RdmChartsResourceConfig
from .services import RdmChartsService, RdmChartsServiceConfig


def _get_rdm_records_service() -> RDMRecordService:
    return unproxy(current_rdm_records_service)


class InvenioChartsTugraz:
    """Invenio-Charts-Tugraz extension."""

    def __init__(self, app: Flask | None = None) -> None:
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Flask application initialization."""
        self.init_services(app)
        self.init_resource(app)
        app.extensions["invenio-charts-tugraz"] = self

    def init_services(self, app: Flask) -> None:
        """Initialize services."""
        self.rdm_charts_service = RdmChartsService(
            config=RdmChartsServiceConfig.build(app),
            rdm_records_service=_get_rdm_records_service(),
        )

    def init_resource(self, app: Flask) -> None:
        """Initialize resources."""
        self.rdm_charts_resource = RdmChartsResource(
            RdmChartsResourceConfig.build(app),
            self.rdm_charts_service,
        )
