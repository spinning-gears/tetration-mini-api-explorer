# tetration-mini-api-explorer

`main.py` is actually a boilerplate for a simple Tetration API script that features the ability to perform a GET operation to any API endpoint with a commandline switch instead of running your script.

The purpose of this mini-explorer for the API is to be used during development of your script. If you're wondering what kind of data an API endpoint might return, you can simply run your own script, but with the `show` switch.

**To use this boilerplate, put your logic in the main() function.**

## Example usage

```python
python main.py
``` 

will actually just print the message "Hello, Tetration!" or do perform whatever logic you place in the main() function.

```bash
python main.py --show users
``` 

will ignore your logic and instead display the `users` API endpoint in JSON format (nicely indented).

```bash
python main.py --show users/5b4ffdec497d4f102ab2f431
```

will get the Tetration user with the user id `5b4ffdec497d4f102ab2f431` (keep in mind that user id is not a user's email address but a GUID generated by Tetration when the user is created).