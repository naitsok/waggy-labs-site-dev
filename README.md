# Waggy Labs Site development repo

This is the developmnet repo for the brand new version of old deprecated Scientific Wagtail site. It is currently being upgraded to the latest versions of the Django and Wagtail. I've also been thinking about changing somewhat the concept and rebranding of this website engine. Looking through websites of different research groups over the last few years, I developed a strong sense that principle invesitgators (PIs) tend to create websites for their groups independent of the webpages provided by universities. The idea for the update is to turn it from a personal blog to an easyly runnable website for a research group.

Therefore, eventually this repo will be divided into a PyPi package and standalone Waggy Labs website: 

- Waggy Labs website will have immediately avalable for an easy setup form a Docker container on one from a numerous number of VPS (or a university server).
- PyPi Django app to be used with either new or existing Django application.

And the breif list of features (not full!) is:

- Full list of the latest Wagtail CMS features.
- Basic customization with an uploadable CSS for Bootstrap to get a personal flavor for the website.
- Almost infinite customization by replacing templates with your own ones and adding your own features with Python. It will require building your own Django website, adding the app and replacing templates using Django templates engine.
- Easy creation of website pages and website menu.
- Writing posts and post threads in a scientific article format (for example such as on ACS website).
- Upgraded writing tools needed for scientific writing, such as writing equation using LaTeX format, referencing figure using markdown syntax, etc.

