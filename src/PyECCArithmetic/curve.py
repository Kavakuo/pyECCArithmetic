# coding=utf-8

class Curve(object):
    """
    An elliptic curve that can be represented by a
    Weierstrass equation y^2 = x^3 + a * x + b mod p
    """


    def __init__(self, a, b, p, name=''):
        self.a = a
        self.b = b
        self.p = p
        self.name = name


    # http://www.secg.org/sec2-v2.pdf
    @staticmethod
    def secp224r1():
        p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000001
        a = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFE
        b = 0xB4050A850C04B3ABF54132565044B0B7D7BFD8BA270B39432355FFB4
        return Curve(a, b, p, 'secp224r1')


    @staticmethod
    def secp256r1():
        p = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
        a = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC
        b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
        return Curve(a, b, p, 'secp256r1')


    @staticmethod
    def secp384r1():
        p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFF0000000000000000FFFFFFFF
        a = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFF0000000000000000FFFFFFFC
        b = 0xB3312FA7E23EE7E4988E056BE3F82D19181D9C6EFE8141120314088F5013875AC656398D8A2ED19D2A85C8EDD3EC2AEF
        return Curve(a, b, p, 'secp384r1')


    @staticmethod
    def secp521r1():
        p = 0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        a = 0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC
        b = 0x0051953EB9618E1C9A1F929A21A0B68540EEA2DA725B99B315F3B8B489918EF109E156193951EC7E937B1652C0BD3BB1BF073573DF883D2C34F1EF451FD46B503F00
        return Curve(a, b, p, 'secp521r1')


    # https://tools.ietf.org/html/rfc5639
    @staticmethod
    def brainpoolP160r1():
        p = 0xE95E4A5F737059DC60DFC7AD95B3D8139515620F
        a = 0x340E7BE2A280EB74E2BE61BADA745D97E8F7C300
        b = 0x1E589A8595423412134FAA2DBDEC95C8D8675E58
        return Curve(a, b, p, 'brainpoolP160r1')


    @staticmethod
    def brainpoolP192r1():
        p = 0xC302F41D932A36CDA7A3463093D18DB78FCE476DE1A86297
        a = 0x6A91174076B1E0E19C39C031FE8685C1CAE040E5C69A28EF
        b = 0x469A28EF7C28CCA3DC721D044F4496BCCA7EF4146FBF25C9
        return Curve(a, b, p, 'brainpoolP160r1')


    @staticmethod
    def brainpoolP224r1():
        p = 0xD7C134AA264366862A18302575D1D787B09F075797DA89F57EC8C0FF
        a = 0x68A5E62CA9CE6C1C299803A6C1530B514E182AD8B0042A59CAD29F43
        b = 0x2580F63CCFE44138870713B1A92369E33E2135D266DBB372386C400B
        return Curve(a, b, p, 'brainpoolP224r1')


    @staticmethod
    def brainpoolP256r1():
        p = 0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377
        a = 0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9
        b = 0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6
        return Curve(a, b, p, 'brainpoolP256r1')


    @staticmethod
    def brainpoolP320r1():
        p = 0xD35E472036BC4FB7E13C785ED201E065F98FCFA6F6F40DEF4F92B9EC7893EC28FCD412B1F1B32E27
        a = 0x3EE30B568FBAB0F883CCEBD46D3F3BB8A2A73513F5EB79DA66190EB085FFA9F492F375A97D860EB4
        b = 0x520883949DFDBC42D3AD198640688A6FE13F41349554B49ACC31DCCD884539816F5EB4AC8FB1F1A6
        return Curve(a, b, p, 'brainpoolP320r1')


    @staticmethod
    def brainpoolP384r1():
        p = 0x8CB91E82A3386D280F5D6F7E50E641DF152F7109ED5456B412B1DA197FB71123ACD3A729901D1A71874700133107EC53
        a = 0x7BC382C63D8C150C3C72080ACE05AFA0C2BEA28E4FB22787139165EFBA91F90F8AA5814A503AD4EB04A8C7DD22CE2826
        b = 0x04A8C7DD22CE28268B39B55416F0447C2FB77DE107DCD2A62E880EA53EEB62D57CB4390295DBC9943AB78696FA504C11
        return Curve(a, b, p, 'brainpoolP384r1')


    @staticmethod
    def brainpoolP512r1():
        p = 0xAADD9DB8DBE9C48B3FD4E6AE33C9FC07CB308DB3B3C9D20ED6639CCA703308717D4D9B009BC66842AECDA12AE6A380E62881FF2F2D82C68528AA6056583A48F3
        a = 0x7830A3318B603B89E2327145AC234CC594CBDD8D3DF91610A83441CAEA9863BC2DED5D5AA8253AA10A2EF1C98B9AC8B57F1117A72BF2C7B9E7C1AC4D77FC94CA
        b = 0x3DF91610A83441CAEA9863BC2DED5D5AA8253AA10A2EF1C98B9AC8B57F1117A72BF2C7B9E7C1AC4D77FC94CADC083E67984050B75EBAE5DD2809BD638016F723
        return Curve(a, b, p, 'brainpoolP512r1')


    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p
