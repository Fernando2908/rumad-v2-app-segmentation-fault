from flask import Flask, jsonify, request
from flask_cors import CORS


from handler.section import SectionHandler
from handler.meeting import MeetingHandler
from handler.requisite import RequisiteHandler

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "This is the RestAPI of Segmentation Fault team."


@app.route("/segmentation_fault/section")
def section():
    return SectionHandler().getAllSection()


@app.route("/segmentation_fault/section/<int:sid>")
def getSectionBySid(sid):
    return SectionHandler().getSectionBySid(sid)


@app.route("/segmentation_fault/meeting")
def meeting():
    return MeetingHandler().getAllMeeting()


@app.route("/segmentation_fault/meeting/<int:mid>")
def getMeetingByMid(mid):
    return MeetingHandler().getMeetingByMid(mid)


@app.route("/segmentation_fault/room")  # type: ignore
def room():
    pass


@app.route("/segmentation_fault/class")  # type: ignore
def courses():
    pass


@app.route("/segmentation_fault/requisite")
def requisite():
    return RequisiteHandler().getAllRequisite()


@app.route("/segmentation_fault/requisite/<int:classid>/<int:reqid>")
def getRequisiteByClassIdReqId(classid, reqid):
    return RequisiteHandler().getRequisiteByClassIdReqId(classid, reqid)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
