import maxminddb

reader = maxminddb.open_database("Geoacumen-Country.mmdb")


ips = [
    "1.1.1.1",
    "216.244.66.248",
    "3.15.9.167",
    "2a02:587:a12:f000:e9bf:9b70:4fd:c66",
    "2002:b9ea:da6b:0:0:0:b9ea:da6b",
    "192.0.91.147",
]

for ip in ips:
    print(reader.get(ip))
