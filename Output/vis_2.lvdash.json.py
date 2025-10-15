# Databricks notebook source
{
  "datasets": [
    {
      "name": "dataset_001",
      "displayName": "HPX Metric Dataset",
      "asset_name": "workspace.default.mv_hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "page_001",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "widget_001",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "dataset_001",
                  "fields": [
                    {
                      "name": "date_dimension",
                      "expression": "DATE_TRUNC(\"MONTH\", `Date`)"
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
                  "fieldName": "date_dimension",
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
          "fieldName": "Date",
          "displayName": "Date",
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
