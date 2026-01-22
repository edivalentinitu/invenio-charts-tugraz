# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology.
#
# Invenio-Jobs is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JS/CSS Webpack bundles for charts-tugraz."""

from invenio_assets.webpack import WebpackThemeBundle

administration = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "invenio-charts-tugraz": "./js/invenio_charts_tugraz/administration/index.js",
            },
            dependencies={
                "react-invenio-forms": "^4.0.0",
                "recharts": "^3.0.0",
            },
        ),
    },
)
