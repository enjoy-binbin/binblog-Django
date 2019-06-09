from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from blog.models import Article, Tag, Category

User = get_user_model()


class Command(BaseCommand):
    """ run manage.py create_testdata """
    admin_username = 'fake_admin'
    admin_password = 'fake_admin'
    admin_email = 'fake_admin@qq.com'
    help = 'Create some fake data for display'


    def handle(self, *args, **options):
        # get_or_create 没有便创建, 返回一个元组 (obj, created)
        user = User.objects.get_or_create(username=self.admin_username, email=self.admin_email, is_staff=True,
                                          is_superuser=True)[0]
        user.set_password(self.admin_password)
        user.save()

        parent_category = Category.objects.get_or_create(name='python学习', parent_category=None)[0]

        sub_category = Category.objects.get_or_create(name='django学习', parent_category=parent_category)[0]

        base_tag = Tag.objects.get_or_create(name='Django')[0]

        # 创建20篇测试文章
        for i in range(1, 20):
            article = Article.objects.get_or_create(
                category=sub_category,
                title='我是测试标题 ' + str(i),
                content='我是测试内容 ' + str(i),
                author=user
            )[0]
            tag = Tag.objects.get_or_create(name='标签' + str(i))[0]

            article.tags.add(tag)
            article.tags.add(base_tag)
            article.save()

        # 创建文章
        article = Article.objects.get_or_create(
            category=sub_category,
            title='彬彬博客',
            author=user,
            content=
            """
### 支持Markdown

```python
print('支持语法高亮')
```
            """,
        )[0]
        article.tags.add(base_tag)
        article.save()

        self.stdout.write('\nCreated a superuser (fake_admin fake_admin).'
                          '\nData creation succeeded.')
