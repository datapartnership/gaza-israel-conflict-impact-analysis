# Damage to Buildings and Infrastructure

The situation in Gaza-Israel has escalated since October 2023. To allow World Bank Staff to estimate the damage undertaken to buildings and points of interest, the Data Lab team conducted a damage assessment using satellite Interferometric Synthetic Aperture Radar (InSAR) imagery.

You can now interact with this map by selecting/deselecting different damage layers to visualize where buildings are most impacted in the Gaza Strip. Upon visual inspection, you can see:

1. **Damage:** You can select and deselect the layers to see damages to roads, buildings and points of interest. The damage value ranges from $[0,1]$, with $1$ indicating higher level of damage.
2. **Conflict:** You can select this layer to view areas wit reported events and fatalities.

```{note}
The results shown in this analysis only reflect the damages until **Febraury 2, 2024**. As the team completes further analysis, the notebook will be updated. 
```

<iframe width="100%" height="500px" src="https://studio.foursquare.com/public/26ba3dfb-0770-4cc6-b6fa-2ee2878580fc/embed" frameborder="0" allowfullscreen></iframe>

```{figure} ../../docs/images/logo.png
---
height: 0px
---
Damage assessment in the Gaza Strip utilizing SAR imagery to evaluate the extent of destruction The damage map above is based on preliminary estimates and have not been verified through field survey or satellite imagery. It does not reflect the final estimations by the World Bank. Country borders or names do not necessarily reflect the World Bank Group's official position. This map is for illustrative purposes and does not imply the expression of any opinion on the part of the World Bank, concerning the legal status of any country or territory or concerning the delimitation of frontiers or boundaries.
```

## Data

The baseline data used for this analysis is as follows. These data act as an input to damage assessment, or add another layer of information to estimate the impact of damage to infrastructure and people of Gaza.

1. [ACLED](https://acleddata.com): The Armed Conflict Location & Event Data Project (ACLED) is a disaggregated data collection, analysis, and crisis mapping project. ACLED collects information on the dates, actors, locations, fatalities, and types of all reported political violence and protest events around the world. The raw data is available through a license obtained by the World Bank.

2. [WorldPop](https://www.worldpop.org): Estimated population density per grid-cell. The units are number of people per square kilometre based on country totals adjusted to match the corresponding official United Nations population estimates that have been prepared by the Population Division of the Department of Economic and Social Affairs of the United Nations Secretariat (2019 Revision of World Population Prospects).This data was produced in 2020.

3. [OpenStreetMap](https://wiki.openstreetmap.org/wiki/About_OpenStreetMap): This is a crowdsourced dataset used to identify Points of Inetrest within Gaza. There is research that suggests that the OSM data for Israel is better than Gaza. However, it is currently the most accessible dataset we can use to estimate if Points of Interest took damage as a result of the attacks.

4. [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview): Satellite imagery forms the core of this analysis. These data are obatined once in two weeks to detect changes to building structures.

5. [Google Earth Engine](https://earthengine.google.com): The heights of the buildings were obtained from Google Earth Engine.

(damage-assessment-methodology)=

## Methodology

The WB Data Lab Lab team developed a multi-step methodology, designed to reduce costs of conducting the analysis while maximizing certainty and frequency of results for damage inventories. Using freely available, bi-weekly satellite radar data, the team has been running a set of automated algorithms to identify significant “changes” to the underlying infrastructure – especially changes in the heights and shapes of features. This analysis is still experimental; it can result in false positives and negatives.

The damage assessment analysis relies on the similarity measure computed using SAR medium resolution and openly accessible [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview) and the employed methodology can be split into 3 steps:

### 1. Image similarity computation

This similarity measurement, namely interferometric coherence ranging from $[0,1]$, provides values of high similarity (usually higher than $0.6$) over structures on that had not suffered almost any variation, as for example buildings or man-made structures, while exhibits lower values (usually lower than $0.4$) over forest and agricultural areas (especially on large time separation between the acquisition time of the satellite data) over water (usually lower than $0.3$) bodies already between consecutive acquisitions.

We have employed all the Copernicus [Sentinel-1](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/overview) data acquired over the Gaza strip, which consists in 3 satellite orbits, namely ascending orbit 87 and 160 and descending orbit 94, and we computed all the similarity maps with respect to the first image available for each of the orbits acquired in September 2022 to have time series measurements that will allow us to use a statistical approach to determine changes using anomaly detection method. Each orbit has 12 days repeat pass, so new updated products can be added regularly every 12 days.

```{figure} ../../docs/images/damage-assessment-calendar.png
---
---
Calendar with Copernicus Sentinel-1 acquisition dates after the war started on past 7th October 2023 until 9th January 2023. 
```

### 2. Change detection based on time series statistics

For the time series change detection, we have computed all the data pre-war September 2022 until end September 2023 to compute the statistics in non-war situation, and to use those statistics to classify the newer data acquired during the war period October 2023 until the present time with pixels for which had been detected a change (potentially attributable to war damage) using anomaly detection method with different thresholds (i.e. 3 sigma rule and 2.5 sigma rule).  

The 3-sigma rule is more conservative and provides more conservative results with false alarms regarding the change detections. 3-sigma rule considers as anomaly values that are lower than the average minus 3 times their standard deviation which it means that are lower than the 99.6% of the value’s normal distribution (measured in non-war conditions) or are included in the 0.15% of possible values, and hence, detected as anomalous. Similarly happens for the 2.5 sigma rule, which pixels are considered as anomaly the ones being the 0.65%. This 2.5 sigma rule may increase some more false alarms, while the 3 sigma rule is considered more conservative anomaly detection rule. See example of this empirical rule below.

```{figure} ../../docs/images/damage-assessment-empirical-rule.jpg
---
scale: 50%
---
Illustration of the empirical rule
```

### 3. Infrastructural damage assessment using the change maps and the vector layers

For the final assessment of infrastructural damage, in roads, points of interest or buildings, the different layers are overlaid and computed whether each feature has been damage or not. For the different features we have computed their potential damage as follows:

- In case of roads, the layer is split into 10 meters roads, and it is computed whether each of the segments had been damaged or not,

- In case of the points-of-interest (POI):

  - Point POIs have been attributed a buffer of 10-meter radius and are overlaid to the change map to detect whether they are likely damaged or not.

  - Area POIs have been overlaid with the change map to detect whether they are likely damaged or not.

- In case of buildings,

  - Using OpenStreetMap building layer, they are overlaid with the change map and computed which is the percentage (in $[0,1]$ range) of their area which are likely damaged. OSM layers comes also with their possible landuse information that is provided by the OSM layers.

  - Using Microsoft footprint layer, they are overlaid with the change map and computed which is the percentage (in $[0,1]$ range) of their area which are likely damaged, but they do not come with landuse information.

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
