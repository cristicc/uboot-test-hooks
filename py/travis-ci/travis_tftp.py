import os
import binascii

def efifit2env(addr=None):
    """Create dictionary describing file for EFI fit image test

    @addr:      address used for loading the file as int (e.g. 0x40400000)
    Return:     dictionary describing the file with entries
                * fn    - filename
                * addr  - loading address, optional
                * dn    - tftp directory
    """
    tftp_dir = os.environ['UBOOT_TRAVIS_BUILD_DIR']

    ret = {
        "fn": "test-efi-fit.img",
        "dn": tftp_dir,
    }
    if addr is not None:
        ret['addr'] = addr

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
        "crc32": hex(binascii.crc32(open(file_full, 'rb').read()) & 0xffffffff)[2:],
    }
    if addr is not None:
        ret['addr'] = addr

    return ret
