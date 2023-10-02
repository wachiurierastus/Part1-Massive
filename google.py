from pydrive.auth import GoogleAuth

from src import google_drive_save


def trial_upload():
    functions.google_upload(source_folder="outputs", destination_folder="CAT1/outputs", parent_folder="root")

    # Authenticate Google services
    gauth = GoogleAuth()


trial_upload()
