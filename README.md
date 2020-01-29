# Hash Map

This is an implementation of a Hash which will work with both ints and strings as keys

## Installation

As long as you have python3 there is nothing you need to install in order to get this working!

In order to use HashMap, open your terminal using `python3`.

Import the HashMap by typing `from hash_map import HashMap`. If you see `True` then you are good to go!

```
from hash_map import HashMap
True
>>> hash = HashMap()
>>> hash[1] = 100
>>> print(hash[1])
100
>>> hash.delete(1)
>>> print(hash[1])
None
>>>
```

## Testing

This project is tested using the pytest framework. If you would like to run the test suite, please install pip. Once pip is installed, run `pip3 install -U pytest` in order to install pytest.

After successful installation, run `pytest` to run the entire test suite.

## API

In order to assign or retrieve elements in the hash, the standard `[]` and `[]=` operators can be used:

```
  hash[5] = 10
  hash[5] \\ will return 10
```

Functions are also available in order to see what keys and values are present in the hash:

```
  hash[1] = 10
  hash[2] = 20

  hash.keys() will return [1,2]
  hash.values() will return [10, 20]
```

Please note that these lists are not going to be in any reliable order.

Elements can also be removed from the hash using the `delete` method:

```
  hash[10] = 100
  hash.delete(10)
  hash[10] will be None
```

If you just need to check that a certain key exists in the Hash, the `exist` method can be used:

```
  hash[10] = 100
  hash.exists(10) will return True
```
