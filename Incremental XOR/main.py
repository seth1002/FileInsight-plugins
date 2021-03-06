#
# Incremental XOR - XORing selected region while incrementing XOR key
#
# Copyright (c) 2012, 2013, Nobutaka Mantani
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

offset = getSelectionOffset()
length = getSelectionLength()

if (length > 0):
    key = showSimpleDialog("XOR key (in hex, default = 0x00):")
    if (key == ""):
        key = 0
    else:
        key = int(key, 16)

    step = showSimpleDialog("Increment step (in hex, default = 0x01):")
    if (step == ""):
        step = 1
    else:
        step = int(step, 16)

    init_key = key
    buf = list(getDocument())

    for i in range(0, length):
        j = offset + i
        buf[j] = chr(ord(buf[j]) ^ key)
        key += step
        key = key & 0xff

    newDocument("New file", 1)
    setDocument("".join(buf))
    setBookmark(offset, length, hex(offset), "#c8ffff")

    if (length == 1):
        print "XORed one byte from offset %s to %s while incrementing key from %s (step %s)." % (hex(offset), hex(offset), hex(init_key), hex(step))
    else:
        print "XORed %s bytes from offset %s to %s while incrementing key from %s (step %s)." % (length, hex(offset), hex(offset + length - 1), hex(init_key), hex(step))
    print "Added a bookmark to XORed region."

