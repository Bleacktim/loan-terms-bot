from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

text = """CIBC Personal Loan
Terms and Conditions

1. Overview
This Agreement applies to any money we lend you under your loan. Your loan may be secured on personal or real property you own or may be unsecured. You will pay (in Canadian dollars) all, or any part, of your debt when it is due or immediately when we demand it.

2. Promise to Repay
You will pay (in Canadian dollars) all amounts required by this Agreement in full, without delay.

3. Interest Payments
Until all amounts owing under this Agreement are paid in full, you must pay interest on the loan at the interest rate set out in the Statement of Disclosure both before and after any of the following events:
- we demand payment;
- the maturity date;
- default.

4. Interest Rate
We will not pay interest on any credit balance in your loan.
You will pay interest on all amounts outstanding on your loan at the annual interest rate set out in the Statement of Disclosure. The interest rate will change automatically whenever the prime rate changes. We may change our prime rate from time to time without notice to you. 

5. Fees and Charges
You must pay, and we may add to the principal amount owing under your loan, any fees, charges and any other amounts you may owe us under this Agreement, including:
- insurance premiums;
- the fees, charges and non-interest charges set out in the Statement of Disclosure.
If you fail to make a payment when due, we may charge you to recover any costs, including legal fees and expenses, we reasonably incur for any action we take to collect the amount you owe us.

6. Payments
You will make regular payments during the term of the loan with the payment frequency specified in the Statement of Disclosure. The total amount owed on your loan includes all amounts you owe on your loan, interest, insurance premiums, taxes and fees.

7. Demand
We may at any time, without prior notice to you and for any reason, demand immediate payment of any amounts outstanding under your loan or this Agreement.

8. Reporting Fraud
You must notify us immediately about any circumstance in which one might reasonably conclude that a fraud may occur in relation to your loan.
"""

for line in text.split('\n'):
    # encode to latin-1 to avoid fpdf character issues
    pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

os.makedirs("docs", exist_ok=True)
pdf.output("docs/loan_terms.pdf")
print("PDF created successfully at docs/loan_terms.pdf")
