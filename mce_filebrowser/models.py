import datetime

from django.db import models
from django.utils.translation import ugettext as _

from mce_filebrowser.conf import   LOCAL_MCE_FILEBROWSER_UPLOADDIR,LOCAL_MCE_FILEBROWSER_PERUSER

def content_file_name(instance, filename):
    if LOCAL_MCE_FILEBROWSER_PERUSER == True:
        return "%s/%s/%s/%s" %(LOCAL_MCE_FILEBROWSER_UPLOADDIR,'user-%s' % str(instance.user_id), datetime.datetime.now().strftime("%Y/%m/%d"), filename)
    else:
        return "%s/%s/%s" %(LOCAL_MCE_FILEBROWSER_UPLOADDIR, datetime.datetime.now().strftime("%Y/%m/%d"), filename)



class FileBrowserFile(models.Model):
    """ Uploaded file model """
    FILE_TYPES = (
        ('img', _('Image')),
        ('doc', _('Document')),
    )
    
    file_type = models.CharField(max_length=3, choices=FILE_TYPES)
    uploaded_file = models.FileField(
        upload_to=content_file_name,
        verbose_name = _('File / Image'),
        max_length=300,
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Create date')
    )

    user_id = models.IntegerField(null=True, blank=True, verbose_name=_('Who does this file belong to?'))

    def __unicode__(self):
        return u'%s' % self.uploaded_file.name
