# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import json

import frappe


@frappe.whitelist()
def update_task(args: str, field_map: str):
	"""Updates Doc (called via gantt) based on passed `field_map`"""
	args = frappe._dict(json.loads(args))
	field_map = frappe._dict(json.loads(field_map))
	d = frappe.get_doc(args.doctype, args.name)
	for field_name in (field_map.start, field_map.end):
		field = d.meta.get_field(field_name)
		if not field or field.fieldtype not in ("Date", "Datetime"):
			frappe.throw(frappe._("Invalid Gantt date field: {0}").format(field_name))
	d.set(field_map.start, args.start)
	d.set(field_map.end, args.end)
	d.save()
