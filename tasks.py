#!/usr/bin/env python

import os
import shutil
import gzip

from invoke import task
import requests

from app.util import get_connection, ip2int


@task
def download(c):
    url = "https://ip.ludost.net/raw/country.db.gz"
    download_path = 'country.db.gz'
    target_path = 'country.csv'

    connection = get_connection()

    r = requests.get(url, verify=False, stream=True)

    with open(download_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    with gzip.open(download_path, 'rb') as f_in:
        with open(target_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    os.unlink(download_path)

    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM ip2country')

        with open(target_path, "r") as file:

            page = []

            while True:
                line = file.readline().strip()
                if len(line) == 0:
                    break

                parts = line.upper().split(" ")

                parts[0] = ip2int(parts[0])
                parts[1] = ip2int(parts[1])

                page.append("({0}, {1}, '{2}')".format(*parts))

                if len(page) > 6000:
                    sql = "INSERT INTO ip2country(`left`, `right`, country) VALUES " + ','.join(page)
                    cursor.execute(sql)
                    page = []

            if len(page) > 0:
                sql = "INSERT INTO ip2country(`left`, `right`, country) VALUES " + ','.join(page)
                cursor.execute(sql)

    os.unlink(target_path)

    connection.commit()
    connection.close()


@task
def server(c):
    from app import app
    app.run()
