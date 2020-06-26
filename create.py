import netaddr
import mmdbencoder
import csv
from collections import namedtuple
import subprocess


Row = namedtuple("Row", ["start", "end", "as_num", "iso_code", "as_description"])

subprocess.call(["curl", "-O", "https://iptoasn.com/data/ip2asn-combined.tsv.gz"])
subprocess.call(["gunzip", "-f", "ip2asn-combined.tsv.gz"])


enc = mmdbencoder.Encoder(
    6,  # IP version
    32,  # Size of the pointers
    "Geoacumen-Country",  # Name of the table
    ["en"],  # Languages
    {
        "en": "Geoacumen - Open Source IP to country mapping database by Kevin Chung"
    },  # Description
    compat=True,
)

print("Building data")
with open("ip2asn-combined.tsv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter="\t")
    for row in csv_reader:
        row = Row(*row)
        cidrs = netaddr.iprange_to_cidrs(row.start, row.end)
        for cidr in cidrs:
            data = enc.insert_data({"country": {"iso_code": row.iso_code}})
            enc.insert_network(cidr, data, strict=False)


print("Writing database")
with open("Geoacumen-Country.mmdb", "wb") as f:
    enc.write(f)
