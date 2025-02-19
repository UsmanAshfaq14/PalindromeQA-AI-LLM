import json
import csv
import io
from typing import List, Dict, Union, Tuple
from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    error_message: str = ""
    data: List[str] = None

@dataclass
class ProductCodeAnalysis:
    original_code: str
    reversed_code: str
    is_palindrome: bool

class PalindromeQA:
    def __init__(self):
        self.analysis_results: List[ProductCodeAnalysis] = []
    
    def validate_product_code(self, code: str) -> bool:
        """Validate if a product code contains only alphanumeric characters."""
        return code.isalnum()
    
    def parse_csv_data(self, csv_data: str) -> ValidationResult:
        """Parse and validate CSV data."""
        try:
            reader = csv.DictReader(io.StringIO(csv_data))
            if 'product_code' not in reader.fieldnames:
                return ValidationResult(False, "ERROR: Missing required field 'product_code' in header.")
            
            product_codes = []
            for i, row in enumerate(reader, 1):
                if 'product_code' not in row:
                    return ValidationResult(False, f"ERROR: Missing required field 'product_code' at row {i}.")
                code = row['product_code'].strip()
                if not code:
                    return ValidationResult(False, f"ERROR: Empty product code at row {i}.")
                if not self.validate_product_code(code):
                    return ValidationResult(False, f"ERROR: Invalid characters detected in product_code at row {i}.")
                product_codes.append(code)
            
            return ValidationResult(True, data=product_codes)
        except Exception as e:
            return ValidationResult(False, f"ERROR: Invalid CSV format. {str(e)}")
    
    def parse_json_data(self, json_data: str) -> ValidationResult:
        """Parse and validate JSON data."""
        try:
            data = json.loads(json_data)
            if 'product_codes' not in data:
                return ValidationResult(False, "ERROR: Missing required field 'product_codes' in JSON.")
            
            product_codes = []
            for i, code in enumerate(data['product_codes']):
                if not isinstance(code, str):
                    return ValidationResult(False, f"ERROR: Invalid product code at index {i}.")
                code = code.strip()
                if not code:
                    return ValidationResult(False, f"ERROR: Empty product code at index {i}.")
                if not self.validate_product_code(code):
                    return ValidationResult(False, f"ERROR: Invalid characters detected in product_code at index {i}.")
                product_codes.append(code)
            
            return ValidationResult(True, data=product_codes)
        except Exception as e:
            return ValidationResult(False, f"ERROR: Invalid JSON format. {str(e)}")
    
    def analyze_product_code(self, code: str) -> ProductCodeAnalysis:
        """Analyze a single product code for palindrome properties."""
        reversed_code = code[::-1]
        is_palindrome = code.upper() == reversed_code.upper()
        return ProductCodeAnalysis(code, reversed_code, is_palindrome)
    
    def generate_report(self, product_codes: List[str]) -> str:
        """Generate the analysis report in markdown format."""
        self.analysis_results = [self.analyze_product_code(code) for code in product_codes]
        
        report = [
            "# Data Validation Report",
            "## 1. Data Structure Check:",
            f"- Number of product codes received: {len(product_codes)}",
            "",
            "## 2. Required Field Check:",
            "- product_code: Present",
            "",
            "## 3. Data Format Validation:",
            "- Each product code is alphanumeric: Yes",
            "",
            "## Validation Summary:",
            "Data validation is successful! Proceeding with analysis...",
            "",
            "# Processing Formulas & Logic:",
            "1. Reversal Process:",
            "   - Let Original Code = S, where S is a string.",
            "   - $$Reversed\\ Code = reverse(S)$$",
            "   Example: If S = \"A1B2\", then reverse(S) = \"2B1A\".",
            "",
            "2. Palindrome Determination:",
            "   - $$IF\\ S == reverse(S)\\ THEN\\ code\\ is\\ \"Palindrome\"\\ ELSE\\ \"Not\\ Palindrome\"$$",
            "",
            f"# Product Code Analysis Summary",
            f"Total Codes Evaluated: {len(self.analysis_results)}",
            "",
            "# Detailed Analysis"
        ]
        
        for analysis in self.analysis_results:
            report.extend([
                f"- Original Code: {analysis.original_code}",
                f"- Reversed Code: {analysis.reversed_code}",
                f"- Palindrome Status: {'Palindrome' if analysis.is_palindrome else 'Not Palindrome'}",
                "- Step-by-Step Explanation:",
                f"   - Step 1: Original Code = \"{analysis.original_code}\"",
                f"   - Step 2: Reversed Code = \"{analysis.reversed_code}\"",
                f"   - Step 3: IF Original Code equals Reversed Code THEN \"Palindrome\" ELSE \"Not Palindrome\"",
                ""
            ])
        
        report.extend([
            "# Final Report:",
            "Palindromes found:",
            *[f"- {analysis.original_code}" for analysis in self.analysis_results if analysis.is_palindrome],
            "",
            "# Feedback Request:",
            "Would you like detailed calculations for any specific product code? Rate this analysis (1-5)."
        ])
        
        return "\n".join(report)

    def process_data(self, data: str, format_type: str) -> Tuple[bool, str]:
        """Process the input data and return the report or error message."""
        if format_type.lower() == 'csv':
            validation_result = self.parse_csv_data(data)
        elif format_type.lower() == 'json':
            validation_result = self.parse_json_data(data)
        else:
            return False, "ERROR: Invalid format type. Please use CSV or JSON."
        
        if not validation_result.is_valid:
            return False, validation_result.error_message
        
        report = self.generate_report(validation_result.data)
        return True, report

# Example usage
if __name__ == "__main__":
#     # Example CSV input
#     csv_example = """product_code
# A1B1A
# 12321
# HELLO
# ABC123
# 121"""

    # Example JSON input
    json_example = """
        {
    "product_codes": [
        "RADAR",
        "4554",
        "STATS",
        "CIVIC",
        "KAYAK",
        "REFER",
        "SOLLOS",
        "ROTOR",
        "123454321",
        "BEEB"
    ]
    }

    """
    
    qa_system = PalindromeQA()
    
    # # Process CSV example
    # success, result = qa_system.process_data(csv_example, 'csv')
    # if success:
    #     print("CSV Analysis:")
    #     print(result)
    #     print("\n" + "="*50 + "\n")
    
    # Process JSON example
    success, result = qa_system.process_data(json_example, 'json')
    if success:
        print("JSON Analysis:")
        print(result)
        print("\n" + "="*50 + "\n")