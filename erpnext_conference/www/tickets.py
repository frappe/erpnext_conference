# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from erpnext_conference.api import get_tickets

def get_context(context):
	context.tickets = get_tickets()