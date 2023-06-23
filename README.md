Simple example program to try and reproduce this issue with `vl-convert`:

* https://github.com/vega/vl-convert/issues/67

## Run in Docker

```
./run-in-docker
```

## Run standalone

1. Create a venv and activate it
2. `pip install -r requirements.txt`
3. `vl-convert-bulk.py vega-lite/*.json`

## Failure output seen

```
#
# Fatal error in , line 0
# Check failed: Deoptimizer::IsValidReturnAddress(PointerAuthentication::StripPAC(pc), isolate_).
#
#
#
#FailureMessage Object: 0xffff8cce8550
==== C stack trace ===============================

    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0x11f9624) [0xffff8e015624]
    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0x910b24) [0xffff8d72cb24]
    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0x11f2820) [0xffff8e00e820]
    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0xe43d5c) [0xffff8dc5fd5c]
    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0x97ac54) [0xffff8d796c54]
    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0x977b2c) [0xffff8d793b2c]
    /usr/local/lib/python3.9/site-packages/vl_convert/vl_convert.cpython-39-aarch64-linux-gnu.so(+0x1064234) [0xffff8de80234]
Trace/breakpoint trap
```