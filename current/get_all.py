import requests

url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/CompulsoryTestingBuilding_View2/FeatureServer/0/query"

querystring = {"f":"json","resultOffset":"0","resultRecordCount":"8000","where":"((Status_Cal LIKE '%Active%'))","orderByFields":"GazetteDate_Date DESC,Status ASC,District_EN ASC","outFields":"*","spatialRel":"esriSpatialRelIntersects"}

payload = ""
headers = {
    "authority": "services8.arcgis.com",
    "cache-control": "max-age=0",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    # "cookie": "esri_gdpr=oneTrust; sat_track=true; pi_opt_in82202=true; _biz_uid=0820215d5d174064ace2a18ee7245273; _biz_nA=2; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _biz_pendingA=%5B%5D; OptanonAlertBoxClosed=2022-01-24T14:26:58.059Z; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jan+24+2022+22%3A26%3A58+GMT%2B0800+(Hong+Kong+Standard+Time)&version=6.29.0&isIABGlobal=false&hosts=&consentId=4eefb0b6-4ce3-499f-a5e9-d616add2bdb7&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false; AMCVS_ED8D65E655FAC7797F000101%40AdobeOrg=1; AMCV_ED8D65E655FAC7797F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C19017%7CMCMID%7C19989067364285283831096728235736388931%7CMCAAMLH-1643639218%7C3%7CMCAAMB-1643639218%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1643041618s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; s_sq=esriglobalext%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fdevelopers.arcgis.com%25252Fpython%25252Fguide%25252Fusing-the-gis%25252F%2526link%253DAccept%252520All%252520Cookies%2526region%253Donetrust-button-group%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fdevelopers.arcgis.com%25252Fpython%25252Fguide%25252Fusing-the-gis%25252F%2526oid%253DAccept%252520All%252520Cookies%2526oidt%253D3%2526ot%253DSUBMIT",
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)