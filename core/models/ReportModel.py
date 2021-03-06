from datetime import datetime
import uuid
from flask import session
from utils.Database import Database as base
from bson.objectid import ObjectId
class Report(object):
	def __init__ (self,reportOwner,reportName,reportType,reportDescription,reportLevel,AttackComplexity,AttackVector,getprivilege,reportFile,reportDate=None,reportId=None,reportScore=0,report_status=0,locked=False):
		self.reportId = uuid.uuid4().hex if reportId is None else reportId
		self.reportName = reportName
		self.reportType = reportType
		self.reportDate = datetime.now()
		self.reportLevel = reportLevel
		self.reportOwner = reportOwner
		self.reportScore = reportScore
		self.AttackVector = AttackVector
		self.AttackComplexity = AttackComplexity
		self.getprivilege = getprivilege
		self.reportDescription = reportDescription
		self.reportFile = reportFile
		# report status gonna be as following 1 for accepted 0 for waiting and -1 for rejected by default gonna be defined as waiting
		self.report_status = report_status
		# this field gonna be reserved for locking purposes regarding admin review
		self.locked = locked
		'''i have changed this  please check one more time'''
	@classmethod
	def get_report_name(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportName']
	@classmethod
	def get_report_type(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportType']
	@classmethod
	def get_report_date(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportDate']
	@classmethod
	def get_report_level(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['reportLevel']
	@classmethod
	def get_report(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data
	@classmethod
	def find_reports_by_owner_id(cls,owner_id):
		return [post for post in base.find(collection="reports",query={"reportOwner":owner_id})]
	@classmethod
	def set_score(cls,reportId,score):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			query={"filter":{"reportId":reportId},"update":{"$set":{"reportScore":score}}}
			base.update("reports",query)
			return True
		else:
			return False
	@classmethod
	def register_report(cls,reportOwner,reportName,reportType,reportDescription,reportLevel,AttackComplexity,AttackVector,getprivilege,reportFile):
		#TODO fix report file saving	
		unsavedReport = cls(reportOwner,reportName,reportType,reportDescription,reportLevel,AttackComplexity,AttackVector,getprivilege,reportFile)	
		if unsavedReport is not None:
			unsavedReport.save_mongo()

	@classmethod
	def get_attack_vector(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['AttackVector']
	@classmethod
	def get_attack_complexity(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['AttackComplexity']
	@classmethod
	def get_priviliges(cls,reportId):
		data = base.find_one("reports",{"reportId":reportId})
		if data is not None:
			return data['getprivilege']
	@classmethod
	def get_reportFile(cls,reportId):
		data = base.find_one("reports",{"reportId" : reportId})
		if data is not None:
			return data['reportFile']
	@staticmethod
	def get_reports_queue(reportOwner):
		data = base.find("reports",{"reportOwner":{"$eq":reportOwner},"status":{"$eq":0}})
		if data is not None:
			return data.count()+1
	@staticmethod
	def get_all_reports_count():
		data = base.find("reports",{})
		if data is not None:
			return data.count()
	@staticmethod
	def get_pending_reports_count():
		data = base.find("reports",{"status":{"$eq":0}})
		if data is not None:
			return data.count()
	@staticmethod
	def get_accepted_reports_count():
		data = base.find("reports",{"status":{"$eq":1}})
		if data is not None:
			return data.count()
	@staticmethod
	def get_rejected_reports_count():
		data = base.find("reports",{"status":{"$eq":-1}})
		if data is not None:
			return data.count()
	@staticmethod
	def get_all_reports():
		data = base.find("reports",{})
		if data is not None:
			return list(data)
	@staticmethod
	def get_all_pending_reports():
		data = base.find("reports",{"status":{"$eq":0}})
		if data is not None:
			return list(data)
	@staticmethod
	def get_all_accepted_reports():
		data= base.find("reports",{"status":{"$eq":1}})
		if data is not None:
			return list(data)
	@staticmethod
	def get_all_rejected_reports():
		data = base.find("reports",{"status":{"$eq":-1}})
		if data is not None:
			return list(data)
	@classmethod
	def delete(self,_id):
		base.delete("reports",{"reportId":_id})
	@classmethod
	def update(self,_id,field,value):
		base.update("reports",{"filter":{"reportId":_id},"update":{"$set":{field:value}}})
	@classmethod
	def get_report_status_per_user(cls,reportOwner,state):
		data = base.find("reports",{"reportOwner":{"$eq":reportOwner},"status":{"$eq":state}})
		if data is not None:
			return data.count()
	def json(self):
		return{
		"reportName":self.reportName,
		"reportType":self.reportType,
		"reportLevel":self.reportLevel,
		"reportOwner":self.reportOwner,
		"AttackVector":self.AttackVector,
		"AttackComplexity":self.AttackComplexity,
		"getprivilege":self.getprivilege,
		"reportId":self.reportId,
		"reportDate" :self.reportDate,
		"reportScore" : self.reportScore,
		"reportFile" : self.reportFile,
		"reportDescription" : self.reportDescription,
		"status":self.report_status,
		"locked":self.locked}
	def save_mongo(self):
		base.insert("reports",self.json())