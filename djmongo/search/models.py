from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import Group
import json
from django.utils.encoding import python_2_unicode_compatible

OUTPUT_CHOICES = (("json","JSON"),
                  ("html", "HTML"),
                  ("csv","Comma Seperated Value (.csv)"),
                  )

@python_2_unicode_compatible
class SavedSearch(models.Model):

    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    group           = models.ForeignKey(Group, blank=True, null=True)
    output_format   = models.CharField(max_length=4, choices=OUTPUT_CHOICES,
                                        default="json")
    slug            = models.SlugField(max_length=100, unique=True)
    query           = models.TextField(max_length=2048, default="{}",            
                                        verbose_name="JSON Query")
    type_mapper     = models.TextField(max_length=2048, default="{}",            
                                        verbose_name="Map non-string variables to numbers or boolean")
    is_public       = models.BooleanField(default=False, blank=True,
                            help_text = "If checked, the search can be run without authentication")
    
    sort            = models.TextField(max_length=2048, default="", blank=True,
                                        verbose_name="Sort Dict",
                                        help_text="""e.g. [["somefield", 1], ["someotherfield", -1] ]""")
    
    return_keys     = models.TextField(max_length=2048, default="", blank=True,
                                      
                            help_text = """Default is blank which returns all keys.
                            Seperate keys by whitespace to limit the keys that are returned."""
                                        )
    
    default_limit   = models.IntegerField(default=getattr(settings, 'MONGO_LIMIT', 200),
                            help_text = "Limit results to this number unless specified otherwise.",
                                        )
    database_name   = models.CharField(max_length=100)
    collection_name = models.CharField(max_length=100)
    creation_date   = models.DateField(auto_now_add=True)
    
    class Meta:
        get_latest_by = "creation_date"
        ordering = ('-creation_date',)
        verbose_name_plural = "Saved Searches"

    def __str__(self):
        return "%s" % (self.slug)
        
        
@python_2_unicode_compatible        
class DatabaseAccessControl(models.Model):

    database_name   = models.CharField(max_length=256)
    collection_name = models.CharField(max_length=256)
    is_public       = models.BooleanField(default=False, blank=True)
    search_keys     =  models.TextField(max_length=4096, default="", blank=True,              
                        help_text = """The default, blank, returns all keys.
                                        Providing a list of keys, seperated by whitespace,
                                        limits the API search to only these keys.""")
    groups          = models.ManyToManyField(Group,  blank=True,
                                related_name = "djmongo_database_access_control")
    
    class Meta:
        #get_latest_by = "creation_date"
        #ordering = ('-creation_date',)
        verbose_name_plural = "Database Access Controls"
        unique_together =  (('database_name', 'collection_name'), )

    def __str__(self):
        return "%s/%s" % (self.database_name, self.collection_name )
        

