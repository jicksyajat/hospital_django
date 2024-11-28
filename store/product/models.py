from django.db import models


class DEPARTMENT(models.Model):

    id=models.BigAutoField(
        primary_key=True
    )
    dept_name=models.CharField(max_length=50)
    dept_des=models.TextField()
    def __str__(self):
        return self.dept_name
    

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    # doc_name=models.ForeignKey(Doctors,on_delete=)
    booking_date=models.DateField()
    

    def __str__(self):
        return self.p_name
    


class Doctors(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_spec = models.TextField()
    # dep_name = models. ForeignKey(DEPARTMENT,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors',default='defaults_image.jpg')


    def __str__(self):
        return 'DR'+' '+ self.doc_name +'- (' + self.doc_spec +')'
    
