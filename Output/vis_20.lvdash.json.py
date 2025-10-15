# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_metric_dataset",
      "displayName": "HPX Metrics",
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
            "name": "performance_trend_chart",
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
                      "name": "total_revenue",
                      "expression": "MEASURE(`Total Revenue`)"
                    },
                    {
                      "name": "total_cost",
                      "expression": "MEASURE(`Total Cost`)"
                    },
                    {
                      "name": "profit_margin",
                      "expression": "MEASURE(`Profit Margin`)"
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
                      "fieldName": "total_revenue",
                      "displayName": "Total Revenue"
                    },
                    {
                      "fieldName": "total_cost",
                      "displayName": "Total Cost"
                    },
                    {
                      "fieldName": "profit_margin",
                      "displayName": "Profit Margin"
                    }
                  ],
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "Performance Metrics Over Time"
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
