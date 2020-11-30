学习笔记

## Main

```python
if __name__ == '__main__':     # Runs main() if file wasn't imported.
    main()
```

## List

```python
<list> = <list>[from_inclusive : to_exclusive : ±step_size]
<list>.append(<el>)            # Or: <list> += [<el>]
<list>.extend(<collection>)    # Or: <list> += <collection>
<list>.sort()
<list>.reverse()
<list> = sorted(<collection>)
<iter> = reversed(<list>)
sum_of_elements  = sum(<collection>)
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]
sorted_by_second = sorted(<collection>, key=lambda el: el[1])
sorted_by_both   = sorted(<collection>, key=lambda el: (el[1], el[0]))
flatter_list     = list(itertools.chain.from_iterable(<list>))
product_of_elems = functools.reduce(lambda out, el: out * el, <collection>)
list_of_chars    = list(<str>)
```

- **Module [operator](#operator) provides functions itemgetter() and mul() that offer the same functionality as [lambda](#lambda) expressions above.**

```python
<int> = <list>.count(<el>)     # Returns number of occurrences. Also works on strings.
index = <list>.index(<el>)     # Returns index of first occurrence or raises ValueError.
<list>.insert(index, <el>)     # Inserts item at index and moves the rest to the right.
<el> = <list>.pop([index])     # Removes and returns item at index or from the end.
<list>.remove(<el>)            # Removes first occurrence of item or raises ValueError.
<list>.clear()                 # Removes all items. Also works on dictionary and set.
```

## Dictionary

```python
<view> = <dict>.keys()                          # Coll. of keys that reflects changes.
<view> = <dict>.values()                        # Coll. of values that reflects changes.
<view> = <dict>.items()                         # Coll. of key-value tuples that reflects chgs.
value  = <dict>.get(key, default=None)          # Returns default if key is missing.
value  = <dict>.setdefault(key, default=None)   # Returns and writes default if key is missing.
<dict> = collections.defaultdict(<type>)        # Creates a dict with default value of type.
<dict> = collections.defaultdict(lambda: 1)     # Creates a dict with default value 1.
<dict> = dict(<collection>)                     # Creates a dict from coll. of key-value pairs.
<dict> = dict(zip(keys, values))                # Creates a dict from two collections.
<dict> = dict.fromkeys(keys [, value])          # Creates a dict from collection of keys.
<dict>.update(<dict>)                           # Adds items. Replaces ones with matching keys.
value = <dict>.pop(key)                         # Removes item or raises KeyError.
{k for k, v in <dict>.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in <dict>.items() if k in keys}  # Returns a dictionary, filtered by keys.
```

### Counter

```python
>>> from collections import Counter
>>> colors = ['blue', 'blue', 'blue', 'red', 'red']
>>> counter = Counter(colors)
>>> counter['yellow'] += 1
Counter({'blue': 3, 'red': 2, 'yellow': 1})
>>> counter.most_common()[0]
('blue', 3)
```

## Set

```python
<set> = set()
<set>.add(<el>)                                 # Or: <set> |= {<el>}
<set>.update(<collection>)                      # Or: <set> |= <set>
<set>  = <set>.union(<coll.>)                   # Or: <set> | <set>
<set>  = <set>.intersection(<coll.>)            # Or: <set> & <set>
<set>  = <set>.difference(<coll.>)              # Or: <set> - <set>
<set>  = <set>.symmetric_difference(<coll.>)    # Or: <set> ^ <set>
<bool> = <set>.issubset(<coll.>)                # Or: <set> <= <set>
<bool> = <set>.issuperset(<coll.>)              # Or: <set> >= <set>
<el> = <set>.pop()                              # Raises KeyError if empty.
<set>.remove(<el>)                              # Raises KeyError if missing.
<set>.discard(<el>)                             # Doesn't raise an error.
```

## Tuple

**Tuple is an immutable and hashable list.**

```python
<tuple> = ()
<tuple> = (<el>, )
<tuple> = (<el_1>, <el_2> [, ...])
```

### Named Tuple

**Tuple's subclass with named elements.**

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', 'x y')
>>> p = Point(1, y=2)
Point(x=1, y=2)
>>> p[0]
1
>>> p.x
1
>>> getattr(p, 'y')
2
>>> p._fields  # Or: Point._fields
('x', 'y')
```

## String

```python
<str>  = <str>.strip()                       # Strips all whitespace characters from both ends.
<str>  = <str>.strip('<chars>')              # Strips all passed characters from both ends.
<list> = <str>.split()                       # Splits on one or more whitespace characters.
<list> = <str>.split(sep=None, maxsplit=-1)  # Splits on 'sep' str at most 'maxsplit' times.
<list> = <str>.splitlines(keepends=False)    # Splits on \n,\r,\r\n. Keeps them if 'keepends'.
<str>  = <str>.join(<coll_of_strings>)       # Joins elements using string as separator.
<bool> = <sub_str> in <str>                  # Checks if string contains a substring.
<bool> = <str>.startswith(<sub_str>)         # Pass tuple of strings for multiple options.
<bool> = <str>.endswith(<sub_str>)           # Pass tuple of strings for multiple options.
<int>  = <str>.find(<sub_str>)               # Returns start index of first match or -1.
<int>  = <str>.index(<sub_str>)              # Same but raises ValueError if missing.
<str>  = <str>.replace(old, new [, count])   # Replaces 'old' with 'new' at most 'count' times.
<str>  = <str>.translate(<table>)            # Use `str.maketrans(<dict>)` to generate table.
<str>  = chr(<int>)                          # Converts int to Unicode char.
<int>  = ord(<str>)                          # Converts Unicode char to int.
```

- **Also: `'lstrip()'`, `'rstrip()'`.**
- **Also: `'lower()'`, `'upper()'`, `'capitalize()'` and `'title()'`.**

### Property Methods

```text
┏━━━━━━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┓
┃               │ [ !#$%…] │ [a-zA-Z] │  [¼½¾]   │  [²³¹]   │  [0-9]   ┃
┠───────────────┼──────────┼──────────┼──────────┼──────────┼──────────┨
┃ isprintable() │    ✓     │    ✓     │    ✓     │    ✓     │    ✓     ┃
┃ isalnum()     │          │    ✓     │    ✓     │    ✓     │    ✓     ┃
┃ isnumeric()   │          │          │    ✓     │    ✓     │    ✓     ┃
┃ isdigit()     │          │          │          │    ✓     │    ✓     ┃
┃ isdecimal()   │          │          │          │          │    ✓     ┃
┗━━━━━━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┛
```

- **Also: `'isspace()'` checks for `'[ \t\n\r\f\v…]'`.**

## Type

- **Everything is an object.**
- **Every object has a type.**
- **Type and class are synonymous.**

```python
<type> = type(<el>)                          # Or: <el>.__class__
<bool> = isinstance(<el>, <type>)            # Or: issubclass(type(<el>), <type>)
>>> type('a'), 'a'.__class__, str
(<class 'str'>, <class 'str'>, <class 'str'>)
```

#### Some types do not have built-in names, so they must be imported:

```python
from types import FunctionType, MethodType, LambdaType, GeneratorType
```

### Abstract Base Classes

**Each abstract base class specifies a set of virtual subclasses. These classes are then recognized by isinstance() and issubclass() as subclasses of the ABC, although they are really not.**

```python
>>> from collections.abc import Sequence, Collection, Iterable
>>> isinstance([1, 2, 3], Iterable)
True
┏━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━━━┓
┃                  │  Sequence  │ Collection │  Iterable  ┃
┠──────────────────┼────────────┼────────────┼────────────┨
┃ list, range, str │     ✓      │     ✓      │     ✓      ┃
┃ dict, set        │            │     ✓      │     ✓      ┃
┃ iter             │            │            │     ✓      ┃
┗━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━━━┛
>>> from numbers import Integral, Rational, Real, Complex, Number
>>> isinstance(123, Number)
True
┏━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┓
┃                    │ Integral │ Rational │   Real   │ Complex  │  Number  ┃
┠────────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┨
┃ int                │    ✓     │    ✓     │    ✓     │    ✓     │    ✓     ┃
┃ fractions.Fraction │          │    ✓     │    ✓     │    ✓     │    ✓     ┃
┃ float              │          │          │    ✓     │    ✓     │    ✓     ┃
┃ complex            │          │          │          │    ✓     │    ✓     ┃
┃ decimal.Decimal    │          │          │          │          │    ✓     ┃
┗━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┛
```

## Regex

```python
import re
<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences with 'new'.
<list>  = re.findall(<regex>, text)            # Returns all occurrences as strings.
<list>  = re.split(<regex>, text, maxsplit=0)  # Use brackets in regex to include the matches.
<Match> = re.search(<regex>, text)             # Searches for first occurrence of the pattern.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.
<iter>  = re.finditer(<regex>, text)           # Returns all occurrences as match objects.
```

- **Search() and match() return None if they can't find a match.**
- **Argument `'flags=re.IGNORECASE'` can be used with all functions.**
- **Argument `'flags=re.MULTILINE'` makes `'^'` and `'$'` match the start/end of each line.**
- **Argument `'flags=re.DOTALL'` makes dot also accept the `'\n'`.**
- **Use `r'\1'` or `'\\1'` for backreference.**
- **Add `'?'` after an operator to make it non-greedy.**

### Match Object

```python
<str>   = <Match>.group()                      # Returns the whole match. Also group(0).
<str>   = <Match>.group(1)                     # Returns part in the first bracket.
<tuple> = <Match>.groups()                     # Returns all bracketed parts.
<int>   = <Match>.start()                      # Returns start index of the match.
<int>   = <Match>.end()                        # Returns exclusive end index of the match.
```

### Special Sequences

- **By default digits, alphanumerics and whitespaces from all alphabets are matched, unless `'flags=re.ASCII'` argument is used.**
- **Use a capital letter for negation.**

```python
'\d' == '[0-9]'                                # Matches any digit.
'\w' == '[a-zA-Z0-9_]'                         # Matches any alphanumeric.
'\s' == '[ \t\n\r\f\v]'                        # Matches any whitespace.
```



以上内容[参考了这里](https://github.com/gto76/python-cheatsheet)，没有在开头就加上参考的链接，是想让读者能读到文章的末尾。

另外，笔记不想重复“造轮子了”（明明是没有人家弄的好），这么漂亮的笔记（虽然是参考的，但链接已经贴上啦，哈哈哈哈），希望能打个高分～



