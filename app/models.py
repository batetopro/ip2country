import socket
import struct


from sqlalchemy.dialects.mysql import INTEGER


from app import db


class CountryRange(db.Model):
    __tablename__ = 'ip2country'
    __table_args__ = (
        db.PrimaryKeyConstraint('left', 'right'),
    )

    left = db.Column(INTEGER(unsigned=True), nullable=False)
    right = db.Column(INTEGER(unsigned=True), nullable=False)
    country = db.Column(db.String(2), nullable=False)

    @classmethod
    def ip2int(cls, addr):
        return struct.unpack("!I", socket.inet_aton(addr))[0]

    @classmethod
    def int2ip(cls, addr):
        return socket.inet_ntoa(struct.pack("!I", addr))

    @classmethod
    def convert_ip(cls, addr):
        value = cls.ip2int(addr)
        check = CountryRange.query.filter(CountryRange.left <= value).filter(CountryRange.right >= value).first()
        if not check:
            return 'xx'
        return check.country
