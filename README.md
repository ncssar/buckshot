# buckshot
SAR coordinate buckshot - show lat/lon coordinate possibilities in all three coordinate systems

The coordinate possibilities can be sent to a GPX file, and can be sent to any accessable saved SARTopo Offline or sartopo.com map.

See the latest installation instructions [here](INSTALL.md).

See the guidelines for contributing to this project [here](CONTRIBUTING.md).

# Why?

There are three lat/lon coordinate systems:

- Decimal degrees  (D.d)
- Degrees and decimal minutes  (D M.m)
- Degrees, minutes, and decimal seconds  (D M S.s)

Confusion between those coordinate systems can be a big problem, especially during a Search and Rescue operation, and especially during the initial callout and response.

While an incorrect datum (WGS84 vs NAD27 CONUS) can mean the actual location is off by a few hundred meters, **an incorrect coordinate system can lead you astray by _15 miles or more!_**

By also getting a verbal description of the location ("On the side of Prosser Mountain"), you can rule out the impossible or unlikely candidates.

It has happened before and will happen again.  This program mitigates the problem.

Maybe the person who told you the coordinates was not familiar with coordinate systems.

Maybe the wording you recieved was ambiguous or did not make sense.

Maybe you think you can infer a coordinate system from the wording you got, but, you want to verify.

Maybe the agency that gave you coordinates made some assumption about coordinate system, and you made a different assumption.

Regardless of the reason, this program gives quick visual verification.

![buckshot GUI](/doc/buckshot.png)

![buckshot sarsoft map](/doc/buckshot_map.png)

[![SAR Buckshot video](/doc/buckshot_video_thumb.png)](https://www.youtube.com/watch?v=QPygvh3QiJA)

