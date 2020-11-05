import struct


def read_bmp_file(ff_name):
    bmp = open(ff_name, 'rb')
    print('Type: ', bmp.read(2).decode())
    print('Size:       %s' % struct.unpack('I', bmp.read(4)))
    print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
    print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
    print('Offset:     %s' % struct.unpack('I', bmp.read(4)))

    print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
    print('Width:           %s' % struct.unpack('I', bmp.read(4)))
    print('Height:          %s' % struct.unpack('I', bmp.read(4)))
    print('ColourPlanes:    %s' % struct.unpack('H', bmp.read(2)))
    print('Bit rep Pixel:   %s' % struct.unpack('H', bmp.read(2)))

    print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
    print('Raw Image Size:     %s' % struct.unpack('I', bmp.read(4)))
    print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
    print('Vertical Resolution:   %s' % struct.unpack('I', bmp.read(4)))
    print('Number of Colours:   %s' % struct.unpack('I', bmp.read(4)))
    print('Important Coloursde:   %s' % struct.unpack('I', bmp.read(4)))


f_name = "tmp_files/lavanda.bmp"
read_bmp_file(f_name)
