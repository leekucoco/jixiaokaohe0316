from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class DepartDetail(models.Model):
    """
    机构
    """
    DEPT_TYPE = (
        (1, "机关"),
        (2, "支行"),

    )
    name = models.CharField(default="", max_length=30, verbose_name="机构", help_text="机构")
    desc = models.TextField(default="", verbose_name="机构描述", help_text="机构描述")
    dept_type = models.IntegerField(choices=DEPT_TYPE, verbose_name="组织", help_text="组织")
    parent_dept = models.ForeignKey("self", null=True, blank=True, verbose_name="上级部门", help_text="上级部门",
                                        related_name="parentdept")
    manager = models.ForeignKey(User, verbose_name="部门经理", help_text="部门经理", related_name="dept_manager")
    leader = models.ForeignKey(User, verbose_name="主管领导", help_text="主管领导", related_name="dept_leader")
    basesalary = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class IndexUserDepart(models.Model):
    user = models.ForeignKey(User, related_name='user_depart',verbose_name="用户-部门")
    depart =models.ForeignKey(DepartDetail, related_name='depart_user',verbose_name="部门-用户")

    class Meta:
        verbose_name = '用户-机构'
        verbose_name_plural = verbose_name
        unique_together = ("user", "depart")
    def __str__(self):
        return self.depart.name
