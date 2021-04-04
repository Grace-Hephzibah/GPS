import pygeoip

val = input("Enter the IP Address : \n")
print()

gip = pygeoip.GeoIP("GeoLiteCity.dat")

res = gip.record_by_addr(val)

for key,value in res.items():
    print('%s : %s', %(key, value)
