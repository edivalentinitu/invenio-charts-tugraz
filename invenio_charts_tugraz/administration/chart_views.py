# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio administration view module."""

from typing import Final

from invenio_administration.views.base import (
    AdminResourceBaseView,
)


class RdmChartsView(AdminResourceBaseView):
    """Configuration for Jobs list view."""

    name: Final = "charts"
    title: Final = "RDM Charts"
    menu_label: Final = "RDM Charts"
    category: Final = "Statistics"
    icon: Final = "chart bar"
    request_headers: Final = {"Accept": "application/json"}
    template: Final = "invenio_charts_tugraz/rdm-charts.html"
    resource_config: Final = "rdm_charts_resource"
    api_endpoint: Final = "/rdm-charts"
    chart_titles: Final = {
        "access_status": "Access Status",
        "file_type": "File Type",
        "resource_type": "Resource Type",
    }

    def get(self) -> str:
        """Update GET view method with specific fields."""
        return self.render(  # type: ignore[no-any-return]
            **{
                "api_endpoint": self.api_endpoint,
                "chart_titles": self.chart_titles,
            },
        )
