import pandas as pd
from datetime import datetime
from flask import jsonify
from dao.meeting import MeetingDAO
from handler.insert_update_handler import clean_data


class MeetingHandler:
    def mapToDict(self, tuple):
        result = {}
        result["mid"] = tuple[0]
        result["ccode"] = tuple[1]
        result["starttime"] = tuple[2].strftime("%H:%M:%S") if hasattr(tuple[2], 'strftime') else tuple[2]
        result["endtime"] = tuple[3].strftime("%H:%M:%S") if hasattr(tuple[3], 'strftime') else tuple[3]
        result["cdays"] = tuple[4]
        return result
    
    def confirmDataInDF(self, df_to_verify, df_meeting):
        columns_to_check = ["ccode", "starttime", "endtime", "cdays"]
        df_meeting = df_meeting.astype({col: str for col in columns_to_check})
        df_to_verify = df_to_verify.astype({col: str for col in columns_to_check})
        
        # Check if the data to insert is already in the database
        values_to_check = df_to_verify[columns_to_check].iloc[0]
        duplicate_count = df_meeting[columns_to_check].eq(values_to_check).all(axis=1).sum()
        
        return duplicate_count == 1

    def getAllMeeting(self):
        result = []
        dao = MeetingDAO()
        temp = dao.getAllMeeting()

        for row in temp:
            result.append(self.mapToDict(row))
        return jsonify(result)

    def getMeetingByMid(self, mid):
        dao = MeetingDAO()
        result = dao.getMeetingByMid(mid)

        if result is not None:
            return jsonify(self.mapToDict(result))
        else:
            return "Not Found", 404
    
    def insertMeeting(self, meeting_json):
        if "ccode" not in meeting_json or "starttime" not in meeting_json or "endtime" not in meeting_json or "cdays" not in meeting_json:
            return "Missing required fields", 400
        
        ccode = meeting_json["ccode"]
        starttime = datetime.strptime(meeting_json["starttime"], "%H:%M:%S").strftime("%H:%M:%S")
        endtime = datetime.strptime(meeting_json["endtime"], "%H:%M:%S").strftime("%H:%M:%S")
        cdays = meeting_json["cdays"]
        
        data = {
            "mid": 1000,
            "ccode": [ccode],
            "starttime": [starttime],
            "endtime": [endtime],
            "cdays": [cdays]
        }
        df_to_insert = pd.DataFrame(data)
        df_list = clean_data(df_to_insert, "meeting")
        
        df_meeting = []
        for df, df_name in df_list:
            if df_name == "meeting":
                df_meeting = df

                
        is_data_confirmed = self.confirmDataInDF(df_to_insert, df_meeting)
        
        if is_data_confirmed:
            dao = MeetingDAO()
            mid = dao.insertMeeting(ccode, starttime, endtime, cdays)
            temp = (mid, ccode, starttime, endtime, cdays)
            
            return self.mapToDict(temp), 201
        
        else:
            return "Data can't be inserted due to duplicates or record already exists", 400
        
    def getMostMeeting(self):
        result = []
        dao = MeetingDAO()
        temp = dao.getMostMeeting()
        
        for row in temp:
            result.append(self.mapToDict(row))
        return jsonify(result)