from datetime import datetime, date
import yaml
import os.path
import sys

def get_epoch():

    # Default to March 28, 2020
    ret = date(2020, 3, 18)

    # Check for config file
    yaml_file_path = os.path.expanduser(os.path.join("~", ".covid-date.yaml"))
    if os.path.exists(yaml_file_path):
        yaml_data = yaml.load(open(yaml_file_path), Loader=yaml.FullLoader)
        if "epoch" in yaml_data:
            try:
                yaml_date = yaml_data["start"]
                assert type(yaml_date) == type(datetime.now().date())
                ret = yaml_date
            except Exception:
                print(
                    "There's something wrong with your yaml config file. "
                    "Using default date " + str(ret),
                    file=sys.stderr)

    return ret


def covid_year(date):
    covid_epoch = get_epoch()

    covid_years = (date - covid_epoch).days
    return covid_years

def covid_year_now():
    current_date = datetime.now().date()
    return covid_year(current_date)
