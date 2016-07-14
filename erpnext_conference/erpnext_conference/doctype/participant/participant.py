# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

class Participant(Document):
	def validate(self):
		self.total_cost = 0
		for ticket in self.tickets:
			self.total_cost += ticket.cost * ticket.quantity
