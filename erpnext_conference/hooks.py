# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_conference"
app_title = "ERPNext Conference"
app_publisher = "Frappe Technologies"
app_description = "Website and Ticketing platform for ERPNext Conference"
app_icon = "octicon octicon-organization"
app_color = "blue"
app_email = "developers@frappe.io"
app_license = "GPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_conference/css/erpnext_conference.css"
# app_include_js = "/assets/erpnext_conference/js/erpnext_conference.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_conference/css/erpnext_conference.css"
# web_include_js = "/assets/erpnext_conference/js/erpnext_conference.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_conference.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_conference.install.before_install"
# after_install = "erpnext_conference.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_conference.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_conference.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_conference.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_conference.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_conference.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_conference.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_conference.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_conference.event.get_events"
# }

