import os
import csv
import requests

from typing import List, Tuple, Optional
from dataclasses import dataclass

"""
This code is written based of evaluations from

https://public.totalglobalsports.com/public/event/3064/college-list
"""


@dataclass
class Coach:
    id: str
    collegeId: int
    userRoleId: int
    firstName: str
    lastName: str
    email: str
    phone: str
    role: str
    roleId: int
    userId: int
    userImage: str
    collegeProgramId: int
    publish: int
    statusId: int
    publicEmail: str
    publicEmailDisplayEnabled: int


@dataclass
class CollegeInfo:
    programId: int
    description: str
    collegeId: int
    sportId: int
    eventId: int
    collegeName: str
    city: str
    type: str
    logo: str
    statecode: str
    conferenceName: str
    collegeDivisionId: int
    collegeDivisionName: str
    gender: str
    webSite: str
    status: str
    publish: int
    stateId: int
    collegeConferenceId: int
    coaches: List[Coach]


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
    regionId: Optional[int]
    countryId: Optional[int]
    code: str
    name: str
    image: str
    timeZoneId: str


@dataclass
class EventData:
    eventID: int
    eventLogo: str
    eventPublicBanner: Optional[str]
    eventBGImage: Optional[str]
    eventBGColor: str
    name: str
    description: Optional[str]
    feeSummary: str
    orgTypeID: int
    regStartDate: Optional[str]
    regEndDate: Optional[str]
    regStatus: bool
    regStatusText: str
    location: str
    address: str
    city: str
    zip: str
    stateID: int
    eventSubTypeID: int
    eventStartDate: str
    eventEndDate: str
    eventFeatures: Optional[str]
    tournamentPurchaseCost: int
    paymentDate: str
    transactionID: Optional[str]
    cardType: Optional[str]
    maskedCardNum: Optional[str]
    originalAmount: Optional[str]
    discountAmount: Optional[str]
    orgID: int
    appID: str
    stateCode: str


def get_college_division_list() -> List[Division]:
    url = "https://public.totalglobalsports.com/api/player/get-college-division-list"
    response = requests.get(url)
    data = response.json()

    divisions = []
    for item in data["data"]:
        division = Division(id=item["collegeDivisionID"], name=item["collegeDivisionName"])
        divisions.append(division)

    return divisions


def get_college_conference_list() -> List[Conference]:
    url = "https://public.totalglobalsports.com/api/player/get-college-conference-list"
    response = requests.get(url)
    data = response.json()

    conferences = []
    for item in data["data"]:
        conference = Conference(id=item["collegeconferenceID"],
                                divisionId=item["collegedivisionID"],
                                name=item["conferencename"])
        conferences.append(conference)

    return conferences


def get_all_states() -> List[State]:
    url = "https://public.totalglobalsports.com/api/player/get-all-states"

    response = requests.get(url)
    data = response.json()

    states = []
    for item in data["data"]:
        state = State(id=item["stateID"],
                      regionId=item["regionID"],
                      countryId=item["countryID"],
                      code=item["stateCode"],
                      name=item["stateName"],
                      image=item["stateImage"],
                      timeZoneId=item["timeZoneID"])
        states.append(state)

    return states




def get_event_details(eventId: int) -> EventData:
    # url = f"https://public.totalglobalsports.com/public/event/{eventId}/college-list"
    url = f"https://public.totalglobalsports.com/api/Event/get-event-details-by-eventID/{eventId}"

    response = requests.get(url)
    data = response.json().get("data")

    event = EventData(eventID=data["eventID"],
                      eventLogo=data["eventLogo"],
                      eventPublicBanner=data["eventPublicBanner"],
                      eventBGImage=data["eventBGImage"],
                      eventBGColor=data["eventBGColor"],
                      name=data["name"],
                      description=data["description"],
                      feeSummary=data["feeSummary"],
                      orgTypeID=data["orgTypeID"],
                      regStartDate=data["regStartDate"],
                      regEndDate=data["regEndDate"],
                      regStatus=data["regStatus"],
                      regStatusText=data["regStatusText"],
                      location=data["location"],
                      address=data["address"],
                      city=data["city"],
                      zip=data["zip"],
                      stateID=data["stateID"],
                      eventSubTypeID=data["eventSubTypeID"],
                      eventStartDate=data["eventStartDate"],
                      eventEndDate=data["eventEndDate"],
                      eventFeatures=data["eventFeatures"],
                      tournamentPurchaseCost=data["tournamentPurchaseCost"],
                      paymentDate=data["paymentDate"],
                      transactionID=data["transactionID"],
                      cardType=data["cardType"],
                      maskedCardNum=data["maskedCardNum"],
                      originalAmount=data["originalAmount"],
                      discountAmount=data["discountAmount"],
                      orgID=data["orgID"],
                      appID=data["appID"],
                      stateCode=data["stateCode"])

    return event


def get_colleges_attending_list_with_coaches_by_event(eventId: int) -> List[CollegeInfo]:
    url = f"https://public.totalglobalsports.com/api/Event/get-colleges-attending-list-with-coaches-by-event/{eventId}"
    response = requests.get(url)
    data = response.json()

    infos = []
    for item in data["data"]:
        info = CollegeInfo(programId=item["collegeInfo"]["collegeprogramID"],
                           description=item["collegeInfo"]["description"],
                           collegeId=item["collegeInfo"]["collegeID"],
                           sportId=item["collegeInfo"]["sportID"],
                           eventId=item["collegeInfo"]["eventID"],
                           collegeName=item["collegeInfo"]["collegename"],
                           city=item["collegeInfo"]["city"],
                           type=item["collegeInfo"]["type"],
                           logo=item["collegeInfo"]["logo"],
                           statecode=item["collegeInfo"]["statecode"],
                           conferenceName=item["collegeInfo"]["conferencename"],
                           collegeDivisionId=item["collegeInfo"]["collegeDivisionID"],
                           collegeDivisionName=item["collegeInfo"]["collegedivisionname"],
                           gender=item["collegeInfo"]["gender"],
                           webSite=item["collegeInfo"]["webSite"],
                           status=item["collegeInfo"]["status"],
                           publish=item["collegeInfo"]["publish"],
                           stateId=item["collegeInfo"]["stateID"],
                           collegeConferenceId=item["collegeInfo"]["collegeConferenceID"],
                           coaches=[])

        for coach in item["coachList"]:
            c = Coach(id=coach["id"],
                      collegeId=coach["collegeid"],
                      userRoleId=coach["userRoleID"],
                      firstName=coach["firstname"],
                      lastName=coach["lastname"],
                      email=coach["email"],
                      phone=coach["phone"],
                      role=coach["role"],
                      roleId=coach["roleID"],
                      userId=coach["userid"],
                      userImage=coach["userImage"],
                      collegeProgramId=coach["collegeprogramID"],
                      publish=coach["publish"],
                      statusId=coach["statusID"],
                      publicEmail=coach["publicEmail"],
                      publicEmailDisplayEnabled=coach["publicEmailDisplayEnabled"])

            info.coaches.append(c)

        infos.append(info)

    return infos


def find_coach(coach: Coach, accumulator: List[Tuple[CollegeInfo, Coach]]) -> int:
    for i, (current_college, current_coach) in enumerate(accumulator):
        if coach.id == current_coach.id:
            return i

    return -1


def process_event(eventId: int, accumulator: List[Tuple[CollegeInfo, Coach]]):
    event = get_event_details(eventId)
    colleges = get_colleges_attending_list_with_coaches_by_event(eventId)

    output_file = f"{eventId}_scout.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["College Name", "City", "State", "URL", "Name", "Role", "Email", "Phone"])

        for college in colleges:
            for coach in college.coaches:
                writer.writerow([college.collegeName,
                                 college.city,
                                 college.statecode,
                                 college.webSite,
                                 f"{coach.firstName} {coach.lastName}",
                                 coach.role,
                                 coach.email,
                                 coach.phone])

                # Check if college and coach are already in accumulator
                if not any(
                        c.collegeName == college.collegeName and o.firstName == coach.firstName and o.lastName == coach.lastName
                        for c, o in accumulator):
                    accumulator.append((college, coach))


if __name__ == "__main__":
    divisions = get_college_division_list()
    conferences = get_college_conference_list()
    states = get_all_states()

    accumulator = []

    output_file = f"divisions.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name"])

        for division in divisions:
            writer.writerow([division.id, division.name])

    output_file = f"conferences.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Division ID", "Name"])

        for conference in conferences:
            writer.writerow([conference.id, conference.divisionId, conference.name])

    output_file = f"states.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Code", "Image", "Time Zone ID"])

        for state in states:
            writer.writerow([state.id, state.name, state.code, state.image, state.timeZoneId])

    process_event(3009, accumulator)
    process_event(3010, accumulator)
    process_event(2992, accumulator)
    process_event(3016, accumulator)
    process_event(3028, accumulator)
    process_event(3030, accumulator)
    process_event(3031, accumulator)
    process_event(3033, accumulator)
    process_event(3035, accumulator)
    process_event(3036, accumulator)
    process_event(3064, accumulator)

    output_file = "scout.csv"

    if os.path.exists(output_file):
        os.remove(output_file)

    # Sort the accumulator by college name then by coach name
    accumulator.sort(key=lambda x: (x[0].collegeName, x[1].lastName, x[1].firstName))

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["College Name", "Division", "Conference", "City", "State", "URL", "Name", "Role", "Email", "Phone"])

        for college, coach in accumulator:
            writer.writerow([college.collegeName,
                             college.collegeDivisionName,
                             college.conferenceName,
                             college.city,
                             college.statecode,
                             college.webSite,
                             f"{coach.firstName} {coach.lastName}",
                             coach.role,
                             coach.email,
                             coach.phone])
