import urllib.request as ur

url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm={}&endTm={}"

rng = input("Input the start and end date>> ")
rngs = rng.split(' ')
if len(rngs) < 2:
    print("Error!!")
    exit()

startdt = rngs[0]
enddt = rngs[1]
url = url.format(startdt, enddt)
print(rng, startdt, enddt, url)

saveFile = "./images/weather.html"
mem = ur.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")