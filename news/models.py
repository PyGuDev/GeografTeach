from django.db import models
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(PostManager, self).get_queryset().filter(avilable=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

class NewsPost(models.Model):
    categorys = models.ForeignKey('Category', on_delete=models.CASCADE,  blank=True, null=True,)
    title = models.CharField(max_length=30, db_index=True)
    urlyoutube = models.CharField(max_length=255, blank=True)
    img = models.ImageField(upload_to="media/upload", blank=True)
    text = RichTextUploadingField(blank=True)
    textcut = RichTextUploadingField(blank=True)
    pub_date = models.DateField(auto_now=True)
    avilable = models.BooleanField(default=True)
    objects = PostManager()
    visite_count = models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

