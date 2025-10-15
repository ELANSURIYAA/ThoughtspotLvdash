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
            "name": "performance_trend_widget",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_view_dataset",
                  "fields": [
                    {
                      "name": "Event Date",
                      "expression": "DATE_TRUNC("MONTH", `Event Date`)"
                    },
                    {
                      "name": "Active Devices",
                      "expression": "MEASURE(`Active Devices`)"
                    },
                    {
                      "name": "Total Events",
                      "expression": "MEASURE(`Total Events`)"
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
                  "fieldName": "Event Date",
                  "displayName": "Month",
                  "scale": {
                    "type": "temporal"
                  }
                },
                "y": {
                  "fields": [
                    {
                      "fieldName": "Active Devices",
                      "displayName": "Active Devices"
                    },
                    {
                      "fieldName": "Total Events",
                      "displayName": "Total Events"
                    }
                  ],
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "Monthly Performance Trends"
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
