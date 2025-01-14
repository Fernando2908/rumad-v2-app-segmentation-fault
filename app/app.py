from flask import Flask, request
from flask_cors import CORS

from handler.section import SectionHandler
from handler.meeting import MeetingHandler
from handler.requisite import RequisiteHandler
from handler.course import ClassHandler
from handler.room import RoomHandler
from handler.registration import RegistrationHandler

app = Flask(__name__)
CORS(app)


# ROOT ROUTE
@app.route("/")
def hello_world():
    return "This is the RestAPI of Segmentation Fault team."


# SECTION ROUTES
@app.route("/segmentation_fault/section", methods=["GET", "POST"])
def section():
    if request.method == "GET":
        return SectionHandler().getAllSection()
    else:
        return SectionHandler().insertSection(request.json)


@app.route("/segmentation_fault/section/<int:sid>", methods=["GET", "PUT", "DELETE"])
def sectionByID(sid):
    if request.method == "DELETE":
        return SectionHandler().deleteSectionBySid(sid)
    elif request.method == "PUT":
        return SectionHandler().updateSectionBySid(sid, request.json)
    else:
        return SectionHandler().getSectionBySid(sid)


# MEETING ROUTES
@app.route("/segmentation_fault/meeting", methods=["GET", "POST"])
def meeting():
    if request.method == "GET":
        return MeetingHandler().getAllMeeting()
    else:
        return MeetingHandler().insertMeeting(request.json)


@app.route("/segmentation_fault/meeting/<int:mid>", methods=["GET", "PUT", "DELETE"])
def meetingByMID(mid):
    if request.method == "GET":
        return MeetingHandler().getMeetingByMid(mid)
    elif request.method == "PUT":
        return MeetingHandler().updateMeetingByMid(mid, request.json)
    else:
        return MeetingHandler().deleteMeetingByMid(mid)


# ROOM ROUTES
@app.route("/segmentation_fault/room", methods=["GET", "POST"])
def room():
    if request.method == "GET":
        return RoomHandler().getAllRoom()
    else:
        return RoomHandler().insertRoom(request.json)


@app.route("/segmentation_fault/room/<int:rid>", methods=["GET", "PUT", "DELETE"])
def roomByRID(rid):
    if request.method == "GET":
        return RoomHandler().getRoomByRid(rid)
    elif request.method == "PUT":
        return RoomHandler().updateRoomByRid(rid, request.json)
    else:
        return RoomHandler().deleteRoomByRid(rid)


# CLASS ROUTES
@app.route("/segmentation_fault/class", methods=["GET", "POST"])
def courses():
    if request.method == "GET":
        return ClassHandler().getAllClass()
    elif request.method == "POST":
        return ClassHandler().insertClass(request.json)


@app.route("/segmentation_fault/class/<int:cid>", methods=["GET", "PUT", "DELETE"])
def courseByID(cid):
    if request.method == "GET":
        return ClassHandler().getclassById(cid)
    elif request.method == "PUT":
        return ClassHandler().updateClassById(cid, request.json)
    elif request.method == "DELETE":
        return ClassHandler().deleteClassById(cid)


# REQUISITE ROUTES
@app.route("/segmentation_fault/requisite", methods=["GET", "POST"])
def requisite():
    if request.method == "GET":
        return RequisiteHandler().getAllRequisite()
    else:
        return RequisiteHandler().insertRequisite(request.json)


@app.route(
    "/segmentation_fault/requisite/<int:classid>/<int:reqid>",
    methods=["GET", "PUT", "DELETE"],
)
def requisiteByClassIdReqId(classid, reqid):
    if request.method == "DELETE":
        return RequisiteHandler().deleteRequisiteByClassIdReqId(classid, reqid)
    elif request.method == "PUT":
        return RequisiteHandler().updateRequisiteByClassIdReqId(
            classid, reqid, request.json
        )
    else:
        return RequisiteHandler().getRequisiteByClassIdReqId(classid, reqid)


# LOCAL STATICS (4/4)
# Top 3 rooms per building with the most capacity
@app.route("/segmentation_fault/room/<string:building>/capacity", methods=["POST"])
def getMaxCapacity(building):
    return RoomHandler().getMaxCapacity(building)


# Top 3 rooms with the most student-to-capacity ratio
@app.route("/segmentation_fault/room/<string:building>/ratio", methods=["POST"])
def getRatioByBuilding(building):
    return RoomHandler().getRatioByBuilding(building)


# Top 3 classes that were taught the most per room
@app.route("/segmentation_fault/room/<id>/classes", methods=["POST"])
def mostPerRoom(id):
    return ClassHandler().getMostPerRoom(id)


# Top 3 most taught classes per semester per year
@app.route("/segmentation_fault/classes/<year>/<semester>", methods=["POST"])
def mostPerSemester(year, semester):
    return ClassHandler().getMostPerSemester(year, semester)


# GLOBAL STATICS (4/4)
# Top 5 meetings with the most sections
@app.route("/segmentation_fault/most/meeting", methods=["POST"])
def mostMeeting():
    return MeetingHandler().getMostMeeting()


# Top 3 classes that appears the most as prerequisite to other classes
@app.route("/segmentation_fault/most/prerequisite", methods=["POST"])
def mostPrerequisite():
    return ClassHandler().getMostPrerequisite()


# Top 3 classes that were offered the least
@app.route("/segmentation_fault/least/classes", methods=["POST"])
def leastClass():
    return ClassHandler().getLeastClass()


# Total number of sections per year
@app.route("/segmentation_fault/section/year", methods=["POST"])
def sectionYear():
    return SectionHandler().getSectionPerYear()


# USER ROUTES
# User login
@app.route("/segmentation_fault/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    return RegistrationHandler().logInUser(username, password)

# User sign up
@app.route("/segmentation_fault/signup", methods=["POST"])
def signup():
    data = request.get_json()  
    username = data.get("username")
    password = data.get("password")
    return RegistrationHandler().signUpUser(username, password)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
