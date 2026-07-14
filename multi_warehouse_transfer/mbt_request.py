<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data noupdate="1">
        <record id="seq_mbt_request" model="ir.sequence">
            <field name="name">Multi-Branch Transfer Request</field>
            <field name="code">mbt.request</field>
            <field name="prefix">MBT/%(year)s/</field>
            <field name="padding">5</field>
            <field name="company_id" eval="False"/>
            <field name="use_date_range" eval="True"/>
        </record>
    </data>
</odoo>