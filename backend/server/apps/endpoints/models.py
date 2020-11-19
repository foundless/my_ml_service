from django.db import models

# Create your models here.

class Endpoint(models.Model):
	'''
	The Endpoint object represents ML API endpoint
	Attributes:
		name:The name of the endpoint, it will be used in API URL
		owner: The string with owner name
		created_at: The date when endpoint was created
	'''
	name = models.CharField(max_length=128)
	owner = models.CharField(max_length = 128)
	created_at = models.DateTimeField(auto_now_add = True, blank=True)

class MLAlgorithm(models.Model):
	'''
	The MLAlgorithm represent the ML algoritm object.
	'''
	name = models.CharField(max_length = 128)
	description = models.CharField(max_length = 10000)
	code = models.CharField(max_length = 50000)
	version = models.CharField(max_length = 128)
	owner =  models.CharField(max_length = 128)
	created_at = models.DateTimeField(auto_now_add = True, blank=True)
	parent_endpoint=models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
	status =  models.CharField(max_length = 128)
	active =  models.BooleanField()
	created_by =  models.CharField(max_length = 128)
	created_at =  models.DateTimeField(auto_now_add=True, blank=True)
	parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")

class MLRequest(models.Model):
	'''
	The MLRequest will keep information about all requests to ML algorithms
	'''
	input_data =  models.CharField(max_length = 10000)
	full_response =  models.CharField(max_length = 10000)
	response =  models.CharField(max_length = 10000)
	feedback =  models.CharField(max_length = 10000)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)
