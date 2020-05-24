# Viacom CPM/Facebook Page Analytics
![](https://d21buns5ku92am.cloudfront.net/33601/images/330519-VIMN%20logo-01222e-large-1568697452.png)

# Project Motivation
Viacom is an American media conglomerate, founded in 2005 and headquartered in New York City. Viacom has hundreds of subsidiaries, and each subsidiary has an associated Facebook page. When a vendor reaches out to Viacom to post an advertisement on one of those pages, Facebook charges Viacom a certain amount of CPM (Cost of Thousand Impressions), and Viacom charges the vendor a certain amount of CPM, usually around $25. Viacom needs an analytics team to make insights from the 444 pages regarding traffic, conversion funnels, demographics, and CPM in order to make better business decisions and optimize their pricing strategy by predicting how much CPM Facebook charges Viacom.

**The purpose of this project is:**
- **Build a model to predict the CPM** charged on Viacom by Facebook, in order to optimize Viacom's pricing strategies towards the ads posted by vendors
- **Build an end-to-end pipeline** to transform and load the page metrics data into an interactive Tableau dashboard to analyze conversion funnels and demographic cohorts, as well as to inform business decisions regarding page selection for ads

# Data
(because of the confidentiality agreement with Viacom, source data is not uploaded to Github)

**CPM data of 2018 and 2019**
- The page ID of Viacom's Facebook pages
- The CPM charged by Facebook for a certain page, on the certain day and demographic
- Demographic (gender, age group) of which the CPM was charged
- Date of when the CPM was charged

**Page Level data**
- Metrics recorded for pages, such as page impressions, page views, and click to action

# Results and Findings
The outcome of this project is:
- An interactive Tableau Dashboard to provide decision-making support regarding traffic, conversion funnels, demographics
- A CPM model and function that enables Viacom to calculate the total ad profit earned by a certain page within a given time period, with a variable of CPM charged by Viacom (default $25)

Below is a short demostration of the Tableau Dashboard that I created:
- The top left worksheet allows me to select ranked pages by conversion rates, and by clicking on the page, the demographic for the page populates below the worksheet
- The 444 pages are clustered into 3 cohorts, as shown on the right of the dashboard
  - cluster 1 has little traffic and high conversion rates
  - cluster 2 has the highest traffic and 0 conversion rate (cluster 2 has only 1 page)
  - cluster 3 has the medium amount of traffic and conversion rates
- By knowing from what cluster we want for the pages, we can filter the left worksheets by clusters to find the desired pages
according to different needs such as high page views low conversion rates, or low page views but high conversion rates

![](https://media.giphy.com/media/fsQTOc5PBpXbmkK59l/giphy.gif)
