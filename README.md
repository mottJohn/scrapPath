# About The Project

The scripts are used to download [path grid data](https://path.epd.gov.hk/).

There are 5476 grids cover the entire Hong Kong area. Each grid contains meteorology data, concentration data, in 10 levels. Downloading by mouse clicking is definitely not ideal.

Currently, the programs are set to download 2010 meteorology data, 2020 concentration data in Level 1. Users can modify the setting easily by changing the xPath.

There are 5 copies of the script. They are essentially the same with the difference on grid numbers. Each script is responsible for downloading 1000 grids. The benefits of doing so are, it speeds up the downloading process; it is more forgiving in failure (meaning, if you failed, it is easier to find and fix).

The downloading file is .zip. The program will extract the zips for you and delete them once it is done.

# Getting Start
1. Just download the whole thing and unzip
2. Run each .py files in anaconda prompt.