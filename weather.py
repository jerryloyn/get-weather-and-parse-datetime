from datetime import date, datetime, timedelta
import requests
import json
import textwrap


def get_data(info):
    """Send API request to HKO for weather information.

    Args:
    info (str): The request info which can either be `current_temp` or `forecast` only.

    Returns:
    dict

    Raises:
    ValueError: If info is not `current_temp` or `forecast`
    """

    # check info arg value
    if info not in ["current_temp", "forecast"]:
        raise ValueError(
            "info can either be `current_temp` or `forecast` only")

    info_map = {
        "current_temp": "rhrread",
        "forecast": "fnd"
    }

    # send api request to HKO
    payload = {"dataType": info_map[info], "lang": "en"}
    r = requests.get(
        "https://data.weather.gov.hk/weatherAPI/opendata/weather.php", params=payload)

    return json.loads(r.content)


def format_current_temp(data, **kwargs):
    """Print current temperature.

    Args:
    data (dict): The current temperature data.
    **kwargs: Arbitrary keyword arguments.
        *kwargs* are used to specify additional parameters like `district`

    Returns:
    None
    """

    # format district temperature data
    district_temp_str = u">> {place}: {temp}\N{DEGREE SIGN}C"

    print("Current temperature:\n---------")

    # loop the temperature data for every district
    for d in data["temperature"]["data"]:

        if kwargs.get("district") is None or kwargs.get("district") == d["place"]:
            print(district_temp_str.format(place=d["place"],
                                           temp=d["value"]))


def format_forecast(data, **kwargs):
    """Print next 3 days temperature and humidity forecast.

    Args:
    data (dict): The forecast data
    **kwargs: Arbitrary keyword arguments.

    Returns:
    None
    """

    # get the list of next 3 days
    today = date.today()
    forecast_days = [today + timedelta(days=i) for i in range(1, 4)]

    # format daily data
    daily_forecast_str = textwrap.dedent(u"""\
    {weekday} (Date of {date})
    >> Temperature:
    >>>> Max.: {max_temp}\N{DEGREE SIGN}C
    >>>> Min: {min_temp}\N{DEGREE SIGN}C
    >> Humidity:
    >>>> Max: {max_hum}%
    >>>> Min {min_hum}%
    --------- """)

    print("Next 3-day weather forecast:\n---------")

    # loop the temperature data for every day
    for d in data["weatherForecast"]:
        forecast_day = datetime.strptime(d["forecastDate"], "%Y%m%d").date()

        if forecast_day in forecast_days:
            print(daily_forecast_str.format(weekday=forecast_day.strftime('%a'),
                                            date=forecast_day.strftime(
                                                "%Y-%m-%d"),
                                            max_temp=d["forecastMaxtemp"]["value"],
                                            min_temp=d["forecastMintemp"]["value"],
                                            max_hum=d["forecastMaxrh"]["value"],
                                            min_hum=d["forecastMinrh"]["value"]))


def main(info, **kwargs):
    format_func_map = {
        "current_temp": format_current_temp,
        "forecast": format_forecast
    }

    data = get_data(info)
    format_func_map[info](data, **kwargs)


if __name__ == "__main__":

    # get current temperature
    main("current_temp")

    # get current temperature in Sha Tin
    main("current_temp", district="Sha Tin")

    # get next 3 days weather forecast
    main("forecast")
