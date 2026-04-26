from app.config import settings

class SupplierClient:
    def create_order(self, order):
        # Replace with your approved supplier API.
        # Supplier must ship with your business as seller of record,
        # no supplier branding, and compliant packing slips/invoices.
        if not settings.supplier_api_base_url or not settings.supplier_api_key:
            return {
                "ok": False,
                "message": "Supplier API not configured."
            }

        return {
            "ok": False,
            "message": "Supplier order stub. Add your supplier endpoint here."
        }

    def get_tracking(self, supplier_order_id):
        return None
