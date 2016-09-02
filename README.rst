Ella CMS
########

Ella is opensource CMS based on Django framework, designed for flexibility.

It is composed from several modules:

* **Ella core** is the main module which links the rest together. It
  defines architecture on which other modules are built but doesn't do
  anything really usefull all alone.
* **Ella core plugins** are plugins that are shipped in one package
  together with Ella. There are **articles** and **positions** which 
  we consider to be a basic toolbox for each Ella site.
* **Other Ella plugins** are standalone applications (and therfore
  not shipped with the core) that provide some
  specific functionality using **Ella's architecture**. We can mention
  polls, galleries, quizes and many more.
      
**Feature highlights**:

* Simple organization of content based on categories
* Efficent implementation of the published content
* In-build photo formating backend
* Django-admin ready
* Plugin system
* Flexibile
* Scalable
* Extensible
* Caching-friendly
* Well tested
* Proven in production environment

Django > 1.8
************

For use with django > 1.8 add few ella templatetags dependencies to builtins TEMPLATES setting, see example below ::

	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                'django.template.context_processors.debug',
	                'django.template.context_processors.request',
	                'django.contrib.auth.context_processors.auth',
	                'django.contrib.messages.context_processors.messages',
	            ],
	            'builtins': [
	                'ella.core.templatetags.core',
	                'ella.core.templatetags.related',
	                'ella.core.templatetags.custom_urls_tags',
	                'django.templatetags.i18n',
	                'ella.photos.templatetags.photos',
	            ],
	        },
	    },
	]

Django < 1.7
************

For use with django < 1.7 use south >= 1.0.0 or 
set SOUTH_MIGRATION_MODULES setting for ella modules 
to south_migrations directory (south >= 1.0.0 looks to south_migrations directory by default).

If you need migrate your project from ella 2.x to ella 3.x use django < 1.7 and south, 
then migrate your project and then you can upgrade to django 1.7 or higher.
    
News
****

Currently, we released the **3.x version** which features a **major cleanup** 
of the code a **removal of unneeded dependencies**.

More news are on the way as we are going to make a nicely-tailored admin 
specifically made for the need of news writers and editors. 
    
Docs
****

Docs are hosted on readthedocs.org, go to http://ella.rtfd.org.

Community
*********

* We stick with github to manage the issues, see https://github.com/ella/ella/issues.
* mailing list can be found at ella-project@googlegroups.com
* IRC channel #ellacms on freenode.net

Quickstart
**********

Have a look at the docs: http://readthedocs.org/docs/ella/en/latest/quickstart.html.

Build status
************

:Master branch:

  .. image:: https://travis-ci.org/MichalMaM/ella.svg?branch=master
     :alt: Travis CI - Distributed build platform for the open source community
     :target: https://travis-ci.org/MichalMaM/ella
