# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Services configs."""

from typing import Final

from invenio_records_resources.services import RecordServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin, FromConfig


class RdmChartsServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    """Rdm charts service configuration."""

    # will use rdm-records service for most calls.
    service_id: Final = "rdm-charts"

    # common configuration
    permission_policy_cls: Final = FromConfig("RDM_PERMISSION_POLICY")
