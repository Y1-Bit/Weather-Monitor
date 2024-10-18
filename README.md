# Weather-Monitor

## Description

This project is designed for collecting and exporting weather data. It uses an API to fetch weather data, saves it in a database, and provides the ability to export the data in Excel format.

## Installation

1. Ensure you have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/) installed.

2. Clone the repository:
   ```bash
   git clone https://github.com/Y1-Bit/Weather-Monitor.git
   cd Weather-Monitor

## Commands

Run the application:

```bash
make up
```
This command starts the application in the background.


Apply migrations:

```bash
make migrate
```
This command applies the migrations to the database to create the necessary tables and fields.


Export data:

```bash
make export
```
This command exports the latest weather data to the file data/latest_weather_data.xlsx.
