# Estimating Damage to Buildings and Infrastructure

The situation in Gaza has escalated since the first Isreali attack on the 6t of October 2023. To allow World Bank Staff to estimate the damage undertaken to buildings and points of interest, the Data Lab team conducted a damage assessment using satellite imagery. 

## Data

The baseline data used for this analysis is as follows. These data act as an input to damage assessment, or add another layer of information to estimate the impact of damage to infrastructure and people of Gaza. 

1. ACLED: The Armed Conflict Location & Event Data Project (ACLED) is a disaggregated data collection, analysis, and crisis mapping project. ACLED collects information on the dates, actors, locations, fatalities, and types of all reported political violence and protest events around the world. The raw data is available through a license obtained by the World Bank. 

2. WorldPop: Estimated population density per grid-cell. The units are number of people per square kilometre based on country totals adjusted to match the corresponding official United Nations population estimates that have been prepared by the Population Division of the Department of Economic and Social Affairs of the United Nations Secretariat (2019 Revision of World Population Prospects).This data was produced in 2020. 

3. OpenStreetMaps: This is a crowdsourced dataset used to identify Points of Inetrest within Gaza. There is research that suggests that the OSM data for Israel is better than Gaza. However, it is currently the most accessible dataset we can use to estimate if Points of Interest took damage as a result of the attacks. 

4. Sentinel-1: Satellite imagery forms the core of this analysis. These data are obatined once in two weeks to detect changes to building structures. 

5. Google Earth Engine: The heights of te buildings were obtained from Google Earth Engine. 

## Methdology

The WB data Lab team developed a multi-step methodology, designed to reduce costs of conducting the analysis while maximizing certainty and frequency of results for damage inventories.  

Using freely available, bi-weekly satellite radar data (Sentinel-1), the team has been running a set of automated algorithms to identify significant “changes” to the underlying infrastructure (with the ESA WorldCover 10m dataset as the baseline) – especially changes in the heights and shapes of features. This analysis is still experimental; it can result in false positives and negatives.  

The team has overlaid radar change detection data with underlying baseline data (described in the previous section) and extracted a list of candidate infrastructure and facilities that may have been damaged. 


## Limitations

```{caution}
- This analysis has not yet been verified using a different datasource. The team is currently working on procuring extreemly high resolution imagery to verify whether the buildings identified as damaged have collapsed or experienced impact. 
```

ACLED is a crowdsourced dataset and is higly likely tat the numbers they are reporting are underreported. They keep changing their data based on local validation. OSM has multiple poliical and technical limitations for the current use case. However, it is one of the datasets that is publicly accessible and hence, is being used. Bittner (2017) outlined the Israeli domination of OSM entries, whereas there are far fewer mappers in Palestine. 