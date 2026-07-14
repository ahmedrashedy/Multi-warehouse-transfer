Multi-Branch Transfer (Transit-Aware)
====================================

Chain internal transfers across two hops with a single click:

    Source → Transit → Destination

Designed for businesses with a central warehouse that supplies multiple
branch warehouses via a transit/buffer location. Creates both internal
transfers, reserves stock and validates them automatically, with a
cron-based safety net for late-arriving stock.

Usage
-----

1. *Inventory → Configuration → Warehouses* — tick **Is Main Source** on
   your central warehouse and **Is Transit** on the buffer warehouse.
2. *Inventory → Operations → Multi-Branch Transfers → Transfers* — click
   **New**, choose Source / Transit / Destination warehouses, add product
   lines.
3. Click **Confirm**. Both transfers are created and processed.
4. Use **Cancel** or **Reset to Draft** to handle exceptions.

See ``static/description/index.html`` for a full illustrated guide.

Technical notes
---------------

* Odoo 19.0 (Community / Enterprise).
* Depends on ``stock``, ``mail``, ``product``.
* Adds two boolean flags (``x_is_main_source``, ``x_is_transit``) to
  ``stock.warehouse``.
* Adds two groups (User / Manager) under *Multi-Branch Transfer* in
  *Settings → Users & Companies → Groups*.
* Cron ``Multi-Branch Transfer: reprocess pending`` runs every 15 minutes.

Author
------

Ahmed Rashedy

* Email: ahmedrashedy001@gmail.com
* Phone: +20 112 207 9077
