# -*- coding: utf-8 -*-
from django.db import models


class Archives(models.Model):
    artid = models.IntegerField()
    itemname = models.CharField(max_length=765, db_column='itemName')  # Field name made lowercase.
    address = models.CharField(max_length=765, db_column='Address', blank=True)  # Field name made lowercase.
    phone = models.CharField(max_length=765, db_column='Phone', blank=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'archives'


class Archivescategory(models.Model):
    collectorcode = models.CharField(max_length=150, db_column='collectorCode', blank=True)  # Field name made lowercase.
    educator = models.CharField(max_length=765, blank=True)
    linkactive = models.CharField(max_length=765, blank=True)
    nameenglish = models.CharField(max_length=765, db_column='nameEnglish', blank=True)  # Field name made lowercase.
    catcode = models.IntegerField(primary_key=True)
    namehebrew = models.CharField(max_length=765, db_column='nameHebrew')  # Field name made lowercase.
    description = models.CharField(max_length=765, blank=True)
    exprtcode = models.CharField(max_length=150, blank=True)
    birthcountry = models.CharField(max_length=150, db_column='birthCountry', blank=True)  # Field name made lowercase.
    deathyear = models.CharField(max_length=150, db_column='deathYear', blank=True)  # Field name made lowercase.
    birthyear = models.CharField(max_length=150, db_column='birthYear', blank=True)  # Field name made lowercase.
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'archivescategory'


class Articles(models.Model):
    artid = models.IntegerField()
    itemname = models.CharField(max_length=765, db_column='itemName')  # Field name made lowercase.
    author = models.CharField(max_length=765, blank=True)
    subject = models.CharField(max_length=765, blank=True)
    filenames1 = models.CharField(max_length=765, blank=True)
    filenames = models.CharField(max_length=765, blank=True)
    year = models.CharField(max_length=150, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)
    source = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = u'articles'


class Articlescategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'articlescategory'


class Biblio(models.Model):
    artid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=765, db_column='itemName')  # Field name made lowercase.
    author = models.CharField(max_length=765, blank=True)
    publisher = models.CharField(max_length=765, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'biblio'


class Bibliocategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'bibliocategory'


class Categories(models.Model):
    artid = models.IntegerField(primary_key=True)
    namehebrew = models.CharField(max_length=765, db_column='nameHebrew')  # Field name made lowercase.
    nameenglish = models.CharField(max_length=765, db_column='nameEnglish', blank=True)  # Field name made lowercase.
    linkname = models.CharField(max_length=765, blank=True)
    linkactive = models.CharField(max_length=150, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.ForeignKey('Categoriescategory')
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'categories'


class Categoriescategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    namehebrew = models.CharField(max_length=765, db_column='nameHebrew', blank=True)  # Field name made lowercase.
    nameenglish = models.CharField(max_length=765, db_column='nameEnglish')  # Field name made lowercase.
    description = models.CharField(max_length=765, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'categoriescategory'


class Designers(models.Model):
    artid = models.IntegerField(primary_key=True)
    namehebrew = models.CharField(max_length=765, db_column='nameHebrew')  # Field name made lowercase.
    nameenglish = models.CharField(max_length=765, db_column='nameEnglish', blank=True)  # Field name made lowercase.
    designercode = models.CharField(max_length=150, db_column='designerCode', blank=True)  # Field name made lowercase.
    # exprtcode     = models.CharField(max_length=765, blank=True)
    birthyear = models.CharField(max_length=30, db_column='birthYear', blank=True)  # Field name made lowercase.
    deathyear = models.CharField(max_length=30, db_column='deathYear', blank=True)  # Field name made lowercase.
    birthcountry = models.CharField(max_length=75, db_column='birthCountry', blank=True)  # Field name made lowercase.
    linkactive = models.CharField(max_length=9, blank=True)
    # educator      = models.CharField(max_length=9, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    commentsbrief = models.TextField(db_column='CommentsBrief', blank=True)  # Field name made lowercase.
    # added         = models.DateTimeField()
    # addedby       = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = u'designers'


class Designerscategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)

    class Meta:
        managed = False
        db_table = u'designerscategory'


class Events(models.Model):
    artid = models.IntegerField(primary_key=True)
    subtitle1 = models.CharField(max_length=765, db_column='subTitle1')  # Field name made lowercase.
    subcontents1 = models.TextField(blank=True)
    subtitle2 = models.CharField(max_length=765, db_column='subTitle2', blank=True)  # Field name made lowercase.
    subcontents2 = models.TextField(blank=True)
    subtitle3 = models.CharField(max_length=765, db_column='subTitle3', blank=True)  # Field name made lowercase.
    subcontents3 = models.TextField(blank=True)
    subtitle4 = models.CharField(max_length=765, db_column='subTitle4', blank=True)  # Field name made lowercase.
    subcontents4 = models.TextField(blank=True)
    eventcontents = models.TextField(db_column='eventContents', blank=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'events'


class Links(models.Model):
    artid = models.IntegerField()
    itemname = models.CharField(max_length=765, db_column='itemName')  # Field name made lowercase.
    itemurl = models.CharField(max_length=765, blank=True)
    sitelanguage = models.CharField(max_length=765, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'links'


class Linkscategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'linkscategory'


class Movies(models.Model):
    artid = models.IntegerField()
    itemname = models.CharField(max_length=765, db_column='itemName')  # Field name made lowercase.
    description = models.CharField(max_length=765, blank=True)
    filenames = models.CharField(max_length=765, blank=True)
    movielength = models.CharField(max_length=150, db_column='movieLength', blank=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'movies'


class Moviescategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'moviescategory'


class Pages(models.Model):
    artid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=765, db_column='itemName')  # Field name made lowercase.
    pagelink = models.CharField(max_length=765, blank=True)
    pagetitle = models.CharField(max_length=150, db_column='pageTitle', blank=True)  # Field name made lowercase.
    pagecontents = models.TextField(db_column='pageContents', blank=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'pages'


class SidarItems(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    client = models.CharField(max_length=765, db_column='Client', blank=True)  # Field name made lowercase.
    # copyright          = models.CharField(max_length=765, db_column='Copyright', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=765, db_column='Country', blank=True)  # Field name made lowercase.
    date = models.CharField(max_length=765, db_column='Date', blank=True)  # Field name made lowercase.
    # department         = models.CharField(max_length=765, db_column='Department', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True)  # Field name made lowercase.
    # description_writer = models.CharField(max_length=765, db_column='Description Writer', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    designer = models.CharField(max_length=765, db_column='Designer', blank=True)  # Field name made lowercase.
    designercode = models.CharField(max_length=150, db_column='DesignerCode', blank=True)  # Field name made lowercase.
    # directory_path     = models.CharField(max_length=765, db_column='Directory Path', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    document_title = models.CharField(max_length=765, db_column='Document Title', blank=True)  # Field renamed to remove spaces. Field name made lowercase.
    # extension          = models.CharField(max_length=765, db_column='Extension', blank=True) # Field name made lowercase.
    # fieldname          = models.CharField(max_length=765, db_column='FieldName', blank=True) # Field name made lowercase.
    # file_type_mac      = models.CharField(max_length=765, db_column='File Type Mac', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    filename = models.CharField(max_length=765, db_column='Filename', blank=True)  # Field name made lowercase.
    # item               = models.CharField(max_length=765, db_column='Item', blank=True) # Field name made lowercase.
    # keywords           = models.CharField(max_length=765, db_column='Keywords', blank=True) # Field name made lowercase.
    # number_of_pages    = models.CharField(max_length=765, db_column='Number of Pages', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    path = models.CharField(max_length=765, db_column='Path', blank=True)  # Field name made lowercase.
    # illustration_by    = models.CharField(max_length=765, db_column='Photo/Illustration by', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    size = models.CharField(max_length=765, db_column='Size', blank=True)  # Field name made lowercase.
    technique = models.CharField(max_length=765, db_column='Technique', blank=True)  # Field name made lowercase.
    topic = models.CharField(max_length=765, db_column='Topic', blank=True)  # Field name made lowercase.
    # watermark_url      = models.CharField(max_length=765, db_column='Watermark URL', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    # watermarked        = models.CharField(max_length=765, db_column='Watermarked', blank=True) # Field name made lowercase.
    # website            = models.CharField(max_length=765, db_column='Website', blank=True) # Field name made lowercase.
    country_he = models.CharField(max_length=765, blank=True)
    size_he = models.CharField(max_length=765, blank=True)
    # זכויות_יוצרים         = models.CharField(max_length=765, db_column='\xd7\x96\xd7\x9b\xd7\x95\xd7\x99\xd7\x95\xd7\xaa \xd7\x99\xd7\x95\xd7\xa6\xd7\xa8\xd7\x99\xd7\x9d', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    technique_he = models.CharField(max_length=765, blank=True)
    client_he = models.CharField(max_length=765, blank=True)
    collection_he = models.CharField(max_length=765, blank=True)
    # מילות_מפתח         = models.CharField(max_length=765, db_column='\xd7\x9e\xd7\x99\xd7\x9c\xd7\x95\xd7\xaa \xd7\x9e\xd7\xa4\xd7\xaa\xd7\x97', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    designer_he = models.CharField(max_length=765, blank=True)
    subject_he = models.CharField(max_length=765, blank=True)
    # סוג_המסמך          = models.CharField(max_length=765, db_column='\xd7\xa1\xd7\x95\xd7\x92 \xd7\x94\xd7\x9e\xd7\xa1\xd7\x9e\xd7\x9a', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    # פריט               = models.CharField(max_length=765, blank=True)
    category_he = models.CharField(max_length=765, blank=True)
    title_he = models.CharField(max_length=765, blank=True)  # Field renamed to remove spaces. Field name made lowercase.
    description_he = models.TextField(blank=True)
    date = models.CharField(max_length=765, blank=True)
    # תאריך_עיברי         = models.CharField(max_length=765, db_column='\xd7\xaa\xd7\x90\xd7\xa8\xd7\x99\xd7\x9a \xd7\xa2\xd7\x99\xd7\x91\xd7\xa8\xd7\x99', blank=True) # Field renamed to remove spaces. Field name made lowercase.

    class Meta:
        managed = False
        db_table = u'sidar_items'


class Studiorelate(models.Model):
    id = models.IntegerField(primary_key=True)
    designer = models.CharField(max_length=765, blank=True)
    relates = models.CharField(max_length=765, blank=True)

    class Meta:
        managed = False
        db_table = u'studiorelate'


class Subjects(models.Model):
    artid = models.IntegerField(primary_key=True)
    namehebrew = models.CharField(max_length=765, db_column='nameHebrew')  # Field name made lowercase.
    nameenglish = models.CharField(max_length=765, db_column='nameEnglish', blank=True)  # Field name made lowercase.
    linkactive = models.CharField(max_length=150, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    catcode = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'subjects'


class Subjectscategory(models.Model):
    catcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sub = models.IntegerField(null=True, blank=True)
    bgcolor = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'subjectscategory'


class Timeline(models.Model):
    artid = models.IntegerField(primary_key=True)
    namehebrew = models.CharField(max_length=765, db_column='nameHebrew')  # Field name made lowercase.
    nameenglish = models.CharField(max_length=765, db_column='nameEnglish', blank=True)  # Field name made lowercase.
    events = models.TextField(blank=True)
    description = models.TextField(blank=True)
    designers = models.TextField(blank=True)
    designers_description = models.TextField(blank=True)
    linkactive = models.CharField(max_length=30, blank=True)
    comments = models.TextField(db_column='Comments', blank=True)  # Field name made lowercase.
    yearstart = models.IntegerField(null=True, blank=True)
    yearend = models.IntegerField(null=True, blank=True)
    timewords = models.TextField(blank=True)
    added = models.DateTimeField()
    addedby = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    extra = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = u'timeline'


class Users(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=150, blank=True)
    fname = models.CharField(max_length=150, blank=True)
    lname = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)
    privilages = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = u'users'
