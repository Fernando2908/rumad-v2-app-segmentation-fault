CREATE SEQUENCE IF NOT EXISTS class_seq;
CREATE SEQUENCE IF NOT EXISTS room_seq;
CREATE SEQUENCE IF NOT EXISTS meeting_seq;
CREATE SEQUENCE IF NOT EXISTS section_seq;
CREATE SEQUENCE IF NOT EXISTS syllabus_seq;

-- COURSES TABLE
CREATE TABLE IF NOT EXISTS "class" (
  "cid" INTEGER PRIMARY KEY DEFAULT nextval('class_seq'),
  "cname" VARCHAR(50),
  "ccode" VARCHAR(4),
  "cdesc" VARCHAR(100),
  "term" VARCHAR(35),
  "years" VARCHAR(20),
  "cred" INTEGER NOT NULL,
  "csyllabus" VARCHAR(255)
);

-- ROOM TABLE
CREATE TABLE IF NOT EXISTS "room" (
    "rid" INTEGER PRIMARY KEY DEFAULT nextval('room_seq'),
    "building" VARCHAR(10),
    "room_number" VARCHAR,
    "capacity" INTEGER
);

-- MEETING TABLE
CREATE TABLE IF NOT EXISTS "meeting" (
    "mid" INTEGER PRIMARY KEY DEFAULT nextval('meeting_seq'),
    "ccode" VARCHAR(4),
    "starttime" TIME,
    "endtime" TIME,
    "cdays" VARCHAR(5) 
);

-- SECTION TABLE
CREATE TABLE IF NOT EXISTS "section" (
  "sid" INTEGER PRIMARY KEY DEFAULT nextval('section_seq'),
  "roomid" INTEGER,
  "cid" INTEGER,
  "mid" INTEGER,
  "semester" VARCHAR(10),
  "years" VARCHAR(4),
  "capacity" INTEGER,

  FOREIGN KEY ("roomid") REFERENCES "room"("rid"),
  FOREIGN KEY ("cid") REFERENCES "class"("cid"),
  FOREIGN KEY ("mid") REFERENCES "meeting"("mid")
);

-- VECTOR EXTENSION
CREATE EXTENSION IF NOT EXISTS vector;

-- SYLLABUS TABLE
CREATE TABLE IF NOT EXISTS "syllabus" (
  "chunkid" INTEGER PRIMARY KEY DEFAULT nextval('syllabus_seq'),
  "courseid" INTEGER,
  "embedding_text" vector(500),
  "chunk" VARCHAR(255),

  FOREIGN KEY ("courseid") REFERENCES "class"("cid")
);

-- REQUISITE TABLE
CREATE TABLE IF NOT EXISTS "requisite" (
  "classid" INTEGER,
  "reqid" INTEGER,
  "prereq" BOOLEAN,

  PRIMARY KEY ("classid", "reqid"),
  FOREIGN KEY ("classid") REFERENCES "class"("cid"),
  FOREIGN KEY ("reqid") REFERENCES "class"("cid")
);






