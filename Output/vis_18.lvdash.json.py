# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metric_view_dataset",
      "displayName": "HPX Metric View",
      "asset_name": "workspace.default.hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "hpx_executive_summary_page",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "active_devices_trend_widget",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_view_dataset",
                  "fields": [
                    {
                      "name": "event_date",
                      "expression": "DATE_TRUNC(\"DAY\", `Event Date`)"
                    },
                    {
                      "name": "active_devices",
                      "expression": "MEASURE(`Active Devices`)"
                    },
                    {
                      "name": "cumulative_devices",
                      "expression": "SUM(MEASURE(`Active Devices`)) OVER (ORDER BY DATE_TRUNC(\"DAY\", `Event Date`) ROWS UNBOUNDED PRECEDING)"
                    }
                  ],
                  "disaggregated": false
                }
              }
            ],
            "spec": {
              "version": 3,
              "widgetType": "line",
              "encodings": {
                "x": {
                  "fieldName": "event_date",
                  "displayName": "Event Date",
                  "scale": { "type": "temporal" }
                },
                "y": {
                  "fields": [
                    {
                      "fieldName": "active_devices",
                      "displayName": "Active Devices"
                    },
                    {
                      "fieldName": "cumulative_devices",
                      "displayName": "Cumulative Devices"
                    }
                  ],
                  "scale": { "type": "quantitative" }
                }
              },
              "frame": {
                "title": "Active Devices Trend",
                "showTitle": true
              }
            }
          },
          "position": { "x": 0, "y": 0, "width": 12, "height": 8 }
        }
      ],
      "pageType": "PAGE_TYPE_CANVAS",
      "filters": [
        {
          "fieldName": "Event Date",
          "displayName": "Event Date",
          "type": "FILTER",
          "isMandatory": false,
          "isSingleValue": false
        },
        {
          "fieldName": "Region",
          "displayName": "Region",
          "type": "FILTER",
          "isMandatory": false,
          "isSingleValue": true
        }
      ]
    }
  ],
  "uiSettings": {
    "theme": {
      "widgetHeaderAlignment": "ALIGNMENT_UNSPECIFIED"
    }
  }
}
