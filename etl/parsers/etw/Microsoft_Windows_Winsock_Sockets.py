# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winsock-Sockets
GUID : bde46aea-2357-51fe-7367-d5296f530bd1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, \
                      Int64sl, Int64ul, Bytes, Double, Float32l, Struct, \
                      Computed, GreedyBytes, Hex
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=1, version=0)
class Microsoft_Windows_Winsock_Sockets_1_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockCreateStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=2, version=0)
class Microsoft_Windows_Winsock_Sockets_2_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockCreateStop'),
        'ErrorCode' / Hex(Int32ul),
        'Socket' / Int64ul,
        'AddressFamily' / Int32ul,
        'SocketType' / Int32ul,
        'Protocol' / Int32ul,
        'ProcessId' / Int32ul
        # TBR TODO: seems the messages have not the expected lenght
        #'FailurePoint' / Hex(Int32ul)
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=3, version=0)
class Microsoft_Windows_Winsock_Sockets_3_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockCloseStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=4, version=0)
class Microsoft_Windows_Winsock_Sockets_4_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockCloseStop'),
        'ErrorCode' / Hex(Int32ul),
        'Socket' / Int64ul,
        'IsProviderSocket' / Int8ul,
        'FailurePoint' / Hex(Int32ul)
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=5, version=0)
class Microsoft_Windows_Winsock_Sockets_5_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockAcceptStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=6, version=0)
class Microsoft_Windows_Winsock_Sockets_6_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockAcceptStop'),
        'ErrorCode' / Hex(Int32ul),
        'SocketAccepted' / Int64ul,
        'SocketListening' / Int64ul,
        'ProcessId' / Int32ul,
        'FailurePoint' / Hex(Int32ul)
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=7, version=0)
class Microsoft_Windows_Winsock_Sockets_7_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockSetOptStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=8, version=0)
class Microsoft_Windows_Winsock_Sockets_8_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockSetOptStop'),
        'ErrorCode' / Hex(Int32ul),
        'Socket' / Int64ul,
        'Level' / Int32ul,
        'OptName' / Int32ul,
        'OptLen' / Int32ul,
        'OptVal' / Int32ul,
        'FailurePoint' / Hex(Int32ul)
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=9, version=0)
class Microsoft_Windows_Winsock_Sockets_9_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockConnectStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=10, version=0)
class Microsoft_Windows_Winsock_Sockets_10_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockConnectStop'),
        'ErrorCode' / Hex(Int32ul),
        'Socket' / Int64ul,
        'AddressLength' / Int32ul,
        'Address' / Bytes(lambda this: this.AddressLength),
        'FailurePoint' / Hex(Int32ul)
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=11, version=0)
class Microsoft_Windows_Winsock_Sockets_11_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockBindStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=12, version=0)
class Microsoft_Windows_Winsock_Sockets_12_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockBindStop'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=13, version=0)
class Microsoft_Windows_Winsock_Sockets_13_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockGetOptStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=14, version=0)
class Microsoft_Windows_Winsock_Sockets_14_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockGetOptStop'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=15, version=0)
class Microsoft_Windows_Winsock_Sockets_15_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockListenStart'),
        'unparsed' / GreedyBytes
    )


@declare(guid=guid('bde46aea-2357-51fe-7367-d5296f530bd1'), event_id=16, version=0)
class Microsoft_Windows_Winsock_Sockets_16_0(Etw):
    pattern = Struct(
        'sname' / Computed('SockListenStop'),
        'ErrorCode' / Hex(Int32ul),
        'Socket' / Int64ul,
        'Backlog' / Int32ul,
        'FailurePoint' / Hex(Int32ul)
    )
