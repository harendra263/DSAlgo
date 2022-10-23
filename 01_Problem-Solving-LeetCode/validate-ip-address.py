# Time:  O(1)
# Space: O(1)

import string


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        blocks = IP.split('.')
        if len(blocks) == 4:
            return next(
                (
                    "Neither"
                    for i in xrange(len(blocks))
                    if not blocks[i].isdigit()
                    or not 0 <= int(blocks[i]) < 256
                    or (blocks[i][0] == '0' and len(blocks[i]) > 1)
                ),
                "IPv4",
            )

        blocks = IP.split(':')
        if len(blocks) == 8:
            return next(
                (
                    "Neither"
                    for i in xrange(len(blocks))
                    if not (1 <= len(blocks[i]) <= 4)
                    or any(c not in string.hexdigits for c in blocks[i])
                ),
                "IPv6",
            )

        return "Neither"

