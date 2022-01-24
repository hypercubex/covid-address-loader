import requests

url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/CompulsoryTestingBuilding_View2/FeatureServer/0/query"

# max page size is 2000, please add pagination

querystring = {"f":"json","resultOffset":"0","resultRecordCount":"8000","where":"((Status_Cal LIKE '%History%'))","orderByFields":"GazetteDate_Date DESC,Status ASC,District_EN ASC","outFields":"*","spatialRel":"esriSpatialRelIntersects"}

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