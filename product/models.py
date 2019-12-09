from django.db import models

class Sale(models.Model):
	reason = models.CharField(max_length=128)
	percent = models.IntegerField()

	def __str__(self):
		return '{} => {}'.format(self.reason, self.percent)



class Good(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	price = models.IntegerField()
	sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{} => {}'.format(self.title, self.price)
