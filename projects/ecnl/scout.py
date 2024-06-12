import os
import csv
import requests

from typing import List
from dataclasses import dataclass

"""
This code is written based of evaluations from

https://public.totalglobalsports.com/public/event/3064/college-list
"""


@dataclass
class Coach:
    name: str
    title: str
    email: str

    def __init__(self):
        self.name = ""
        self.title = ""
        self.email = ""


@dataclass
class Program:
    name: str
    sport: str
    division: str
    conference: str
    location: str
    type: str
    website: str
    coaches: List[Coach]

    def __init__(self):
        self.name = ""
        self.sport = ""
        self.division = ""
        self.conference = ""
        self.location = ""
        self.type = ""
        self.website = ""
        self.coaches = []


@dataclass
class Division:
    id: int
    name: str


@dataclass
class Conference:
    id: int
    divisionId: int
    name: str


@dataclass
class State:
    id: int
    regionId: int | None
    countryId: int | None
    code: str
    name: str
    image: str
    timeZoneId: str

def get_college_division_list() -> List[Division]:
    url = "https://public.totalglobalsports.com/api/player/get-college-division-list"
    response = requests.get(url)
    data = response.json()

    divisions = []
    for item in data['data']:
        division = Division(id=item['collegeDivisionID'], name=item['collegeDivisionName'])
        divisions.append(division)

    return divisions


def get_college_conference_list() -> List[Conference]:
    url = "https://public.totalglobalsports.com/api/player/get-college-conference-list"
    response = requests.get(url)
    data = response.json()

    conferences = []
    for item in data['data']:
        conference = Conference(id=item['collegeconferenceID'],
                                divisionId=item['collegedivisionID'],
                                name=item['conferencename'])
        conferences.append(conference)

    return conferences


def get_all_states() -> List[State]:
    url = "https://public.totalglobalsports.com/api/player/get-all-states"

    response = requests.get(url)
    data = response.json()

    states = []
    for item in data['data']:
        state = State(id=item['stateID'],
                      regionId=item['regionID'],
                      countryId=item['countryID'],
                      code=item['stateCode'],
                      name=item['stateName'],
                      image=item['stateImage'],
                      timeZoneId=item['timeZoneID'])
        states.append(state)

    return states




def get_event_details(eventId: int):
    url = f"https://public.totalglobalsports.com/public/event/{eventId}/college-list"

    response = requests.get(url)
    data = response.json()


def get_colleges_attending_list_with_coaches_by_event(eventId: int) -> List[Program]:
    url = f"https://public.totalglobalsports.com/api/player/get-colleges-attending-list-with-coaches-by-event/{eventId}"
    response = requests.get(url)
    data = response.json()

    programs = []
    for item in data['data']:
        program = Program()
        program.name = item['collegeName']
        program.sport = item['sportName']
        program.division = item['collegeDivisionName']
        program.conference = item['conferenceName']
        program.location = item['location']
        program.type = item['type']
        program.website = item['website']

        for coach in item['coaches']:
            c = Coach()
            c.name = coach['name']
            c.title = coach['title']
            c.email = coach['email']
            program.coaches.append(c)

        programs.append(program)

    return programs


if __name__ == "__main__":
    divisions = get_college_division_list()
    conferences = get_college_conference_list()
    states = get_all_states()

    output_file = "divisions.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name"])

        for division in divisions:
            writer.writerow([division.id, division.name])

    output_file = "conferences.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Division ID", "Name"])

        for conference in conferences:
            writer.writerow([conference.id, conference.divisionId, conference.name])


    output_file = "states.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Code", "Image", "Time Zone ID"])

        for state in states:
            writer.writerow([state.id, state.name, state.code, state.image, state.timeZoneId])

    # output_file = "scout.csv"
    #
    # if os.path.exists(output_file):
    #     os.remove(output_file)
    #
    # with open(output_file, "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["University", "Sport", "Division", "Conference", "Location", "Type", "Website", "Coach Name", "Coach Title", "Coach Email"])
    #
    #     for program in programs:
    #         for coach in program.coaches:
    #             writer.writerow([program.name, program.sport, program.division, program.conference, program.location, program.type, program.website, coach.name, coach.title, coach.email])