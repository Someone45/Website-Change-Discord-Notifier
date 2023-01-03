# Website Change Notifier

WCN is a Python library for checking when a website has changed.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install discord
```

## Usage

Replace the URL of the website you would like to get updates on and the discord token (plus other information) in order to have the bot relay the information to you. You can always create your own custom API for the notifications to be sent through.

This works by converting the response of the website in a hash which is then compared to the response of the website after x amount of time has passed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
