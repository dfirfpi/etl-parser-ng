# -*- coding: utf-8 -*-
'''
Microsoft-Windows-Kernel-Network
GUID : 7dd42a49-5329-4832-8dfd-43d979153a88
'''
# [20230121] Replaced double quotes with singles ones.
# [20230108] Added Computed to imports and refactored the long line
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, \
                      Int64sl, Int64ul, Bytes, Double, Float32l, Struct, \
                      Computed
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=10, version=0)
class Microsoft_Windows_Kernel_Network_10_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataSent'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'startime' / Int32ul,
        'endtime' / Int32ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=11, version=0)
class Microsoft_Windows_Kernel_Network_11_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataReceived'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=12, version=0)
class Microsoft_Windows_Kernel_Network_12_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ConnectionAttempted'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'mss' / Int16ul,
        'sackopt' / Int16ul,
        'tsopt' / Int16ul,
        'wsopt' / Int16ul,
        'rcvwin' / Int32ul,
        'rcvwinscale' / Int16ul,
        'sndwinscale' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=13, version=0)
class Microsoft_Windows_Kernel_Network_13_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DisconnectIssued'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=14, version=0)
class Microsoft_Windows_Kernel_Network_14_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataRetransmitted'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=15, version=0)
class Microsoft_Windows_Kernel_Network_15_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ConnectionAccepted'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'mss' / Int16ul,
        'sackopt' / Int16ul,
        'tsopt' / Int16ul,
        'wsopt' / Int16ul,
        'rcvwin' / Int32ul,
        'rcvwinscale' / Int16ul,
        'sndwinscale' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=16, version=0)
class Microsoft_Windows_Kernel_Network_16_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ReconnectAttempted'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=17, version=0)
class Microsoft_Windows_Kernel_Network_17_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('TCPConnectionAttemptFailed'),
        'Proto' / Int16ul,
        'FailureCode' / Int16ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=18, version=0)
class Microsoft_Windows_Kernel_Network_18_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ProtocolCopiedDataOnBehalfOfUser'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=26, version=0)
class Microsoft_Windows_Kernel_Network_26_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataSent_26'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'startime' / Int32ul,
        'endtime' / Int32ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=27, version=0)
class Microsoft_Windows_Kernel_Network_27_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataReceived_27'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=28, version=0)
class Microsoft_Windows_Kernel_Network_28_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ConnectionAttempted_28'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'mss' / Int16ul,
        'sackopt' / Int16ul,
        'tsopt' / Int16ul,
        'wsopt' / Int16ul,
        'rcvwin' / Int32ul,
        'rcvwinscale' / Int16ul,
        'sndwinscale' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=29, version=0)
class Microsoft_Windows_Kernel_Network_29_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DisconnectIssued_29'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=30, version=0)
class Microsoft_Windows_Kernel_Network_30_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataRetransmitted_30'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=31, version=0)
class Microsoft_Windows_Kernel_Network_31_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ConnectionAccepted_31'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'mss' / Int16ul,
        'sackopt' / Int16ul,
        'tsopt' / Int16ul,
        'wsopt' / Int16ul,
        'rcvwin' / Int32ul,
        'rcvwinscale' / Int16ul,
        'sndwinscale' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=32, version=0)
class Microsoft_Windows_Kernel_Network_32_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ReconnectAttempted_32'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=34, version=0)
class Microsoft_Windows_Kernel_Network_34_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('ProtocolCopiedDataOnBehalfOfUser_34'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=42, version=0)
class Microsoft_Windows_Kernel_Network_42_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataSentOverUDP'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=43, version=0)
class Microsoft_Windows_Kernel_Network_43_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataReceivedOverUDP'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'daddr' / Int32ul,
        'saddr' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=49, version=0)
class Microsoft_Windows_Kernel_Network_49_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('UDPConnectionAttemptFailed'),
        'Proto' / Int16ul,
        'FailureCode' / Int16ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=58, version=0)
class Microsoft_Windows_Kernel_Network_58_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataSentOverUDP_58'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )


@declare(guid=guid('7dd42a49-5329-4832-8dfd-43d979153a88'), event_id=59, version=0)
class Microsoft_Windows_Kernel_Network_59_0(Etw):
    pattern = Struct(
        # [20230108] Added Struct's name base on manifest
        'sname' / Computed('DataReceivedOverUDP_59'),
        'PID' / Int32ul,
        'size' / Int32ul,
        'dport' / Int16ul,
        'sport' / Int16ul,
        'seqnum' / Int32ul,
        'connid' / Int32ul
    )

