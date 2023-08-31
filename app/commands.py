import os
import shutil
import gzip


import requests
import click


from app import app
from app.models import CountryRange, db


@app.cli.command("load")
# @click.argument("name")
def load_ip2country():
    url = "https://ip.ludost.net/raw/country.db.gz"
    download_path = 'country.db.gz'
    target_path = 'country.csv'

    r = requests.get(url, verify=False, stream=True)

    with open(download_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    with gzip.open(download_path, 'rb') as f_in:
        with open(target_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    os.unlink(download_path)

    CountryRange.query.delete()

    ctr = 0
    with open(target_path, "r") as file:
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break

            ctr += 1
            if ctr % 10000 == 0:
                print(ctr)

            parts = line.upper().split(" ")
            item = CountryRange(
                left=CountryRange.ip2int(parts[0]),
                right=CountryRange.ip2int(parts[1]),
                country=parts[2],
            )
            db.session.add(item)

    db.session.commit()
    os.unlink(target_path)
