# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metric_dataset",
      "displayName": "HPX Metrics",
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
            "name": "performance_chart",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_dataset",
                  "fields": [
                    {
                      "name": "date",
                      "expression": "`date`"
                    },
                    {
                      "name": "total_users",
                      "expression": "MEASURE(`total_users`)"
                    },
                    {
                      "name": "active_users",
                      "expression": "MEASURE(`active_users`)"
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
                  "displayName": "Date",
                  "scale": { "type": "temporal" }
                },
                "y": {
                  "fields": [
                    {
                      "fieldName": "total_users",
                      "displayName": "Total Users"
                    },
                    {
                      "fieldName": "active_users",
                      "displayName": "Active Users"
                    }
                  ],
                  "scale": { "type": "quantitative" }
                }
              },
              "frame": {
                "title": "User Activity Metrics",
                "showTitle": true
              }
            }
          },
          "position": { "x": 0, "y": 0, "width": 12, "height": 8 }
        }
      ],
      "pageType": "PAGE_TYPE_CANVAS",
      "filters": []
    }
  ],
  "uiSettings": {
    "theme": {
      "widgetHeaderAlignment": "ALIGNMENT_UNSPECIFIED"
    }
  }
}
