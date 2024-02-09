from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class EnAboutCollege(models.Model):
    txt=models.TextField('Homepage: About the College')
    address=models.CharField('Address',max_length=100)


    def __str__(self) -> str:
        return self.address
    
    class Meta:
        verbose_name='General data'
        verbose_name_plural='General data'

class EnProfessions(models.Model):
    name=models.CharField('Name of specialty',max_length=100)
    img=models.ImageField('Imagers',upload_to='Professions imagers')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Professions'
        verbose_name_plural='Professions'

class EnProfDetail(models.Model):
    name=models.ForeignKey(EnProfessions,on_delete=models.CASCADE,related_name='enprofdetail')
    info=models.TextField('Section information')

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name='detailed information'
        verbose_name_plural='detailed information'  

class EnStaffs(models.Model):
    name=models.CharField('Name Surname',max_length=50)
    prof=models.CharField('The position held',max_length=50)
    img=models.ImageField('Imagers',upload_to='Staffs')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Stuff'
        verbose_name_plural='Stuff'    



class EnQuestions(models.Model):
    question=models.CharField('question',max_length=255)
    answer=models.TextField('answer')

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        verbose_name='question and answer'
        verbose_name_plural='question and answer'


class EnContactUs(models.Model):
    address=models.CharField('Address',max_length=100)
    phone=PhoneNumberField('phone number (+374)')
    email=models.EmailField('Email')
    facebook=models.URLField('Facebook',blank=True)
    linkedin=models.URLField('LinkedIn',blank=True)
    instagram=models.URLField('Instagram',blank=True)


    def __str__(self) -> str:
        return self.address
    
    class Meta:
        verbose_name='contacts'
        verbose_name_plural='contacts'

class EnDimord(models.Model):
    title=models.CharField('Title',max_length=255)
    subtitle=models.CharField('Distinguished line at the beginning of the text ',max_length=500)
    text=models.TextField('The rest of the text')
    img=models.ImageField('imgers',upload_to='dimord',null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='applicant'
        verbose_name_plural='applicant'