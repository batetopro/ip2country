import socket
import struct
import pymysql
from app.settings import Settings


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


def ip2country(ip):
    db = get_connection()
    cursor = db.cursor()

    value = ip2int(ip)
    sql = 'SELECT country FROM ip2country WHERE `left` >= {0} AND `right` <= {1}'.format(value, value)

    cursor.execute(sql)

    row = cursor.fetchone()
    cursor.close()

    if row is None:
        return 'XX'

    return row[0]


def get_connection():
    return pymysql.connect(
        host=Settings.DB['HOST'],
        user=Settings.DB['USER'],
        password=Settings.DB['PASSWORD'],
        db=Settings.DB['BASE'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
