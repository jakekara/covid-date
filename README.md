# covid-date

Print the covid date since you entered lockdown. Each day is one year!

For those of us working at Yale, the start date was usually March
18. See the "Use a different date" section below to set a custom covid
epoch start date.

### Install

```bash
$ pip install git+https://github.com/jakekara/covid-date
```

Or use
[pipx](https://packaging.python.org/guides/installing-stand-alone-command-line-tools/). It's
a good way to install standalone CLI tools.


### Usage

```bash
$ covid-date
Covid Year 105
```

### Use a different date

To use a different date, create a yaml file called "covid-date.yaml"
in your home directory. (There's an example file in this repo that
changes the start date to March 15, 2020).

The yaml file should have a single value, "start" in YYYY-MM-DD
format. Like so:

```yaml
start: 2020-03-15
```