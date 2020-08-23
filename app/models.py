from django.db import models


def user_directory_path(instance, filename):
    if instance.custom_dir_name:
        # file will be uploaded to MEDIA_ROOT/<custom_dir_name>/<filename>
        return f"{instance.custom_dir_name}/{filename}"
    else:
        # file will be uploaded to MEDIA_ROOT/book_<id>/<filename>
        return f"book_{instance.id}/{filename}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    custom_dir_name = models.CharField(max_length=50, blank=True, null=True)
    file = models.FileField(upload_to=user_directory_path, blank=True, null=True)
