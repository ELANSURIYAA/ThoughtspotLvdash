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
            "name": "active_users_trend_widget",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_view_dataset",
                  "fields": [
                    {
                      "name": "event_date",
                      "expression": "DATE_TRUNC(\"MONTH\", `Event Date`)"
                    },
                    {
                      "name": "active_users",
                      "expression": "MEASURE(`Active Users`)"
                    },
                    {
                      "name": "new_users",
                      "expression": "MEASURE(`New Users`)"
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
                      "fieldName": "new_users",
                      "displayName": "New Users"
                    }
                  ],
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "User Activity Trends"
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
