## Requests

This sub-project contains a simple crawler that will collect the address that will be queried synchronously using the python module named [`requests`](https://requests.readthedocs.io/en/latest/) and store them in a database table. We will use a SQLite database to do this and the [`dataset`](https://dataset.readthedocs.io/en/latest/) for simplicity for now. This crawler will work synchronously because the [`requests`](https://requests.readthedocs.io/en/latest/) module works this way and does not support asynchronous execution.
