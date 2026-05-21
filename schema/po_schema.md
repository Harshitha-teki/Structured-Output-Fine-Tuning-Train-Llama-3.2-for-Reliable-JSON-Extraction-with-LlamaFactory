# Purchase Order (PO) JSON Schema

This document defines the JSON schema used for purchase orders (POs). Every PO example must follow this schema exactly.

Required keys (all must be present; when absent in source, use null as specified):

- buyer (string): The organisation or person placing the order. Example: "Acme Corp". If unknown, set to null.
- supplier (string): The organisation supplying the goods/services. If unknown, set to null.
- po_number (string): The purchase order number as printed on the document. If missing, set to null.
- date (string, YYYY-MM-DD): PO creation date in ISO format. If unparseable, set to null.
- delivery_date (string, YYYY-MM-DD or null): Expected delivery date. If absent, set to null.
- currency (string, 3-letter ISO code): Currency used for prices and totals. If absent or unclear, set to null.
- total (float): The PO total amount as a JSON number. If not indicated, set to null.
- items (array of objects): Each item object MUST contain exactly: item_name (string), quantity (integer), unit_price (float). If no itemization is present, use an empty array [].

Item object fields:

- item_name (string): Description or catalogue name of the item. If missing, use an empty string "".
- quantity (integer): Quantity ordered. If not specified, default to 1.
- unit_price (float): Price per unit as a JSON number. If unavailable, set to null.

Absent field conventions:

- Use JSON null for numeric/date/currency fields that are missing, to preserve type expectations.
- Use an empty string for missing purely textual sub-fields like item_name or line item description.
- Every example must include all required keys; do not omit keys from the JSON object.
