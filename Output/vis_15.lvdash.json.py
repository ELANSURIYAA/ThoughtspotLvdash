# Databricks notebook source
{
  "datasets": [
    {
      "name": "hpx_dataset_15",
      "displayName": "HPX Dataset 15",
      "asset_name": "workspace.default.mv_hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "hpx_page_15",
      "displayName": "HPX Executive Summary",
      "layout": [
        {
          "widget": {
            "name": "hpx_widget_15",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "hpx_dataset_15",
                  "fields": [
                    {
                      "name": "Event Date",
                      "expression": "DATE_TRUNC('MONTH', `Event Date`)"
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
                  "displayName": "Event Date",
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
                "title": "Active Devices and Total Events Over Time"
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
