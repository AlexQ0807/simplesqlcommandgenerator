## Simple SQL Command Generator Package
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/simplesqlcommandgenerator.git
```


### Example

```
from simplesqlcommandgenerator.commandgenerator import CommandGenerator

table_name = "Customers"
insert_items = {
    "CustomerName": "Cardinal",
    "ContactName": "Tom B. Erichsen",
    "Address": "Skagen 21",
    "City": "Stavanger",
    "PostalCode": "4006",
    "Country": "Norway",
}
cmd = CommandGenerator.create_insert_command(table_name=table_name, insert_items=insert_items)
```