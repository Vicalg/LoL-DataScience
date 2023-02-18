import pickle
import os

# Function for loading the pickle file
def load_file(filename: str) -> list:
    """ Load the file having the information of matches into a variable

    Keyword argument:
    filename -- Name of the file with the data (string)

    Return:
    matches_list -- List with the data (list)
    """
    path_data = os.path.dirname(os.getcwd()) + "\\Data\\" + filename 
    with open(path_data, "rb") as file:
        matches_list = pickle.load(file)
    return matches_list

def read_puuid(filename: str) -> str:

    # Reading my puuid (Player Universally Unique IDentifiers) - If i need to use it
    path = os.path.dirname(os.getcwd()) + "\\Keys\\" + filename
    with open(path, "r") as file:
        puuid = file.read()
    return puuid

#def clean_matches()
#
#for information in list_keys_info_participants:
#    df[information] = [matches_no_error[x]["info"]["participants"][index_puuid_match(matches_no_error[x])].get(information) for x in range(len(matches_no_error))]


# Extract the information for a given player on a match
def index_puuid_match(match ,puuid):
    """
    match: specific match (json file)
    puuid: player unique identifier (string)
    return: index value for the summoner with the given puuid (int)
    """
    return(match["metadata"]["participants"].index(puuid))