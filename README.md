# PalindromeQA Case Study

## Overview

**PalindromeQA** is an intelligent system developed to analyze unique alphanumeric product codes for palindromic patterns. Its primary goal is to validate input data, process each product code with clear, step-by-step logic to determine if it is a palindrome, and generate a detailed final report that anyone can understand—even someone without a technical background.

This system ensures that every product code is checked thoroughly. It reverses each code and compares it with the original, then explains each step in simple language along with formulas that make the process easy to follow.

## Features

- **Data Validation:**  
  The system checks the input for:
  - Correct file format: only CSV or JSON provided as plain text within markdown code blocks.
  - Language: only English input is accepted.
  - Presence of the required field: `product_code` (for CSV) or an array under the key `product_codes` (for JSON).
  - Proper content: Each product code must be a non-empty string with only letters and digits (alphanumeric).

- **Palindrome Processing:**  
  For each product code, the system:
  - Reverses the code.
  - Compares the original code with its reversed version.
  - Determines if the code is a "Palindrome" (reads the same forwards and backwards) or "Not Palindrome".

- **Step-by-Step Explanations:**  
  Every analysis comes with a detailed explanation that breaks down:
  - The original code.
  - The reversed code.
  - The comparison process.
  - A simple formula:  
    $$"Reversed\ Code = reverse(Original\ Code)"$$  
  This makes it clear how the final result is determined.

- **Detailed Final Report:**  
  The final report includes:
  - A summary of data validation.
  - Processing formulas and logic.
  - A detailed breakdown for each product code.
  - A final list of all codes identified as palindromes.
  - A feedback request to improve future analyses.

- **Feedback and Iterative Improvement:**  
  After the report is generated, the system asks for feedback on the analysis. Depending on the rating provided, the system either thanks the user for positive feedback or asks for suggestions on how to improve the process.

## System Prompt

The system behavior is governed by a detailed prompt that outlines all the rules for language, data validation, processing logic, response formatting, and error handling. Below is an excerpt that captures the essence of the system prompt:

```markdown
**[system]**

You are PalindromeQA, a system designed to analyze unique alphanumeric product codes for palindromic patterns. Your role is to validate input data, process each product code with step-by-step logic to determine if it is a palindrome, and generate a detailed final report. Follow the instructions below exactly.

LANGUAGE & FORMAT LIMITATIONS
- Only process input in ENGLISH.
- Accept data only as plain text within markdown code blocks labeled as CSV or JSON.

GREETING PROTOCOL
- Greet based on urgency, time, or provided names.
- Ask if the user needs a template for data input if requested.

DATA INPUT & VALIDATION PROTOCOL
- For CSV: Expect a header row with "product_code".
- For JSON: Expect an object with the key "product_codes" containing an array of product code strings.
- Validate that each product code is a non-empty alphanumeric string.

PROCESSING LOGIC
- Reverse each code character by character.
- Compare the original and reversed code to determine if it is a palindrome.
- Provide detailed, step-by-step explanations for each code.

REPORT FORMAT
- Include sections on data validation, processing formulas, detailed analysis, and final report.
- End with a feedback request asking if the user needs more details or suggestions for improvement.
```

## Metadata

- **Project Name:** PalindromeQA  
- **Version:** 1.0.0  
- **Author:** Usman Ashfaq  
- **Keywords:** Palindrome, Product Code Analysis, Data Validation, Step-by-Step Explanation, Automation

## Variations and Test Flows

### Flow 1: Basic Greeting and Template Request
- **User Action:**  
  The user greeted with a simple "hi".
- **Assistant Response:**  
  PalindromeQA responded with a default greeting and asked if the user needed a template for data input.
- **User Action:**  
  The user accepted the template request.
- **Assistant Response:**  
  The system provided CSV and JSON templates.
- **User Action:**  
  The user submitted CSV data containing multiple product codes.
- **Assistant Response:**  
  The system validated the data, processed each product code (by reversing and comparing), and returned a detailed palindrome analysis report.
- **Feedback:**  
  The user rated the analysis positively.

### Flow 2: Time-based Greeting and No Template Request
- **User Action:**  
  The user greeted with "Good morning, it's 9 AM" and indicated no need for a template.
- **Assistant Response:**  
  PalindromeQA provided a time-appropriate greeting and prompted the user for data.
- **User Action:**  
  The user supplied CSV data with several product codes.
- **Assistant Response:**  
  The system processed the data, generated a comprehensive analysis report, and included a final list of palindromic codes.
- **Feedback:**  
  The user rated the analysis as 5, prompting a positive acknowledgment from the system.
  Flow #2 final report:
  ````
  # Data Validation Report
## 1. Data Structure Check:
- Number of product codes received: 10

## 2. Required Field Check:
- product_code: Present

## 3. Data Format Validation:
- Each product code is alphanumeric: Yes

## Validation Summary:
Data validation is successful! Proceeding with analysis...

# Processing Formulas & Logic:
1. Reversal Process:
 - Let Original Code = S, where S is a string.
 $$"Reversed\ Code = reverse(Original\ Code)"$$
 - Reversed Code = reverse(S)
   
2. Palindrome Determination:
 - IF S == reverse(S) THEN code is "Palindrome" ELSE "Not Palindrome"

# Product Code Analysis Summary
Total Codes Evaluated: 10

# Detailed Analysis
- Original Code: RADAR  
  Reversed Code: RADAR  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "RADAR"
  - Step 2: Reversed Code = "RADAR"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: 4554  
  Reversed Code: 4554  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "4554"
  - Step 2: Reversed Code = "4554"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: STATS  
  Reversed Code: STATS  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "STATS"
  - Step 2: Reversed Code = "STATS"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: CIVIC  
  Reversed Code: CIVIC  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "CIVIC"
  - Step 2: Reversed Code = "CIVIC"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: KAYAK  
  Reversed Code: KAYAK  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "KAYAK"
  - Step 2: Reversed Code = "KAYAK"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: REFER  
  Reversed Code: REFER  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "REFER"
  - Step 2: Reversed Code = "REFER"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: SOLLOS  
  Reversed Code: SOLLOS  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "SOLLOS"
  - Step 2: Reversed Code = "SOLLOS"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: ROTOR  
  Reversed Code: ROTOR  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "ROTOR"
  - Step 2: Reversed Code = "ROTOR"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: 123454321  
  Reversed Code: 123454321  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "123454321"
  - Step 2: Reversed Code = "123454321"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

- Original Code: BEEB  
  Reversed Code: BEEB  
  Palindrome Status: Palindrome  
  Step-by-Step Explanation:
  - Step 1: Original Code = "BEEB"
  - Step 2: Reversed Code = "BEEB"
  - Step 3: IF Original Code equals Reversed Code THEN "Palindrome"

# Final Report:
Palindromic Product Codes: RADAR, 4554, STATS, CIVIC, KAYAK, REFER, SOLLOS, ROTOR, 123454321, BEEB

# Feedback Request:
Would you like detailed calculations for any specific product code? Rate this analysis (1-5).
````

### Flow 3: JSON Data with Errors and Corrections
- **User Action:**  
  In an emergency tone, the user submitted JSON data that had a missing required field (an empty string in the array).
- **Assistant Response:**  
  PalindromeQA detected the missing field and returned an error message specifying the issue.
- **User Action:**  
  The user then provided new JSON data that contained an invalid character (non-alphanumeric).
- **Assistant Response:**  
  The system again returned an error message pointing out the invalid character.
- **User Action:**  
  Finally, the user submitted correct JSON data with all valid product codes.
- **Assistant Response:**  
  The system processed the correct data and generated a detailed analysis report.
- **Feedback:**  
  The user rated the analysis as 3, prompting the system to ask, "How can we improve our product code analysis process?"

## Conclusion

**PalindromeQA** stands as a robust, flexible, and user-friendly tool designed to simplify the process of analyzing product codes for palindromic patterns. By enforcing strict data validation rules and providing clear, step-by-step explanations, it ensures both accuracy and transparency in its output. The various test flows demonstrate how PalindromeQA handles different scenarios—from simple greetings to emergency error corrections—and continuously adapts based on user feedback. This project exemplifies how automation can take a complex task and make it accessible and understandable to everyone, paving the way for smarter, data-driven decision making.

---
