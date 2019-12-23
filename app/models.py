import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Questions(models.Model):

    """
    问题模型，
    每个类都是django.db.models.Model的子类
    每个字段都是Field类的实例
    每个Field实例的名字就是字段名字，数据库会把这个值作为表的列名
    可以在每个Field中使用一个可选的第一位置参数用于提供一个人类可读的字段名
    将作为文档的一部分
    """

    def __str__(self):
        return self.question_text

    question_text = models.CharField("问题名称", max_length=200)
    pub_data = models.DateTimeField("发布日期")

    def was_published_recently(self):
        """
        判断问卷是否最近时间发布
        :return: 如果是返回True，如果不是返回False
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now


class Choice(models.Model):

    """
    选项模型
    使用ForeignKey定义了一个外键关系。它告诉Django，每个Choice关联到
    一个对应Question，注意：将外键写在“多”的一方，
    Django支持通用的数据关系：一对一，一对多，多对多
   """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
