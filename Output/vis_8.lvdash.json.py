# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metrics_dataset",
      "displayName": "HPX Metrics Dataset",
      "asset_name": "workspace.default.mv_hpx_metrics"
    }
  ],
  "pages": [
    {
      "name": "hpx_executive_summary",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "performance_metrics_chart",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metrics_dataset",
                  "fields": [
                    {
                      "name": "date",
                      "expression": "DATE_TRUNC("MONTH", `Date`)"
                    },
                    {
                      "name": "active_users",
                      "expression": "MEASURE(`Active Users`)"
                    },
                    {
                      "name": "engagement_rate",
                      "expression": "MEASURE(`Engagement Rate`)"
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
                  "fieldName": "date",
                  "displayName": "Month",
                  "scale": {
                    "type": "temporal"
                  }
                },
                "y": {
                  "fields": [
                    {
                      "fieldName": "active_users",
                      "displayName": "Active Users"
                    },
                    {
                      "fieldName": "engagement_rate",
                      "displayName": "Engagement Rate"
                    }
                  ],
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "Monthly Performance Metrics"
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
          "fieldName": "date",
          "displayName": "Date",
          "type": "FILTER",
          "isMandatory": false,
          "isSingleValue": false
        },
        {
          "fieldName": "region",
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
