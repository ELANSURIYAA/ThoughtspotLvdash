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
      "name": "hpx_executive_summary",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "visualization_19",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_metric_dataset",
                  "fields": [
                    {
                      "name": "date_dimension",
                      "expression": "DATE_TRUNC(\"MONTH\", `Date`)"
                    },
                    {
                      "name": "metric_value",
                      "expression": "MEASURE(`Value`)"
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
                  "displayName": "Date",
                  "scale": {
                    "type": "temporal"
                  }
                },
                "y": {
                  "fieldName": "metric_value",
                  "displayName": "Metric Value",
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "HPX Executive Summary Metric Trend"
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
