# Databricks notebook source
{
  "name": "global_filter_001", 
  "displayName": "Global Filters",
  "layout": [
    {
      "widget": {
        "name": "widget_date_filter",
        "queries": [
          {
            "name": "dashboards/example_dashboard_id/datasets/example_dataset_example_date",
            "query": {
              "datasetName": "example_dataset",
              "fields": [
                {
                  "name": "Example Date",
                  "expression": "`Example Date`"
                },
                {
                  "name": "Example Date_associativity",
                  "expression": "COUNT_IF(`associative_filter_predicate_group`)"
                }
              ],
              "disaggregated": false
            }
          }
        ],
        "spec": {
          "version": 2,
          "widgetType": "filter-date-picker",
          "encodings": {
            "fields": [
              {
                "fieldName": "Example Date",
                "displayName": "Example Date",
                "queryName": "dashboards/example_dashboard_id/datasets/example_dataset_example_date"
              }
            ]
          },
          "selection": {
            "defaultSelection": {
              "values": {
                "dataType": "DATETIME",
                "values": [
                  {
                    "value": "2025-01-01T00:00:00.000"
                  }
                ]
              }
            }
          },
          "frame": {
            "showTitle": true,
            "title": "DateFilter"
          }
        }
      },
      "position": {
        "x": 0,
        "y": 0,
        "width": 1,
        "height": 2
      }
    },
    {
      "widget": {
        "name": "widget_region_filter",
        "queries": [
          {
            "name": "dashboards/example_dashboard_id/datasets/example_dataset_region",
            "query": {
              "datasetName": "example_dataset",
              "fields": [
                {
                  "name": "Region",
                  "expression": "`Region`"
                },
                {
                  "name": "Region_associativity",
                  "expression": "COUNT_IF(`associative_filter_predicate_group`)"
                }
              ],
              "disaggregated": false
            }
          }
        ],
        "spec": {
          "version": 2,
          "widgetType": "filter-single-select",
          "encodings": {
            "fields": [
              {
                "fieldName": "Region",
                "displayName": "Region",
                "queryName": "dashboards/example_dashboard_id/datasets/example_dataset_region"
              }
            ]
          },
          "frame": {
            "showTitle": true,
            "title": "RegionFilter"
          }
        }
      },
      "position": {
        "x": 0,
        "y": 2,
        "width": 1,
        "height": 2
      }
    }
  ],
  "pageType": "PAGE_TYPE_GLOBAL_FILTERS",
  "uiSettings": {
    "theme": {
      "widgetHeaderAlignment": "ALIGNMENT_UNSPECIFIED"
    }
  }
}
