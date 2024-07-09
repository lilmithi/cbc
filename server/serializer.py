from flask import Blueprint, make_response, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, abort, reqparse
from flask_bcrypt import Bcrypt
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, fields
from marshmallow.fields import Nested
from models import (School,Student, Parent, Department, Staff, Grade, Subject, Strand,
                    SubStrand, LearningOutcome, AssessmentRubic, Designation, Year, Term, Report,
                    TokenBlocklist,Category,Stream,db,TeacherSubjectGradeStream,GradeStreamClassTeacher)

serializer_bp = Blueprint('serializer_bp', __name__)
ma = Marshmallow(serializer_bp)
bcrypt = Bcrypt()
api = Api(serializer_bp)


class SchoolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = School
        include_fk = True


schoolSchema = SchoolSchema()

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        include_fk = True

studentSchema = StudentSchema()

class ParentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Parent
        include_fk = True

parentSchema = ParentSchema()


class DepartmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        include_fk = True

departmentSchema = DepartmentSchema()


class StaffSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Staff
        include_fk = True

staffSchema = StaffSchema()


class GradeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Grade
        include_fk = True

gradeSchema = GradeSchema()


class SubjectSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subject
        include_fk = True

subjectSchema = SubjectSchema()


class StrandSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Strand
        include_fk = True

strandSchema = StrandSchema()


class SubStrandSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SubStrand
        include_fk = True

subStrandSchema = SubStrandSchema()


class LearningOutcomeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = LearningOutcome
        include_fk = True

learningOutcomeSchema = LearningOutcomeSchema()


class AssessmentRubicSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AssessmentRubic
        include_fk = True

assessmentRubicSchema = AssessmentRubicSchema()


class DesignationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Designation
        include_fk = True

designationSchema = DesignationSchema()


class YearSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Year
        include_fk = True

yearSchema = YearSchema()


class TermSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Term
        include_fk = True

termSchema = TermSchema()

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk = True

categorySchema = CategorySchema()


class StreamSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Stream
        include_fk = True

streamSchema = StreamSchema()

class TeacherSubjectGradeSchema(SQLAlchemyAutoSchema):
     class Meta:
        model = TeacherSubjectGradeStream
        include_fk = True

teacher_subject_grade_schema = TeacherSubjectGradeSchema()

class GradeStreamClassTeacherSchema(SQLAlchemyAutoSchema):
     class Meta:
        model = GradeStreamClassTeacher
        include_fk = True

grade_stream_class_teacher_schema = GradeStreamClassTeacherSchema()



class ReportSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Report
        include_fk = True
        load_instance = True

    # school = fields.Nested(SchoolSchema)
    # staff = fields.Nested(StaffSchema)
    # year = fields.Nested(YearSchema)
    # term = fields.Nested(TermSchema)
    # grade = fields.Nested(GradeSchema)
    # stream = fields.Nested(StreamSchema)
    # student = fields.Nested(StudentSchema)
    # subject = fields.Nested(SubjectSchema)
    # strand = fields.Nested(StrandSchema)
    # substrand = fields.Nested(SubStrandSchema)
    # learning_outcome = fields.Nested(LearningOutcomeSchema, attribute="learning_outcomes")
    # assessment_rubic = fields.Nested(AssessmentRubicSchema, attribute="assessment_rubics")

reportSchema = ReportSchema()


