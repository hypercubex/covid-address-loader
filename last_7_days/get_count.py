import requests

url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/CompulsoryTestingBuilding_View2/FeatureServer/0/query"

querystring = {"f":"json","returnIdsOnly":"true","returnCountOnly":"true","orderByFields":"GazetteDate_Date DESC,Status ASC,District_EN ASC","spatialRel":"esriSpatialRelIntersects","where":"((Status_Cal LIKE '%7%'))"}

payload = ""
headers = {
    "authority": "services8.arcgis.com",
    "dnt": "1",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept": "*/*",
    "origin": "https://chp-dashboard.geodata.gov.hk",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://chp-dashboard.geodata.gov.hk/",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)