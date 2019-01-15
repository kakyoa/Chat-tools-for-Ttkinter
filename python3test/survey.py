#coding=utf-8
#¼±¼±¼±
class AnonymousSurvey():
	
	
	def __init__(self,question):
		self.question = question
		seslf.response = []
		
	def show_question(self):
		print(question)
		
	def store_response(self,new_response):
		self.responses.append(new_response)
		
	def show_results(self):
		print("Survey results:")
		for response in responses:
			print("- " + response)
