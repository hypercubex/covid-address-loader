import requests

url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/CompulsoryTestingBuilding_View2/FeatureServer/0/query"

querystring = {"f":"json","returnIdsOnly":"true","returnCountOnly":"true","orderByFields":"GazetteDate_Date DESC,Status ASC,District_EN ASC","spatialRel":"esriSpatialRelIntersects","where":"1=1"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)