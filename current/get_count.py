import requests

url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/CompulsoryTestingBuilding_View2/FeatureServer/0/query"

querystring = {"f":"json","resultOffset":"0","resultRecordCount":"8000","where":"((Status_Cal LIKE '%Active%'))","orderByFields":"GazetteDate_Date DESC,Status ASC,District_EN ASC","outFields":"*","spatialRel":"esriSpatialRelIntersects","returnIdsOnly":"true","returnCountOnly":"true"}

payload = ""
headers = {
    "authority": "services8.arcgis.com",
    "cache-control": "max-age=0",
    "sec-ch-ua-mobile": "?0",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)