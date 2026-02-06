// This file is part of InvenioRDM
// Copyright (C) 2026 Graz University of Technology
//
// Invenio RDM Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React, { Component } from "react";
import PropTypes from "prop-types";
import { http } from "react-invenio-forms";
import { Button, Icon } from "semantic-ui-react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export class RdmRecordsCharts extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rdmRecordsData: {},
      activeIndex: 0,
    };
  }

  setActiveIndex = (index) => {
    this.setState({ activeIndex: index });
  };

  async fetchRdmRecordsChartsData() {
    try {
      const { apiUrl } = this.props;
      const hits = await http.get(apiUrl);
      return hits;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  async componentDidMount() {
    const response = await this.fetchRdmRecordsChartsData();
    this.setState({ rdmRecordsData: response.data });
  }

  render() {
    const { rdmRecordsData, activeIndex } = this.state;
    const { chartTitles } = this.props;

    if (!rdmRecordsData?.figure_titles) {
      return null;
    }

    const figureTitles = rdmRecordsData.figure_titles?.map(
      (title) => chartTitles[title]
    );
    const types = rdmRecordsData.types;
    const values = rdmRecordsData.values;

    const title = figureTitles[activeIndex];

    const chartData = types[activeIndex].map((type, idx) => ({
      type,
      count: values[activeIndex][idx],
    }));

    return (
      <div>
        <div style={{ textAlign: "center", marginBottom: "20px" }}>
          {figureTitles.map((title, i) => (
            <Button onClick={() => this.setActiveIndex(i)} size="medium">
              {title}
            </Button>
          ))}
        </div>

        <div
          style={{
            width: "100%",
            maxWidth: "800px",
            height: 600,
            margin: "0 auto",
          }}
        >
          <h3 style={{ textAlign: "center", marginBottom: "10px" }}>{title}</h3>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={chartData}
              margin={{ top: 20, right: 30, left: 20, bottom: 30 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="type" interval={0} width={30} />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="count" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    );
  }
}

RdmRecordsCharts.propTypes = {
  apiUrl: PropTypes.string.isRequired,
  chartTitles: PropTypes.object.isRequired,
};

export default RdmRecordsCharts;
