# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metric_dataset",
      "displayName": "HPX Metric Dataset",
      "asset_name": "workspace.default.HPX_metric_view"
    }
  ],
  "pages": [
    {
      "name": "executive_summary_page",
      "displayName": "Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "hpx_visualization_widget",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_dataset",
                  "fields": [
                    {
                      "name": "date",
                      "expression": "DATE_TRUNC('MONTH', `date`)"
                    },
                    {
                      "name": "total_users",
                      "expression": "MEASURE(`total_users`)"
                    },
                    {
                      "name": "active_users",
                      "expression": "MEASURE(`active_users`)"
                    },
                    {
                      "name": "new_users",
                      "expression": "MEASURE(`new_users`)"
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
                    },
                    {
                      "fieldName": "new_users",
                      "displayName": "New Users"
                    }
                  ],
                  "scale": { "type": "quantitative" }
                }
              },
              "frame": {
                "title": "User Metrics Over Time",
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
