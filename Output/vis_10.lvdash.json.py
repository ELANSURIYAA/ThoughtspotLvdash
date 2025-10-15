# Databricks notebook source
{
  "datasets": [
    {
      "name": "dataset_10",
      "displayName": "HPX Metric Dataset",
      "asset_name": "workspace.default.mv_hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "page_10",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "widget_10",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "dataset_10",
                  "fields": [
                    {
                      "name": "date",
                      "expression": "DATE_TRUNC(\"MONTH\", `date`)"
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
                "title": "Monthly User Activity"
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
