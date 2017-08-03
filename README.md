# satsearch.py

`satsearch.py` is a quick little Python script I wrote to help me fine-tune my
satellite system. It uses `w_scan` and `gotox` to move the satellite disk
incrementally across the sky looking for a signal. When it finds it, it stops.
From there, you can calculate how much tweaking you might need to make to your
setup (or how far USALS is off).

## Prerequisites

1. A satellite dish. :)
1. A DVB card or USB-DVB adapter. I have tested this with both a Tevii S-662
and a TBS-6902.
1. A motor that supports `gotox` (most do).
1. `gotox` (this is the `dvb-apps` package on Ubuntu)
1. `w_scan` [Download here](http://wirbel.htpc-forum.de/w_scan/index2.html)

## Use Example

`./satsearch.py -s 12 -e 20 -d W -i 0.1 S105W0`

This will start the search at 12 degrees offset west, moving the dish in 0.1
degree increments west until it either reaches 20 degrees or finds satellite
S105W0 (which is SES-3 in this case).

## License

MIT
