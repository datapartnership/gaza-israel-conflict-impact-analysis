# Gaza Mobility Analysis

This notebook aims to analyze mobility data from Mapbox in Gaza after the attacks on October 7th. The analysis is exploratory in nature and has not been validated with other data sources primarily due to the lack of availability of similar datasets for the time period in consideration.

Mobility data has often been used as a proxy for economic activity. In this case, it could shed light on
* The regions that saw activity in peacetime (Jan-June 2023) but no activity after October 7th, 2023.
* The regions that saw activity in the time of conflict. This could potentially indicate the congregation of people

The analysis is conducted at two types of aggregation - H3 grids at 0.73 sq. km and admin 2 regions at a weekly level. The temporal and spatial aggregation allows for comparison with Night Time Lights and damage indicators in the other notebooks.

## Data Description

### Mapbox Movement

Mapbox Movement is a global dataset of de-identified and aggregated mobile device activity. The dataset captures significant driving and non-driving mobile device activity aggregated into geographic tiles of 100-meter resolution (approximately one city block) and select Mapbox boundaries. Mapbox Movement typically relies on location data such as GPS coordinates, timestamps, and possibly other metadata attributes like speed, heading, and altitude. This data is typically collected from devices or sources that track location information over time.

The Mapbox Movement data used in this analysis is aggregated at a daily level and is represented in the form of an activity index.


#### Activity Levels

The activity index is a Mapbox proprietary movement indicator that reflects the level of activity in the specified time span and geographic region. The index is calculated as follows:

* Raw data is aggregated by time span and geography, representing the total daily activity within each geographic unit.
* The de-identification process is applied. In this process, small random noise is applied to total counts and geographic areas with counts below a minimum threshold are dropped.
    The de-identified telemetry data that provide the foundation for the Mapbox Movement product are well correlated with the movement of people about the world but do not provide a direct measure of the absolute number of people moving. Any decision made from Mapbox Movement data should be informed by a comparison, whether that’s a comparison of the activity difference between two blocks of a city on any given day, of the change in activity for a given location over some time span, or some combination of the above.

* A scaling factor is calculated by taking the 99.9th percentile of counts across all geographic units and days in the baseline time span.
* Data is normalized by dividing the counts for each day and geographic unit.
* All normalized counts are rounded to the sixth decimal digit.

Because the raw activity counts in a later time span may be greater than activity counts during the baseline time span, the activity index has a range of 0 - ∞. As an example, if the baseline time span is January 2020 and the 99.9th percentile count of total activity per grid tile in January 2020 was 1000 geolocation data points, then a grid tile that had 1500 data points on a day in March would have an activity index of 1.5 for that day.

The Mapbox Movement data set is based on de-identified underlying mobile device activity that grows and changes every day. Any mobility data set is inherently skewed between highly populated regions (urban and metro areas) and sparsely populated regions (rural areas). So instead of providing "raw counts" of measurements, a custom normalization process is applied. This process measures and smooths out the impact of otherwise unpredictable changes in mobile device usage and calculates an activity index, which is more appropriate for comparison across time spans.

#### Baselining

When activity levels are calculated in the context of Mapbox Movement, the baseline typically refers to the normal or expected levels of activity for a given area, time of day, day of the week, or other relevant factors. This baseline serves as a reference point for detecting deviations and anomalies in movement patterns or activity levels.
