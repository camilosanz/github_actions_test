# Teams Attendance app

## High Level Overview

Multiple Teams send Attendance Report to our shared folder on daily basis. 

The file format is csv  but values are tab separated values

Multiple files for the same date **mm/dd/yyy** can arrive the same day, and they can contain same data

Your work consist on developing a console app that allows the user to answer the following questions

- What is the number of Partipants attending General Meeting per date, date filter between 9/12/2022 and 9/16/2022?
- What is the Meeting duration of General Meeting per date, date filter between between 9/12/2022 and 9/16/2022?

## App overview

When the user launches the app you need to present a menu of "template" questions allowing the user to select the question and then input required data for the selected question; once the required input data is entered then the app will do its works and respond the user by printing the answer in pretty json format and also writing it to json file

**Questions template**
- What is the number of Partipants attending **{meeting_name}** Meeting per date, date filter between **{start_date}** and **{end_date}**
- What is the duration of **{meeting_name}** Meeting per date, date filter between **{start_date}** and **{end_date}****

**Answers samples**

- What is the number of Partipants attending **General** Meeting per date, date filter between 9/12/2022 and 9/16/2022?

```json
{
    "meeting_title": "General",
    "data": [
        {
            "date": "9/12/2022",
            "participants": -99999
        },
        {
            "date": "9/13/2022",
            "participants": -99999
        },
        {
            "date": "9/14/2022",
            "participants": -99999
        },
        {
            "date": "9/15/2022",
            "participants": -99999
        },
        {
            "date": "9/16/2022",
            "participants": 22
        }
    ]
}
```

- What is the Meeting duration of **General** Meeting per date, date filter between between 9/12/2022 and 9/16/2022?

```json
{   
    "meeting_title": "General",
    "data": [
        {
            "date": "9/12/2022",
            "duration": "0h 0m"
        },
        {
            "date": "9/13/2022",
            "duration": "0h 0m"
        },
        {
            "date": "9/14/2022",
            "duration": "0h 0m"
        },
        {
            "date": "9/15/2022",
            "duration": "0h 0m"
        },
        {
            "date": "9/16/2022",
            "duration": "1h 3m"
        }
    ]
}
```

## Usage
**To run tests open a shell**

  ```bash

  $ cd /path to/teams_attendance_app
  ```


  *Run the entire test suite*
    
  ``` bash
  $ pytest 
  ```

  *Run the tests for a certain file matching a keyword*
    
  ``` bash
  $ pytest -k <test_file_name>
  ```

  *Run tests while printing all variables and verbose output*

  ``` bash
  $ pytest -vvl
  ```

**To run the app open a shell**

  ```bash

  $ cd /path to/teams_attendance_app/src
  ```

  *Run the app*
    
  ``` bash
  $ python3 main.py 
  ```

## Docker usage

## With Docker

#### Building

Building process

``` bash
$ docker build <host>/attendance_app:<tag>
```

#### Interactive output

To interact with image just run the container without any _args_

``` bash
$ docker run -v "host_folder:/attendance_app/output" -it --rm <host>/attendance_app:<tag>
```

#### Persiste output

To get the output of 

``` bash
$ docker run -v "host_folder:/attendance_app/output" -it --rm <host>/attendance_app:<tag> [args]
```

Args:

- **-o**: Option to process request { 1, 2 }
- **-m**: Name of meeting to search for
- **-sd**: Start date of meeting (YYYY-MM-DD format)
- **-ed**: End date of meeting (YYYY-MM-DD format)

<ins>Example</ins>

``` bash
$ docker run -v "$(pwd)/output:/attendance_app/output" -it --rm <host>/attendance_app:<tag> -o 1 -m general -sd 2022-09-10 -ed 2022-09-20
```

## Docker compose Usage

### Building image

``` bash
$ docker compose build
```

### Running

#### Interactive mode

``` bash
$ docker compose run team-attendance-app
```

#### Parameters pass

``` bash
$ docker compose run team-attendance-app [args]
```

Args:

- **-o**: Option to process request { 1, 2 }
- **-m**: Name of meeting to search for
- **-sd**: Start date of meeting (YYYY-MM-DD format)
- **-ed**: End date of meeting (YYYY-MM-DD format)

<ins>Example</ins>

``` bash
$ docker compose run attendance-app-build -o 1 -m general -sd 2022-09-10 -ed 2022-09-20
```

## Python Usage

### Flake8

For testing porpuses

```python
python -m flake8
```
