# Module was created by Xset

from struct import *

class ByteArray:
    def __init__(self, bytes=b""):
        self.bytes = bytes
        self.count = len(self.bytes)

    def writeByte(self, value):
        self.count += 1
        self.bytes += pack('<b', int(value))
        return self

    def writeUnsignedByte(self, value):
        self.count += 1
        self.bytes += pack('<B', int(value))
        return self

    def writeShort(self, value):
        self.count += 1
        self.bytes += pack('<h', int(value))
        return self

    def writeUnsignedShort(self, value):
        self.count += 1
        self.bytes += pack('<H', int(value))
        return self

    def writeInt(self, value):
        self.count += 1
        self.bytes += pack('<i', int(value))
        return self

    def writeUnsignedInt(self, value):
        self.count += 1
        self.bytes += pack('<I', int(value))
        return self

    def writeBool(self, value):
        self.count += 1
        self.bytes += pack('<?', int(value))
        return self

    def bytesAvailable(self):
        return self.count > 0

    def writeUTF(self, value):
        size = len(value)
        self.writeShort(size)
        self.write(value)
        return self

    def writeUTFBytes(self, value, size):
        valueData = str(pack('<b', 0)) * int(size)
        for data in valueData:
            if len(value) < int(size):
                value = value + pack('<b', 0)
        self.write(value)
        return self

    def writeBytes(self, value):
        self.bytes += bytes(str(value), encoding='utf-8')
        return self

    def write(self, value):
        self.bytes += bytes(str(value), encoding='utf-8')

    def readByte(self):
        value = unpack('<b', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        return value

    def readUnsignedByte(self):
        value = unpack('<B', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        return value

    def readShort(self):
        value = unpack('<h', self.bytes[:2])[0]
        self.bytes = self.bytes[2:]
        return value

    def readUnsignedShort(self):
        value = unpack('<H', self.bytes[:2])[0]
        self.bytes = self.bytes[2:]
        return value

    def readInt(self):
        value = unpack('<i', self.bytes[:4])[0]
        self.bytes = self.bytes[4:]
        return value

    def readUnsignedInt(self):
        value = unpack('<I', self.bytes[:4])[0]
        self.bytes = self.bytes[4:]
        return value

    def readUTF(self):
        size = unpack('<h', self.bytes[:2])[0]
        value = self.bytes[2:2 + size]
        self.bytes = self.bytes[size + 2:]
        return value

    def readUnsignedUTF(self):
        size = unpack('<H', self.bytes[:2])[0]
        value = self.bytes[2:2 + size]
        self.bytes = self.bytes[size + 2:]
        return value

    def toPack(self):
        dev = pack("!l", len(self.bytes) + 4)
        return dev + self.bytes

    def readBy(self, Pos):
        self.bytes = self.bytes[Pos:]
        return self.bytes

    def readBool(self):
        value = unpack('<?', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        if value == 1:
            return True
        else:
            return False

    def readUTFBytes(self, size):
        value = self.bytes[:int(size)]
        self.bytes = self.bytes[int(size):]
        return value

    def toByteArray(self):
        return self.bytes

    def toString(self):
        return self.bytes

    def getLength(self):
        return len(self.bytes)

    def bytesAvailable(self):
        return len(self.bytes) > 0
