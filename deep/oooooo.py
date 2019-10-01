# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr  6 2019, 01:42:57)
# [GCC 8.3.0]
# Embedded file name: <script>

x = [20282409603651670423947251285911,
     158456325028528675187087900574,
     633825300114114700748351602588,
     162259276829213363391578010288020,
     83076749736557242056487941267521419,
     2596148429267413814265248164609936,
     1267650600228229401496703205275,
     158456325028528675187087900574,
     2658455991569831745807614120560689030,
     10633823966279326983230456482242756484,
     664613997892457936451903530140172168,
     20282409603651670423947251285911,
     158456325028528675187087900574,
     83076749736557242056487941267521419,
     41538374868278621028243970633760652,
     549755813848,
     166153499473114484112975882535042954,
     5192296858534827628530496329219983,
     39614081257132168796771975072,
     1267650600228229401496703205275,
     2596148429267413814265248164609936,
     664613997892457936451903530140172168,
     1298074214633706907132624082304913,
     39614081257132168796771975072,
     83076749736557242056487941267521419,
     20282409603651670423947251285911,
     2535301200456458802993406410650,
     20769187434139310514121985316880269,
     2535301200456458802993406410650,
     39614081257132168796771975072,
     18014398509481929,
     5070602400912917605986812821401,
     1125899906842573,
     36028797018963912,
     5070602400912917605986812821401,
     9007199254740938,
     2251799813685196,
     9007199254740938,
     42535295865117307932921825928971026306]


def v(x, y):
    if y == 0:
        return 1
    if x == y:
        return 1
    return v(x-1, y-1) + v(x-1, y)
# v = --- This code section failed: ---
#
#    3       0  LOAD_FAST             1  'y'
#            3  LOAD_CONST               0
#            6  COMPARE_OP            2  ==
#            9  POP_JUMP_IF_TRUE     24  'to 24'
#           12  LOAD_FAST             1  'y'
#           15  LOAD_FAST             0  'x'
#           18  COMPARE_OP            2  ==
#         21_0  COME_FROM             9  '9'
#           21  POP_JUMP_IF_FALSE    28  'to 28'
#           24  LOAD_CONST               1
#           27  RETURN_VALUE_LAMBDA
#         28_0  COME_FROM            21  '21'
#           28  LOAD_GLOBAL           0  'v'
#           31  LOAD_FAST             0  'x'
#           34  LOAD_CONST               1
#           37  BINARY_SUBTRACT
#           38  LOAD_FAST             1  'y'
#           41  LOAD_CONST               1
#           44  BINARY_SUBTRACT
#           45  CALL_FUNCTION_2       2  None
#           48  LOAD_GLOBAL           0  'v'
#           51  LOAD_FAST             0  'x'
#           54  LOAD_CONST               1
#           57  BINARY_SUBTRACT
#           58  LOAD_FAST             1  'y'
#           61  CALL_FUNCTION_2       2  None
#           64  BINARY_ADD
#           65  RETURN_VALUE_LAMBDA
#           -1  LAMBDA_MARKER
#
# Parse error at or near `None' instruction at offset -1


def y(x): return sum([v(y, w) for y in range(ord(x)) for w in range(y)])


z = raw_input('Check flag anda disini :')
u = [y(i) for i in str(z)]


def w(x, y): return 'Selamat yang anda input benar' if x == y else 'Flag yang anda input salah'


print(w(u, x))
