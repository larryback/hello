import urllib.request as ur

url = "http://www.weather.go.kr/cgi-bin/rdr_new/nph-rdr_sfc_pty_img?tm=201901081305&cmp=SFC&obs=HSR&qcd=PTY&acc=&aws=1&map=HR&color=C4&legend=1&size=640&zoom_level=0&zoom_x=0000000&zoom_y=0000000&ZRa=200&ZRb=1.6&rand=12160&gis=&rnexdisp=0&griddisp=0"

saveFile = "./images/weather2.png"
mem = ur.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")
