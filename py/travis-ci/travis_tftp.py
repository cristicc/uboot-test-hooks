import os
import binascii

def efifit2env(file_name=None, addr=None):
    """Create dictionary describing file for EFI fit image test

    @filename:  name of the file to be described
    @addr:      address used for loading the file as int (e.g. 0x40400000)
    Return:     dictionary describing the file with entries
                * dn    - tftp directory
                * fn    - filename, optional
                * size  - file size in bytes, optional
                * crc32 - checksum using CRC-32 algorithm, optional
                * addr  - loading address, optional
    """
    tftp_dir = os.environ['UBOOT_TRAVIS_BUILD_DIR']

    ret = {
        'dn': tftp_dir,
    }

    if addr is not None:
        ret['addr'] = addr

    if file_name:
        file_full = tftp_dir + '/' + file_name
        if os.path.isfile(file_full):
            ret['fn'] = file_name
            ret['size'] = os.path.getsize(file_full)
            with open(file_full, 'rb') as f:
                ret['crc32'] = hex(binascii.crc32(f.read()) & 0xffffffff)[2:]

    return ret

def file2env(file_name, addr=None):
    """Create dictionary describing file

    @filename:  name of the file to be described
    @addr:      address used for loading the file as int (e.g. 0x40400000)
    Return:     dictionary describing the file with entries
                * fn    - filename
                * size  - file size in bytes
                * crc32 - checksum using CRC-32 algorithm
                * addr  - loading address, optional
    """
    file_full = os.environ['UBOOT_TRAVIS_BUILD_DIR'] + "/" + file_name

    if not os.path.isfile(file_full):
        return None

    ret = {
        "fn": file_name,
        "size": os.path.getsize(file_full),
    }

    with open(file_full, 'rb') as fd:
        ret["crc32"] = hex(binascii.crc32(fd.read()) & 0xffffffff)[2:]

    if addr is not None:
        ret['addr'] = addr

    return ret
