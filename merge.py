import requests
import re

urls = [
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=0&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=15000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=30000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=45000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=60000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=75000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=90000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=105000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=120000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=135000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=150000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=165000&limit=15000",
    "https://xmlfeedgenerator.com/f/1/sistem_yazilim5.php?start=180000&limit=15000"
]

items = []

for url in urls:
    r = requests.get(url, timeout=60)
    r.encoding = "utf-8"
    xml = r.text

    # XML declaration ve root temizle
    xml = re.sub(r"<\?xml.*?\?>", "", xml)
    xml = re.sub(r"</?items>", "", xml, flags=re.IGNORECASE)

    items.append(xml.strip())

final_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<items>\n'
final_xml += "\n".join(items)
final_xml += "\n</items>"

with open("jetteknoloji.xml", "w", encoding="utf-8") as f:
    f.write(final_xml)

print("XML birleştirildi")
