from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    blog_category = models.ForeignKey(BlogCategory, verbose_name='Category name', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Post name')
    content = models.TextField()
    image = models.ImageField(upload_to='blog_posts/')
    published = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    in_archive = models.NullBooleanField(default=False)

    def __str__(self):
        return f"{self.title} from \"{self.blog_category.name}\" category"
