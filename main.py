# This is a sample Python script.
import pandas as pd
import os
import xlsxwriter
import json

def ExportJsonToExcel(pathToJsonFile):
    with open(pathToJsonFile) as json_file:
        participantsData = (json.load(json_file))["participants"]
        df = pd.DataFrame(participantsData)
        df.to_excel('DATAFILE.xlsx')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pathToJsonPushUpEvent = 'PushUpEvent.txt'
    pathToJsonRunEvent = 'RunEvent.txt'

    ExportJsonToExcel(pathToJsonPushUpEvent)