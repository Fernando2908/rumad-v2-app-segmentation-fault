from flask import Flask, jsonify, request
from flask_cors import CORS

from handler.section import SectionHandler
from handler.meeting import MeetingHandler
from handler.requisite import RequisiteHandler

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
        return "POST"


@app.route("/segmentation_fault/section/<int:sid>", methods=["GET", "PUT", "DELETE"])
def sectionByID(sid):
    if request.method == "DELETE":
        return SectionHandler().deleteSectionBySid(sid)
    elif request.method == "PUT":
        return "PUT"
    else:
        return SectionHandler().getSectionBySid(sid)


@app.route("/segmentation_fault/meeting", methods = ['GET', 'POST'])
def meeting():
    if request.method == 'GET':
        return MeetingHandler().getAllMeeting()
    else:
        return MeetingHandler().insertMeeting(request.json)


@app.route("/segmentation_fault/meeting/<int:mid>")
def getMeetingByMid(mid):
    return MeetingHandler().getMeetingByMid(mid)


# ROOM ROUTES
@app.route("/segmentation_fault/room")  # type: ignore
def room():
    pass


# CLASS ROUTES
@app.route("/segmentation_fault/class", methods=["GET", "POST"])
def courses():
    if request.method == "GET":
        return ClassHandler().getAllClass()
    elif request.method == "POST":
        return ClassHandler().insertClass(request.json)
    
@app.route("/segmentation_fault/class/<int:cid>", methods=["GET", "PUT", "DELETE"])
def courses2(cid):
    if request.method == "GET":
        return ClassHandler().getclassById(cid)
    elif request.method == "PUT":
        return ClassHandler().updateClassById(cid, request.json)
    elif request.method == "DELETE":
        return ClassHandler().deleteClassById(cid)

@app.route("/segmentation_fault/requisite", methods = ['GET', 'POST'])
def requisite():
    if request.method == 'GET':
        return RequisiteHandler().getAllRequisite()
    else:
        return RequisiteHandler().insertRequisite(request.json)


@app.route("/segmentation_fault/requisite/<int:classid>/<int:reqid>", methods=["GET", "PUT", "DELETE"])
def requisiteByClassIdReqId(classid, reqid):
    if request.method == "DELETE":
        return RequisiteHandler().deleteRequisiteByClassIdReqId(classid, reqid)
    elif request.method == "PUT":
        return "PUT"
    else:
        return RequisiteHandler().getRequisiteByClassIdReqId(classid, reqid)
