# geoacumen-country

This is an entirely open source (Apache 2) IP to country database mapping built
from public sources of data. It was created to avoid having to rely on 3rd
party sources for basic country data.

## Background

The database is provided in the [mmdb
format](https://maxmind.github.io/MaxMind-DB/). It is created with Cloudflare's
[Python MMDB encoder](https://github.com/cloudflare/py-mmdb-encoder). The data
is sourced from [iptoasn.com](https://iptoasn.com/).

Missing/unknown data could potentially be built from the RIR data but that is
currently an open improvement.

## Usage

The mmdb database is useable with any MaxMind mmdb reader. You can look into
bindings for [libmaxmind](https://github.com/maxmind/libmaxminddb).

One such binding in Python is [maxminddb](https://pypi.org/project/maxminddb/).
For example:

```
>>> import maxminddb
>>> reader = maxminddb.open_database('Geoacumen-Country.mmdb')
>>> reader.get('1.1.1.1')
{'country': {'iso_code': 'CN'}}
```

## Building

The database can be rebuilt using the latest data by installing dependencies
and running `create.py`.

For example:

```
pip install --upgrade --force -r requirements.txt
python create.py
```

The database can be quickly tested with the `read.py` script.

## Distribution

You can freely download the database with no attribution requirement. There are
also additional wrapping libraries to make it easier to package the db into
your applications:

- [Python](https://github.com/geoacumen/python-geoacumen)

## Issues

There is no guarantee of correctness or validity of the data returned by this
database. It should not be used in critical, high-accuracy applications. If you
are relying on IP to location databases in any kind of critical operation, you
should re-evaluate that decision.

If you run into a problem, you can file an issue on the Github issue tracker.
However, if you run into any issues it is your responsibility as an open source
user to help improve the quality of the code and database.