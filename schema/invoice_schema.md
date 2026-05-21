# Invoice JSON Schema

This document defines the exact JSON schema used for invoices in this project. Every training and evaluation example MUST conform exactly to these key names, data types, and absent-field conventions.

Required keys (all must be present; absent values must be null where stated):

- vendor (string): The legal or trade name of the invoice issuer. Example: "Tata Steel". If the vendor cannot be determined from the document, set to null.
- invoice_number (string): The invoice identifier as written on the document (may include letters and dashes). If missing, set to null.
- date (string, YYYY-MM-DD): The invoice issue date in ISO format. If only a month/year is present or it cannot be parsed, set to null.
- due_date (string, YYYY-MM-DD or null): The payment due date. If absent, set to null.
- currency (string, 3-letter ISO code): Currency of values (e.g., "USD", "EUR", "INR"). If currency is ambiguous or not shown, set to null.
- subtotal (float): Sum of line item (quantity * unit_price) before tax. Must be a JSON number (e.g., 142500.0). If not calculable, set to null.
- tax (float or null): Tax amount applied to the invoice. If the invoice shows no tax line, set to null.
- total (float): Final total payable. Must be a JSON number. If the total is not present or ambiguous, set to null.
- line_items (array of objects): Each line item object MUST contain exactly: description (string), quantity (integer), unit_price (float). If the document has no line items (e.g., a single lump sum), provide an empty array [].

Line item object fields:

- description (string): Short human-readable description of the item or service. If missing, use an empty string "".
- quantity (integer): Quantity as an integer. If the document shows a decimal quantity, round to nearest integer and record that value. If absent, set to 1.
- unit_price (float): Price per unit as a JSON number. If only a total is provided and not a unit price, set to null.

Notes on absent fields and consistency:

- Use null (JSON null) for missing numerical or date fields (due_date, tax, subtotal, total) to make downstream type checks reliable.
- Use empty string "" only for purely textual sub-fields where an empty textual placeholder is preferable (line item description). Do not use "" for numeric/date fields.
- Every example must include all keys listed above (no missing keys), with the specified types or null/placeholders as described.
