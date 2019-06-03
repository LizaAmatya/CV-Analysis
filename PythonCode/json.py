import urllib2
import simplejson as json

def printResults(data):
    thejson = json.loads(data)

    if "title" in thejson["metadata"]:
        print(thejson["metadata"]["title"])

    count = thejson["metadata"]["count"]
    print (str(count) + "events recorded")

    for i in thejson["features"]:
        print(i["properties"]["place"])
        print("-----\n")

# for i in thejson["Skill"]:
#     if i["properties"]["mag"] >= 4.0:
#         print()


def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson"

    webUrl = urllib2.urlopen(urlData)
    print ("resultcode: " + str(webUrl.getcode()))
    data = webUrl.read()
    printResults(data)

if __name__ == "__main__" :
    main()

