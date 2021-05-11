from django.db import models

class UserData(models.Model):
	created_date=models.DateTimeField(auto_now=True)
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=20)
	status=models.CharField(max_length=20, default='Unactive')
	class Meta:
		db_table="UserData"