"""
Sphinx 3.0.0 bug
"""

class Conf(object):
    """
    Cropped example

    Attributes:
        session: filename where the session will be saved
        interactive_shell : can be "ipython", "python" or "auto". Default: Auto
        stealth: if 1, prevents any unwanted packet to go out (ARP, DNS, ...)
        checkIPID: if 0, doesn't check that IPID matches between IP sent and
            ICMP IP citation received
            if 1, checks that they either are equal or byte swapped
            equals (bug in some IP stacks)
            if 2, strictly checks that they are equals
        checkIPsrc: if 1, checks IP src in IP and ICMP IP citation match
            (bug in some NAT stacks)
        checkIPinIP: if True, checks that IP-in-IP layers match. If False, do
            not check IP layers that encapsulates another IP layer
    """
    session = None
    interactive_shell = None
    stealth = 0
    checkIPID = 0
    checkIPsrc = 0
    checkIPinIP = 0
