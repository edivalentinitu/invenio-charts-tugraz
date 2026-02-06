// This file is part of InvenioRDM
// Copyright (C) 2026 Graz University of Technology
//
// Invenio RDM Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import Example, { RdmRecordsCharts } from "./rdmRecordsCharts";
import React from "react";
import ReactDOM from "react-dom";

const chartsConfig = document.getElementById("invenio-charts-tugraz-rdm");

const api_endpoint = chartsConfig.dataset.apiEndpoint;
const chart_titles = JSON.parse(chartsConfig.dataset.chartTitles);

chartsConfig &&
  ReactDOM.render(
    <RdmRecordsCharts
      apiUrl={`/api${api_endpoint}`}
      chartTitles={chart_titles}
    />,
    document.getElementById("invenio-charts-tugraz-rdm")
  );
