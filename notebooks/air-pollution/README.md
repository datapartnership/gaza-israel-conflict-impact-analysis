# Air Pollution in West Bank

Air Pollution is typically measured by calculating the density of different pollutants in the atmosphere. Some of the commonly measured pollutants are NO2, O3 and particulate matter. Studies found NO2 levels as a useful proxy for economic activity (Deb, et.al., 2020). One of the reasons is because it is measured during the day when businesses are open and people are at work. It also stays close to the source of emissions —such as engines, vehicles or chimneys — and has a short atmospheric life (Ezran, et.al., 2023). Yailymova et.al., 2023 also posited that air quality and, in particular, levels of fine particulate matter (e.g., PM2.5 and PM 10 ) over cities can be a proxy for assessment of economic activity and density of city populations. NO2 along with other NOx reacts with other chemicals in the air to form both particulate matter and ozone. A 2020 study of cities in Sub-Saharan Africa finds that NO2 provides a useful, albeit “noisy”, real-time proxy measure of how COVID-19 has affected [economic activity](https://blogs.worldbank.org/developmenttalk/what-nitrogen-dioxide-emissions-tell-us-about-fragile-recovery-south-asia).

In this analysis, we observe the trends in monthly NO2 levels for West Bank from 2019 to 2024. The methodology to link economic activity to NO2 is still ongoing. This analysis is one step of it. 

## Common sources of NO2

- One of the chemical processes that generates NO2 is burning of fossil fuels (coal, gas and oil). Gives cars use this process, road traffic is the principal outdoor source of nitrogen dioxide (Jarvis et. al., 2010). 
- Diesel powered non-road equipment
- Industrial processes such as oil and gas production
- Coal fired power plants
- While the principal emissions of an aircraft are CO2 and H2O, other major emissions include nitric oxide and nitrogen dioxide (Miake-Lye & Hauglustaine, 2022).
- Any construction activity involving diesel fuel non-road mobile machinery will result in NOx emissions. 


## Data Description

### NO2 Data

Nitrogen oxides (NO2 and NO) are important trace gases in the Earth's atmosphere, present in both the troposphere and the stratosphere. They enter the atmosphere as a result of anthropogenic activities (notably fossil fuel combustion and biomass burning) and natural processes (wildfires, lightning, and microbiological processes in soils). Here, NO2 is used to represent concentrations of collective nitrogen oxides because during the daytime, i.e. in the presence of sunlight, a photochemical cycle involving ozone (O3) converts NO into NO2 and vice versa on a timescale of minutes.

The **total vertical column density of NO2** is calculated by taking the slant column density (SCD) of NO2, which is the amount of NO2 measured along the line of sight of the satellite instrument, and dividing it by the air mass factor (AMF), which corrects the slant column density for the effect of the path length and the scattering and absorption properties of the atmosphere. The Total Vertical Column Density (VCD) is typically given in molecules per square centimeter (molec/cm²).

Sentinel 5P collects data on pollutants such as NO2, SO2, CO and O3. This data can be extracted using Google Earth Engine. [Google Earth Engine](https://earthengine.google.com/) is a cloud-based geospatial analysis platform that enables users to visualize and analyze satellite images of our planet. We used JavaScript code to gather NO2 data from Google Earth Engine for each admin region. The raw data is then uploaded to [SharePoint](https://worldbankgroup.sharepoint.com/teams/DevelopmentDataPartnershipCommunity-WBGroup/Shared%20Documents/Forms/AllItems.aspx?csf=1&e=Yvwh8r&FolderCTID=0x012000CFAB9FF0F938A64EBB297E7E16BDFCFD&web=1&id=%2Fteams%2FDevelopmentDataPartnershipCommunity%2DWBGroup%2FShared%20Documents%2FProjects%2FData%20Lab%2FGaza%20Israel%20Conflict%20Impact%20Analysis%2FData%2Fair%5Fpollution&viewid=80cdadb3%2D8bb3%2D47ae%2D8b18%2Dc1dd89c373c5).

#### Data Access

* Dataset: [Sentinel-5P NRTI NO2: Near Real-Time Nitrogen Dioxide](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_NO2)
* Dataset Provider: [European Space Agency](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-5p-tropomi)
* Granularity: 1113.2 meters of granularity globally
* Frequency: Daily
* License: The use of Sentinel data is governed by the [Copernicus Sentinel Data Terms and Conditions](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice).
* **Data Access**: [The Project SharePoint](https://worldbankgroup.sharepoint.com/teams/DevelopmentDataPartnershipCommunity-WBGroup/Shared%20Documents/Forms/AllItems.aspx?csf=1&e=Yvwh8r&FolderCTID=0x012000CFAB9FF0F938A64EBB297E7E16BDFCFD&web=1&id=%2Fteams%2FDevelopmentDataPartnershipCommunity%2DWBGroup%2FShared%20Documents%2FProjects%2FData%20Lab%2FGaza%20Israel%20Conflict%20Impact%20Analysis&viewid=80cdadb3%2D8bb3%2D47ae%2D8b18%2Dc1dd89c373c5) currently hosts raw data queried from Google Earth Engine and can be accessed by all project team members.



## References

- Deb, P., Furceri, D., Ostry, J. D., & Tawk, N. (2020). The economic effects of COVID-19 containment measures.

- Ezran, Irene; Morris, Stephen D.; Rama, Martín; Riera-Crichton, Daniel. 2023. Measuring Global Economic Activity Using Air Pollution. Policy Research Working Papers; 10445. © World Bank, Washington, DC. http://hdl.handle.net/10986/39827 License: CC BY 3.0 IGO.

- Jarvis, D. J., Adamkiewicz, G., Heroux, M. E., Rapp, R., & Kelly, F. J. (2010). Nitrogen dioxide. In WHO guidelines for indoor air quality: Selected pollutants. World Health Organization.

- Miake-Lye, R. C., & Hauglustaine, D. (2022). Impacts of Aviation NOx Emissions on Air Quality, Health, and Climate. Innovation For a Green Transition-2022 Environmental Report.

- Yailymova, H., Kolotii, A., Kussul, N., & Shelestov, A. (2023, July). Air quality as proxy for assesment of economic activity. In IEEE EUROCON 2023-20th International Conference on Smart Technologies (pp. 89-92). IEEE.
