# Copyright (c) 2024, fathymossad@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class Student(Document):
    def before_naming(self):
            frappe.msgprint("Document not saved to database. Full Name is not set.")
    def autoname(self):
            self.full_name = f"{self.name1} {len(self.name1)}"
    def validate(self):
        if not self.full_name:
            frappe.throw(_("Full Name must be set."))
    def before_save(self):
        if self.name1 and self.last_name:
            self.full_name = f"{self.name1} {self.last_name}"
            


