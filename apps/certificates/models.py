from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
class Cerficates(models.Model):
    """
    证书
    """
    #user = models.ForeignKey(User, verbose_name=u"用户",related_name="cuser")
    name = models.CharField(default="", unique=True, max_length=30, verbose_name="证书名称", help_text="证书名称")
    #code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="证书描述", help_text="证书描述")
    score = models.IntegerField(default= 1 ,verbose_name="证书得分", help_text="证书得分")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "证书"
        verbose_name_plural = verbose_name
        unique_together = ("name", "score")

    def __str__(self):
        return "name:"+self.name+" "+"score:"+str(self.score)

class IndexUserCertificate(models.Model):
    user = models.ForeignKey(User, related_name='user_certificate',verbose_name="用户-证书")
    certificate =models.ForeignKey(Cerficates, related_name='certificate_user',verbose_name="证书-用户")
    image = models.ImageField(upload_to="certificates/images/", null=True, blank=True, verbose_name="证书图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")
    class Meta:
        verbose_name = '用户-证书'
        verbose_name_plural = verbose_name
        #unique_together = ("user", "depart")
    def get_total_score(self):
        return self.certificate.score
    def __str__(self):
        return self.certificate.name

