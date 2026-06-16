import pdfminer.high_level
import io


class PDFExtractor:
    def extract_text(self, pdf_path: str) -> list[str]:
        with open(pdf_path, "rb") as f:
            text = pdfminer.high_level.extract_text(f)
        return [p.strip() for p in text.split("\n\n") if p.strip()]