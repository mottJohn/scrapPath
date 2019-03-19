# About The Project
## Path Grid Data Download
scrapPath_XXX.py

The scripts are used to download [path grid data](https://path.epd.gov.hk/).

There are 5476 grids cover the entire Hong Kong area. Each grid contains meteorology data, concentration data, in 10 levels. Downloading by mouse clicking is definitely not ideal.

Currently, the programs are set to download 2010 meteorology data, 2020 concentration data in Level 1. Users can modify the setting easily by changing dictionary form.

## Calculate the Polluatants Concentration Per Grid according to AQOs
heatmap.py

I have reused the code from [Aermod](https://github.com/mottJohn/AERMOD) to calculate the concentrations of pollutants in each grid according to AQOs requirements. The data will then be plotted as a heatmap in ArcGIS.

Ref:

[AQOs](https://www.epd.gov.hk/epd/english/environmentinhk/air/air_quality_objectives/air_quality_objectives.html)

[RSP to FSP](https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_aqa_model_g5.html)

[Adjustments](https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_aqa_model_g1.html)


# Getting Start
1. Just download the whole thing and unzip
2. Run each postRequest.py file in anaconda prompt.

# To-dos
## Scap [Done]
* Currently, the script use selenium to click the webpage. However, further investigation found that it is actually a form submits to a server. Building a html form as request will be more reliable than clicking webpage, and possibility faster too. 

## Heatmap
* The current script runs very slow (An hour) since it loops through all the grips 8 times for all the AQOs requirements. Need to think of some smarter way to do it. (SOLVED: time reduced to 15 mins)

# Notes
* 8 hour average is rolling, but 24 hours averasge is not because we don't know which 8 hours belong to but we know which 24 hours belong to
* some ambiguity in 0-23 or 1 - 0(24) hour system. The program currently uses 1-0(24) which I am not sure actually. haha.