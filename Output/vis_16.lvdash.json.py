# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metric_dataset",
      "displayName": "HPX Metrics",
      "asset_name": "workspace.default.mv_hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "hpx_overview_page",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "hpx_trend_chart",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_dataset",
                  "fields": [
                    {
                      "name": "date",
                      "expression": "DATE_TRUNC('MONTH', `Date`)"
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
                "title": "User Growth Trends"
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
