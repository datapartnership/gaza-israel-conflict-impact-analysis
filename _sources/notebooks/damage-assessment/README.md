# Estimating Damage to Buildings and Infrastructure

The situation in Gaza-Israel has escalated since October 2023. To allow World Bank Staff to estimate the damage undertaken to buildings and points of interest, the Data Lab team conducted a damage assessment using satellite Interferometric Synthetic Aperture Radar (InSAR) imagery. 

## Data

The baseline data used for this analysis is as follows. These data act as an input to damage assessment, or add another layer of information to estimate the impact of damage to infrastructure and people of Gaza. 

1. [ACLED](https://acleddata.com): The Armed Conflict Location & Event Data Project (ACLED) is a disaggregated data collection, analysis, and crisis mapping project. ACLED collects information on the dates, actors, locations, fatalities, and types of all reported political violence and protest events around the world. The raw data is available through a license obtained by the World Bank. 

2. [WorldPop](https://www.worldpop.org): Estimated population density per grid-cell. The units are number of people per square kilometre based on country totals adjusted to match the corresponding official United Nations population estimates that have been prepared by the Population Division of the Department of Economic and Social Affairs of the United Nations Secretariat (2019 Revision of World Population Prospects).This data was produced in 2020. 

3. [OpenStreetMap](https://wiki.openstreetmap.org/wiki/About_OpenStreetMap): This is a crowdsourced dataset used to identify Points of Inetrest within Gaza. There is research that suggests that the OSM data for Israel is better than Gaza. However, it is currently the most accessible dataset we can use to estimate if Points of Interest took damage as a result of the attacks. 

4. [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview): Satellite imagery forms the core of this analysis. These data are obatined once in two weeks to detect changes to building structures. 

5. [Google Earth Engine](https://earthengine.google.com): The heights of the buildings were obtained from Google Earth Engine. 

## Methodology

The WB data Lab team developed a multi-step methodology, designed to reduce costs of conducting the analysis while maximizing certainty and frequency of results for damage inventories. Using freely available, bi-weekly satellite radar data ([Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview)), the team has been running a set of automated algorithms to identify significant “changes” to the underlying infrastructure (with the [ESA WorldCover 10m](https://esa-worldcover.org/en) dataset as the baseline) – especially changes in the heights and shapes of features. This analysis is still experimental; it can result in false positives and negatives.  

The team has overlaid radar change detection data with underlying baseline data (described in the previous section) and extracted a list of candidate infrastructure and facilities that may have been damaged. 


## Limitations

```{important}
The following damage assessment maps are based on preliminary estimates and have not been verified through field survey or satellite imagery. They do not reflect the final estimations by the [World Bank](https://www.worldbank.org/en/country/westbankandgaza). The project team is currently working on procuring high resolution imagery to verify whether the buildings identified as damaged have collapsed or experienced impact. 
```

```{caution}
Using OpenStreetMap (OSM) and Interferometric Synthetic Aperture Radar (InSAR) for estimating building damage has its strengths but also several limitations:

- **Incomplete Data:**
    - **Coverage Discrepancies:** OSM data might lack comprehensive coverage, especially in certain regions or areas with limited community input or verification. This can lead to incomplete or outdated information about buildings. For instance, {cite:t}`BITTNER201734` outlined the Israeli domination of OSM entries, whereas there are far fewer mappers in Palestine.
    - **Quality Variability:** Data quality can vary significantly as it relies on volunteer contributions. Accuracy in mapping may vary, leading to inconsistencies or errors in identifying buildings

- **Temporal Limitations:**
    - **Data Timeliness:** OSM data might not be up to date due to infrequent updates or changes in the landscape that haven't been reflected yet.
    - **InSAR Timing:** InSAR data might not capture the most recent changes or damages, especially in rapidly evolving situations where damage continues to occur after the data collection period.
    
- **Contextual Understanding:**
    - **Local Knowledge:** OSM data might lack contextual information crucial for assessing damages accurately, such as the original state of buildings or variations in construction materials.
    - **Verification Challenges:** Verifying damages solely based on remote sensing data might lack the on-ground verification necessary for a comprehensive understanding of the situation.

- **Conflict Data**
ACLED is a crowdsourced dataset and is higly likely that the numbers are underreported. ACLED keep changing their data based on local validation. 
```

## References

```{bibliography}
:filter: docname in docnames
```
