import requests
import zipfile
import io

for x in list(range(1, 75)):
    for y in list(range(1,75)):
        data_met = {
            "Years[]": "2010Met",
            "levels[]":'0',
            "x":x,
            "y":y,

        }

        data_conc = {
            "Years[]": "2020Conc",
            "levels[]":'0',
            "x":x,
            "y":y,

        }

        r_met = requests.post("https://path.epd.gov.hk/download.php", data = data_met, verify=False)
        r_conc = requests.post("https://path.epd.gov.hk/download.php", data = data_conc, verify=False)

        z_met = zipfile.ZipFile(io.BytesIO(r_met.content))
        z_met.extractall(r"C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\scrapPath\All Data")
        
        z_conc = zipfile.ZipFile(io.BytesIO(r_conc.content))
        z_conc.extractall(r"C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\scrapPath\All Data")
