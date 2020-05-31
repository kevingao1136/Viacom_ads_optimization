# Viacom Ads Optimization
![](https://d21buns5ku92am.cloudfront.net/33601/images/330519-VIMN%20logo-01222e-large-1568697452.png)

# Project Motivation
Viacom is an American media conglomerate, founded in 2005 and headquartered in New York City. Viacom has hundreds of subsidiaries, and each subsidiary has an associated Facebook page. When a vendor reaches out to Viacom to post an advertisement on one of those pages, Facebook charges Viacom a certain amount of CPM (Cost of Thousand Impressions), and Viacom charges the vendor a certain amount of CPM, usually around $25. Viacom needs an analytics team to make insights from the 444 pages regarding traffic, conversion funnels, demographics, and CPM in order to make better business decisions and optimize their pricing strategy by predicting how much CPM Facebook charges Viacom.

**The purpose of this project is:**
- **Build a model to predict the CPM** charged on Viacom by Facebook, in order to optimize Viacom's advertisement costs
- **Build a Tableau Dashboard to show page metrics and demographic** to inform business decisions regarding page selection for ads

# Data
(because of the confidentiality agreement with Viacom, source data is not uploaded to Github)

**CPM data from 2018-04 and 2019-02**
- The page ID of Viacom's Facebook pages
- The CPM charged by Facebook for a certain page, on the certain day and demographic
- Demographic (gender, age group) of which the CPM was charged
- Date of when the CPM was charged

**Page Metrics data from 2018-01 to 2019-04**
- Metrics recorded for pages, such as page impressions, page views, and click to action

# Results and Findings
The outcome of this project is:
- An interactive Tableau Dashboard to provide decision-making support regarding page impressions per day, clicks per day, demographics
- A CPM model that enables Viacom to calculate CPM charged by Facebook given the following features: age, gender, day, month, year

Below is a screenshot of the Tableau Dashboard created. The Page Metrics on top can be filtered by clusters: I conducted K-Means clustering to cluster all 444 pages into 4 clusters, here are the characteristics of each cluster:

Cluster0: Low impressions and low clicks
Cluster1: Medium impressions and high clicks
Cluster2: High impressions and 0 clicks
Cluster3: Medium impressions and medium clicks
![](https://github.com/kevingao1136/Viacom_ads_optimization/blob/master/tableau_data/Dashboard.png)
