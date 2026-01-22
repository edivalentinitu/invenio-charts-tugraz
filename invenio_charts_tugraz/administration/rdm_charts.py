# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology
#
# Invenio-Charts-Tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio administration view module."""

from invenio_administration.views.base import (
    AdminResourceBaseView,
)


class JobsListView(AdminResourceBaseView):
    """Configuration for Jobs list view."""

    name = "charts"
    title = "Charts"
    menu_label = "Charts"
    category = "System"
    icon = "settings"
    template = "invenio_charts_tugraz/system/jobs/jobs-search.html"
