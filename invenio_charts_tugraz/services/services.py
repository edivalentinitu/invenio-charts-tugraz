# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Charts TUGraz services."""

from copy import deepcopy
from typing import Any, ParamSpecArgs

from invenio_rdm_records.services import RDMRecordService
from sqlalchemy import Identity


def _get_chart_oriented_aggregations(aggregations: dict) -> dict:
    figure_titles = []
    types = []
    values = []

    for title in aggregations:
        figure_titles.append(title)
        local_types = []
        local_values = []
        for type_obj in aggregations[title]["buckets"]:
            local_types.append(type_obj["key"])
            local_values.append(type_obj["doc_count"])
        types.append(deepcopy(local_types))
        values.append(deepcopy(local_values))

        local_types.clear()
        local_values.clear()

    return {
        "figure_titles": figure_titles,
        "types": types,
        "values": values,
    }


class RdmChartsService:
    """Rdm charts service."""

    def __init__(self, rdm_records_service: RDMRecordService, **__: Any) -> None:
        """Constructor."""
        self.rdm_records_service = rdm_records_service

    def get_rdm_records_chart_data(
        self,
        identity: Identity,
        params: ParamSpecArgs | None = None,
    ) -> dict[str, Any]:
        """Get the rdm-records chart data.

        Get the data from rdm-service then remodel it to fit the desired chart views.
        """
        rr_data = self.rdm_records_service.search(
            identity=identity,
            params=params,
        ).to_dict()

        return _get_chart_oriented_aggregations(rr_data.get("aggregations"))
