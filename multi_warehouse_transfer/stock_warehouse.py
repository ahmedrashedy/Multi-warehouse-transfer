# Arabic translation for multi_branch_transfer
# Copyright 2026 Ahmed Rashedy
msgid ""
msgstr ""
"Project-Id-Version: multi_branch_transfer 19.0.1.0.0\n"
"Report-Msgid-Bugs-To: ahmedrashedy001@gmail.com\n"
"POT-Creation-Date: 2026-07-13 12:00+0000\n"
"PO-Revision-Date: 2026-07-13 12:00+0000\n"
"Last-Translator: Ahmed Rashedy <ahmedrashedy001@gmail.com>\n"
"Language: ar\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=6; plural=n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%3>=0 "
"&& n%3<=10 ? 3 : n%3>=11 && n%3<=99 ? 4 : 5;\n"

#. module: multi_branch_transfer
#: model:ir.model,name:multi_branch_transfer.model_mbt_request
msgid "Multi-Branch Transfer Request"
msgstr "طلب تحويل بين الفروع"

#. module: multi_branch_transfer
#: model:ir.model,name:multi_branch_transfer.model_mbt_request_line
msgid "Multi-Branch Transfer Request Line"
msgstr "سطر طلب تحويل بين الفروع"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__name
msgid "Reference"
msgstr "المرجع"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__dest_warehouse_id
msgid "Destination Branch"
msgstr "الفرع المستهدف"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__line_ids
msgid "Products"
msgstr "المنتجات"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__state
msgid "Status"
msgstr "الحالة"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__scheduled_date
msgid "Scheduled Date"
msgstr "التاريخ المجدول"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__notes
msgid "Notes"
msgstr "ملاحظات"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__company_id
msgid "Company"
msgstr "الشركة"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__user_id
msgid "Requester"
msgstr "مقدّم الطلب"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__first_picking_id
msgid "First Transfer (Main → Transit)"
msgstr "التحويل الأول (الرئيسي ← ترانزيت)"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request__second_picking_id
msgid "Second Transfer (Transit → Branch)"
msgstr "التحويل الثاني (ترانزيت ← الفرع)"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request_line__product_id
msgid "Product"
msgstr "المنتج"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request_line__product_uom_qty
msgid "Quantity"
msgstr "الكمية"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_mbt_request_line__product_uom_id
msgid "UoM"
msgstr "وحدة القياس"

#. module: multi_branch_transfer
#: model:ir.actions.act_window,name:multi_branch_transfer.action_mbt_request
#: model:ir.ui.menu,name:multi_branch_transfer.menu_mbt_request
msgid "Multi-Branch Transfers"
msgstr "تحويلات الفروع"

#. module: multi_branch_transfer
#: model:ir.ui.menu,name:multi_branch_transfer.menu_mbt_root
msgid "Multi-Branch Transfers (Operations)"
msgstr "تحويلات الفروع (العمليات)"

#. module: multi_branch_transfer
#: model:ir.module.category,name:multi_branch_transfer.category_mbt
msgid "Multi-Branch Transfer"
msgstr "تحويل بين الفروع"

#. module: multi_branch_transfer
#: model:res.groups,name:multi_branch_transfer.group_mbt_user
msgid "Multi-Branch Transfer / User"
msgstr "مستخدم تحويلات الفروع"

#. module: multi_branch_transfer
#: model:res.groups,name:multi_branch_transfer.group_mbt_manager
msgid "Multi-Branch Transfer / Manager"
msgstr "مدير تحويلات الفروع"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_stock_warehouse__x_is_main_source
msgid "Is Main Source"
msgstr "مخزن رئيسي (مصدر)"

#. module: multi_branch_transfer
#: model:ir.model.fields,field_description:multi_branch_transfer.field_stock_warehouse__x_is_transit
msgid "Is Transit"
msgstr "مخزن ترانزيت"

#. module: multi_branch_transfer
#: model_terms:ir.ui.view,arch_db:multi_branch_transfer.view_mbt_request_form
msgid "Confirm"
msgstr "تأكيد"

#. module: multi_branch_transfer
#: model_terms:ir.ui.view,arch_db:multi_branch_transfer.view_mbt_request_form
msgid "Cancel"
msgstr "إلغاء"

#. module: multi_branch_transfer
#: model_terms:ir.ui.view,arch_db:multi_branch_transfer.view_mbt_request_form
msgid "Reset to Draft"
msgstr "إعادة للمسودة"

#. module: multi_branch_transfer
#: selection:mbt.request,state:draft
msgid "New"
msgstr "جديد"

#. module: multi_branch_transfer
#: selection:mbt.request,state:in_progress
msgid "In Progress"
msgstr "قيد التنفيذ"

#. module: multi_branch_transfer
#: selection:mbt.request,state:first_done
msgid "Main → Transit Done"
msgstr "تم التحويل من الرئيسي إلى الترانزيت"

#. module: multi_branch_transfer
#: selection:mbt.request,state:second_done
msgid "Transit → Branch Done"
msgstr "تم التحويل من الترانزيت إلى الفرع"

#. module: multi_branch_transfer
#: selection:mbt.request,state:done
msgid "Completed"
msgstr "مكتمل"

#. module: multi_branch_transfer
#: selection:mbt.request,state:cancelled
msgid "Cancelled"
msgstr "ملغى"
