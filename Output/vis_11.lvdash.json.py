# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metric_view",
      "displayName": "HPX Metric View",
      "asset_name": "workspace.default.hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "executive_summary",
      "displayName": "Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "widget_11",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_view",
                  "fields": [
                    {
                      "name": "month",
                      "expression": "DATE_TRUNC(\"MONTH\", `Date`)"
                    },
                    {
                      "name": "total_active_devices",
                      "expression": "MEASURE(`Active Devices`)"
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
                  "fieldName": "month",
                  "displayName": "Month",
                  "scale": {
                    "type": "temporal"
                  }
                },
                "y": {
                  "fieldName": "total_active_devices",
                  "displayName": "Total Active Devices",
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "Monthly Active Devices"
              }
            }
          },
          "position": {
            "x": 0,
            "y": 0,
            "width": 12,
            "height": 8
          }
        }
      ],
      "pageType": "PAGE_TYPE_CANVAS",
      "filters": [
        {
          "fieldName": "Date",
          "displayName": "Date",
          "type": "FILTER",
          "isMandatory": false,
          "isSingleValue": false
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
