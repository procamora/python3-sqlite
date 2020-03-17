# python3-sqlite





# Installation

```bash
git clone git@github.com:procamora/python3-sqlite.git sqlite
```

or

```bash
$ pip install procamora-sqlite
```


# Usage

crear una clase que implmente las funciones requerias

```python3
from sqlite.interface_sqlite import *
```


__all__ = ['conection_sqlite', 'execute_script_sqlite', 'dump_database']



```python
def update_host_offline(date: Text):
    query: Text = f"UPDATE Hosts SET active=0 WHERE date <> '{date}';"
    logger.debug(query)
    print(query)
    conection_sqlite(DB, query)
```