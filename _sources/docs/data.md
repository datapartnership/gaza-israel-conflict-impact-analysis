(data)=

# Datasets and Data Products Summary

## Datasets

**Datasets** refer to **all** datasets used in the analytics prepared for a project. The Datasets table includes a description of the data and their update frequency, as well as access links and contact information for questions about use and access. Users should not require any datasets not included in this table to complete the analytical work for the Data Good.

Following is list of all Datasets used in this Data Good:

```{note}
**Project Sharepoint** links are only accessible to the project team. For permissions to access these data, please write to the contact provided. The **Development Data Hub** is the World Bank's central data catalogue and includes meta-data and license information.
```

Where feasible, all datasets that can be obtained through the Development Data Hub have been placed in a special collection: *forthcoming*

All the datasets and data product images are placed in a [SharePoint folder]([Continue](https://worldbankgroup.sharepoint.com.mcas.ms/teams/DevelopmentDataPartnershipCommunity-WBGroup/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=Yvwh8r&cid=fccdf23e%2D94d5%2D48bf%2Db75d%2D0af291138bde&FolderCTID=0x012000CFAB9FF0F938A64EBB297E7E16BDFCFD&id=%2Fteams%2FDevelopmentDataPartnershipCommunity%2DWBGroup%2FShared%20Documents%2FProjects%2FData%20Lab%2FGaza%20Israel%20Conflict%20Impact%20Analysis&viewid=80cdadb3%2D8bb3%2D47ae%2D8b18%2Dc1dd89c373c5)) and access is given to the teams.

| ID  | Name                                              | License                                 | Description                                                        | Update Frequency                             | Access                                                                        | Contact                                                                                                     |
| --- | ------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | Palestine - Subnational Administrative Boundaries | Open                                    | Admin boundaries up to level 2                                     | Every year (Last updated in 20 October 2023) | [HDX](https://data.humdata.org/dataset/cod-ab-pse)                            | [Data Lab](mailto:datalab@worldbank.org)                                                                    |
| 2   | NASA's Black Marble Nighttime Lights              | Open                                    | Visible Infrared Imaging Radiometer Suite (VIIRS) Nighttime Lights | Daily                                        | [NASA's Black Marble](http://blackmarble.gsfc.nasa.gov)                       | [Geospatial Operations Support Team](mailto:gost@worldbank.org) or [Data Lab](mailto:datalab@worldbank.org) |
| 3   | ACLED                                             | Accessible to WB Staff using an API key | Crowdsourced Conflict Event Database                               | Daily                                        | [ACLED Data Export Tool](https://acleddata.com/data-export-tool/)             | [Data Lab](mailto:datalab@worldbank.org)                                                                    |
| 4   | WorldPop                                          | Open                                    | Population Density Estimates data                                  | 2020                                         | [WorldPop](https://hub.worldpop.org/geodata/summary?id=46388)                 | [Data Lab](mailto:datalab@worldbank.org)                                                                    |
| 5   | OpenStreetMaps                                    | Open                                    | Points of Interest                                                 | N/A                                          | [HdX](https://data.humdata.org/search?q=palestine&ext_search_source=main-nav) | [Data Lab](mailto:datalab@worldbank.org)                                                                    |
| 6   | Microsoft Building Footprints                     | Open                                    | Building Footprints                                                | N/A                                          | [GitHub](https://github.com/microsoft/GlobalMLBuildingFootprints)             | [Data Lab](mailto:datalab@worldbank.org)                                                                    |

### Data Availability Statement

Restrictions may apply to the data that support the findings of this study. Data received from the private sector through the Development Data Partnership are subject to the terms and conditions of the data license agreement and the "Official Use Only" data classification. These data are available upon request through the [Development Data Partnership](https://datapartnership.org). Licensing and access information for all other datasets are included in the documentation.

## Data Products Summary

**Data Products** are produced using the **Datasets** and can be further used to generate indicators and insights. All Data Products include documentation, references to original data sources (and/or information on how to access them), and a description of their limitations.

Following is a summary of Data Products used in this Data Good:

| ID  | Name                                       | Description                                                         | Limitations                                                                                                                                                                                    | Datasets Used (ID#) |
| --- | ------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| A   | Observed changes in NightLight Data        | Weekly aggregated trends in nighttime luminosity                    | Changes in nighttime lights could be driven by multiple factors—such as rescue efforts generating lights, to damages and people leaving high-hit areas causing a reduction in nighttime lights | 1,2                              |
| B   | Observed Impact of Conflict Events on PoIs | Daily activity of conflict events overlayed with Points of Interest | The Points of Interest are obtained from OSM, which is crowdsourced and does not have a fixed refresh schedule.                                                                                | 1,3,5                            |
| C   | Damage Assessment                          | Assessment of damage to buildings calculated from satellite imagery |                                                                                                                                                                                                |                                  |
