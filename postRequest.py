import grequests
import zipfile
import io

for i in range(1, 75):
    async_list = []
    for x in range(i, i+1):
        for y in range(1,75):
            print("Downloading {},{}".format(x,y))
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
            r_met = grequests.post("https://path.epd.gov.hk/download.php", data = data_met, verify=False)
            r_conc = grequests.post("https://path.epd.gov.hk/download.php", data = data_conc, verify=False)
            async_list.append(r_met)
            async_list.append(r_conc)
    
    req = grequests.map(async_list)

    for response in req:
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall(r"C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\scrapPath\All Data")
    