# About The Project
## Path Grid Data Download
scrapPath_XXX.py

The scripts are used to download [path grid data](https://path.epd.gov.hk/).

There are 5476 grids cover the entire Hong Kong area. Each grid contains meteorology data, concentration data, in 10 levels. Downloading by mouse clicking is definitely not ideal.

Currently, the programs are set to download 2010 meteorology data, 2020 concentration data in Level 1. Users can modify the setting easily by changing the xPath.

There are 5 copies of the script. They are essentially the same with the difference on grid numbers. Each script is responsible for downloading 1000 grids. The benefits of doing so are, it speeds up the downloading process; it is more forgiving in failure (meaning, if you failed, it is easier to find and fix).

The downloading file is .zip. The program will extract the zips for you and delete them once it is done.

## Calculate the Polluatants Concentration Per Grid according to AQOs
heatmap.py

I have reused the code from [Aermod](https://github.com/mottJohn/AERMOD) to calculate the concentrations of pollutants in each grid according to AQOs requirements. The data will then be plotted as a heatmap in ArcGIS.

Ref:

[AQOs](https://www.epd.gov.hk/epd/english/environmentinhk/air/air_quality_objectives/air_quality_objectives.html)

[RSP to FSP](https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_aqa_model_g5.html)

[Adjustments](https://www.epd.gov.hk/epd/english/environmentinhk/air/guide_ref/guide_aqa_model_g1.html)


# Getting Start
1. Just download the whole thing and unzip
2. Run each .py files in anaconda prompt.

# To-dos
## Scap
* Currently, the script use selenium to click the webpage. However, further investigation found that it is actually a form submits to a server. Building a html form as request will be more reliable than clicking webpage, and possibility faster too.

## Heatmap
* The current script runs very slow since it loops through all the grips 8 times for all the AQOs requirements. Need to think of some smarter way to do it.