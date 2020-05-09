## Usage

To understand how to use this module passing arguments please follow this command:
```python
$ python search.py 'https://www.otus.com' 10 "Yandex"
```

To understand how to use this module without passing arguments (command prompt), please follow these lines:
```python
import search

# Search for www.otus.com using Yandex and returns 10 results
search.Search('https://www.otus.com', results=10, 'Yandex')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests in ```test.py``` as appropriate. 
