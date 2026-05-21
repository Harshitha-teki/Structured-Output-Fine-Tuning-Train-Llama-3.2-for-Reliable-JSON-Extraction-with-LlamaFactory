import json
from pathlib import Path

OUT = Path(__file__).parents[1] / 'data' / 'curated_train_full.jsonl'

def make_invoice(i):
    vendor = f"Vendor_{i:03d}"
    # compute conditional values as strings to avoid putting conditionals inside format specifiers
    due_date_str = f"2024-04-{(i%28)+1:02d}" if i%3 != 0 else 'null'
    currency = 'USD' if i%5 else 'EUR'
    tax_val = None if i%4 == 0 else 10.0 * (i%5)
    subtotal = 100.0 * (i%10 + 1)
    total = subtotal + (tax_val if tax_val is not None else 0)
    tax_str = f"{tax_val:.2f}" if tax_val is not None else 'null'
    line_items = [{"description":"Item A","quantity":i%5+1,"unit_price":round(100.0*((i%5)+1),2)}]

    inv = {
        "instruction": "Extract all invoice fields and return ONLY a valid JSON object. No explanation, no markdown, no code fences.",
        "input": (
            "Invoice\n"
            f"Vendor: {vendor}\n"
            f"Invoice No: INV-{1000+i}\n"
            f"Date: 2024-03-{(i%28)+1:02d}\n"
            f"Due Date: {due_date_str}\n"
            f"Currency: {currency}\n"
            f"Subtotal: {subtotal:.2f}\n"
            f"Tax: {tax_str}\n"
            f"Total: {total:.2f}\n"
            f"Items:\n- Item A, Qty: {i%5+1}, Unit Price: {100.0 * ((i%5)+1):.2f}"
        ),
        "output": None
    }
    out = {
        "vendor": vendor,
        "invoice_number": f"INV-{1000+i}",
        "date": f"2024-03-{(i%28)+1:02d}",
        "due_date": (due_date_str if due_date_str != 'null' else None),
        "currency": currency,
        "subtotal": round(float(subtotal),2),
        "tax": round(float(tax_val),2) if tax_val is not None else None,
        "total": round(float(total),2),
        "line_items": line_items
    }
    inv["output"] = json.dumps(out)
    return inv

def make_po(i):
    buyer = f"Buyer_{i:03d}"
    supplier = f"Supplier_{i:03d}"
    delivery_date_str = f"2024-03-{(i%27)+1:02d}" if i%4 != 0 else 'null'
    currency = 'USD' if i%4 else 'JPY'
    qty = i%10+1
    unit_price = round(5.0*qty,2)
    total = round(qty * unit_price,2)
    items = [{"item_name":"Item X","quantity": qty, "unit_price": unit_price}]

    po = {
        "instruction": "Extract all purchase order fields and return ONLY a valid JSON object. No explanation, no markdown, no code fences.",
        "input": (
            "Purchase Order\n"
            f"Buyer: {buyer}\n"
            f"Supplier: {supplier}\n"
            f"PO No: PO-{2000+i}\n"
            f"Date: 2024-02-{(i%27)+1:02d}\n"
            f"Delivery Date: {delivery_date_str}\n"
            f"Currency: {currency}\n"
            f"Items:\n- Item X, Qty: {qty}, Unit Price: {unit_price:.2f}\n"
            f"Total: {total:.2f}"
        ),
        "output": None
    }
    out = {
        "buyer": buyer,
        "supplier": supplier,
        "po_number": f"PO-{2000+i}",
        "date": f"2024-02-{(i%27)+1:02d}",
        "delivery_date": (delivery_date_str if delivery_date_str != 'null' else None),
        "currency": currency,
        "total": total,
        "items": items
    }
    po["output"] = json.dumps(out)
    return po

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    # 50 invoices
    for i in range(1,51):
        lines.append(make_invoice(i))
    # 30 POs
    for i in range(1,31):
        lines.append(make_po(i))

    with open(OUT, 'w', encoding='utf-8') as f:
        for obj in lines:
            f.write(json.dumps(obj, ensure_ascii=False) + '\n')

    print(f'Wrote {len(lines)} examples to {OUT}')

if __name__ == '__main__':
    main()
