# Prompt Iterations

Document the prompt engineering experiments here. Include at least three versions for each hard baseline document.

Example prompt versions (fill with the actual prompts you used):

1) Strict instruction only:
"Extract all invoice fields and return ONLY a valid JSON object matching the schema: {vendor, invoice_number, date, due_date, currency, subtotal, tax, total, line_items}. Do not add explanation, do not use markdown or code fences. Use null for missing numeric/date fields and empty string for missing text fields."

2) Few-shot example added (one example of a correctly formatted JSON output).

3) Step-by-step constraints (explicitly ban fences and prose; require keys in exact order).

Record each trial's raw response in `prompts/prompt_eval.md`.
