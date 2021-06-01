from django.db import models
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    name=models.fields.CharField('名字',max_length=50)
    email=models.EmailField('邮箱') # 为何这里 charfield 不是models的方法却可以直接调用，调用过程是怎么样的
    url=models.URLField('网址',blank=True)
    text=models.TextField('内容')
    created_time=models.DateTimeField('创建时间',default=timezone.now)
    post=models.ForeignKey('blog.Post',verbose_name='文章',on_delete=models.CASCADE)

    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name,self.text[:20])

    #创建了数据模型,就要迁移数据库，迁移数据库的命令也要记得写