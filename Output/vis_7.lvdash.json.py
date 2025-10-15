# Databricks notebook source
{
  "datasets": [
    {
      "name": "dataset_7",
      "displayName": "HPX Metric Dataset 7",
      "asset_name": "workspace.default.mv_hpx_metric_view"
    }
  ],
  "pages": [
    {
      "name": "page_7",
      "displayName": "HPX Metrics Dashboard",
      "layout": [
        {
          "widget": {
            "name": "widget_7",
            "queries": [
              {
                "name": "main_query",
                "query": {
                  "datasetName": "dataset_7",
                  "fields": [
                    {
                      "name": "date",
                      "expression": "DATE_TRUNC(\"DAY\", `date`)"
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
                  "scale": {
                    "type": "temporal"
                  }
                },
                "y": {
                  "fieldName": "active_users",
                  "displayName": "Active Users",
                  "scale": {
                    "type": "quantitative"
                  }
                }
              },
              "frame": {
                "showTitle": true,
                "title": "Active Users Over Time"
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
      "filters": []
    }
  ],
  "uiSettings": {
    "theme": {
      "widgetHeaderAlignment": "ALIGNMENT_UNSPECIFIED"
    }
  }
}
