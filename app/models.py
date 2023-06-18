from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    d_name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.d_name
class Emp(models.Model):
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    emp_no=models.IntegerField()
    emp_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    manager=models.CharField(max_length=100)
    mgr_id=models.IntegerField()
    def __str__(self) -> str:
        return self.emp_name