import fpdf
class PDFGenerator:
    def __init__(self, output_path: str):
        self.output_path = output_path
        self.pdf = fpdf.FPDF()
        self.pdf.add_page()
        self.pdf.set_font('Arial', size=12)
        
    def add_text(self, text: str):
        """
        Add translated text to the PDF.
        
        Args:
            text (str): Translated text to add to the PDF
        """
        # Split text into lines that fit the page width
        lines = self._split_text_to_lines(text)
        for line in lines:
            self.pdf.cell(0, 10, txt=line, ln=True)
            
    def _split_text_to_lines(self, text: str, max_line_length: int = 80) -> list:
        """
        Split text into lines of appropriate length for the PDF.
        
        Args:
            text (str): Text to split
            max_line_length (int): Maximum characters per line
            
        Returns:
            list: List of lines
        """
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + word) <= max_line_length:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "
                
        if current_line:
            lines.append(current_line.strip())
            
        return lines
        
    def save(self):
        """
        Save the generated PDF to file.
        """
        self.pdf.output(self.output_path)