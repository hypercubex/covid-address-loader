import requests

url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/CompulsoryTestingBuilding_View2/FeatureServer/0/query"

# max page size is 2000, please add pagination

querystring = {"f":"json","resultOffset":"0","resultRecordCount":"8000","where":"1=1","orderByFields":"GazetteDate_Date DESC,Status ASC,District_EN ASC","outFields":"*","spatialRel":"esriSpatialRelIntersects"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)