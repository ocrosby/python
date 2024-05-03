from typing import List

class Player:
    def __init__(self):
        self.Name = None


def get_nwsl_players() -> List[Player]:
    """
    @url "https://nwsl-api-prd-sdp.akamaized.net/v1/nwsl/football/seasons/nwsl::Football_Season::fe17bea0b7234cf7957c7249cb828270/stats/players?locale=en-US&category=general&orderBy=goals&role=all&direction=desc&page=1&pageNumElement=400"
    :return:
    """
    players = []

    # Retrieve all the players from the NWSL.


if __name__ == "__main__":
    print("Hello, World!")

    # Step 1: Gather the Data
    # You need data on NWSL players and their respective college programs.
    # This could include names of players, the colleges they attended,
    # and perhaps years of attendance
