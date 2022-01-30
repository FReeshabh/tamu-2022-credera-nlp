import os
import pandas as pd
from transformers import pipeline
import argparse

def HGExtractFromText(context):
    
    question_answerer = pipeline("question-answering")
    
    NameHG = question_answerer(question="What's the company name? Corporation", context=context)
    InvoiceIDHG = question_answerer(question="What's the company, order, invoice ID or number?", context=context)
    InvoiceDateHG = question_answerer(question="What's the order, invoice date?", context=context)
    InvoiceDueDateHG = question_answerer(question="What's the due date for this order, invoice? Payment date, days", context=context)
    BillingAddressHG = question_answerer(question="What is the billing address? Bill to CREDIT DEBIT ADDRESS", context=context)
    ShippingAddressHG = question_answerer(question="What is the shipping address? Ship to CREDIT DEBIT ADDRESS", context=context)
    BillAmountHG = question_answerer(question="How much does it cost? What's the total amount? $? total, subtotal", context=context)
    OtherInformationHG = question_answerer(question="What's the address, quality, quantity, cost, etc.?", context="context")
    
    """
    NameHG = question_answerer(question="What's the company name?", context=context)
    InvoiceIDHG = question_answerer(question="ID id reg no. number registration", context=context)
    InvoiceDateHG = question_answerer(question="date invoice date", context=context)
    InvoiceDueDateHG = question_answerer(question="due date invoice due date", context=context)
    BillingAddressHG = question_answerer(question="Billing Address address billing", context=context)
    ShippingAddressHG = question_answerer(question="Shipping address shipping Address", context=context)
    BillAmountHG = question_answerer(question="Total bill amount balance due subtotal", context=context)
    OtherInformationHG = question_answerer(question="Name, quantity, quality device product address", context="context")

"""
    changeToDict = {
        'Name': NameHG['answer'],
        'Invoice ID': InvoiceIDHG['answer'],
        'Invoice date': InvoiceDateHG['answer'],
        'Invoice Due date': InvoiceDueDateHG['answer'],
        'Billing Address': BillingAddressHG['answer'],
        'Shipping Addresss': ShippingAddressHG['answer'],
        'Billing Amount': BillAmountHG['answer'],
        'Other Information': OtherInformationHG['answer'],
    }
    toPandas = pd.DataFrame(changeToDict, index=[0])
    toPandas.to_csv("BAHHHHHHHH.csv")


"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("context", help="the context")
    args = parser.parse_args()
    HGExtractFromText(args.context)
"""

context = r"""



"MS
Payment Reminder
ARTS
MANAGEMENT
SYSTEMS
Date: April 25, 2011
Phone: (403) 243-4096
Account #44
From: Arts Management Systems Ltd.
Suite 300
2, 3012 - 17 Avenue SE
Calgary AB T2A OP9
To: JANE SMITH
85 JOHNSTON ST
CALGARY AL T6M 983
Date
Item
Description
Qty
Total
Order # 102 April 19, 2011
Tickets
Die Fledermaus on October 7 2011 at 7:30 PM - 10-FLE
4 $500.00
Tickets
Annie Get Your Gun on December 2 2011 at 7:30 PM - 11-AGG
4 $220.00
Big Time Rush on February 11 2012 at 2:00 PM - 11-RSH
Stamp Collectors Convention 2011 on January 10 2012 at 10:00 AM - 11-STM
Tickets
6 $120.00
Tickets
2
$36.00
Total Tickets
16 $876.00
APR 19 2011
APR 19 2011
Membership Gift Certificates
Donation
I $100.00
Individual Donations
1
$50.00
Total Donations
$50.00
Fees
$5.00
Order Total: $1,031.00
APR 19 2011
APR 19 2011
Раyment
Раyment
Cheque - 123845
Cheque - 968
1 S-500.00
1 S-250.00
2 S-750.00
Total Paid
Balance Due: $281.00
A payment is now due. Please forward your payment along with the remittance coupon below.
Please Remit this Portion with your Payment
Balance Due:
$281.00
To: Arts Management Systems Ltd.
Name: JANE SMITH (File #44)
Suite 300
2, 3012 - 17 Avenue SE
Calgary AB T2A OP9
"

"MS"

"Payment"

"Reminder"

"ARTS"

"MANAGEMENT"

"SYSTEMS"

"Date:"

"April"

"25,"

"2011"

"Phone:"

"(403)"

"243-4096"

"Account"

"#44"

"From:"

"Arts"

"Management"

"Systems"

"Ltd."

"Suite"

"300"

"2,"

"3012"

"-"

"17"

"Avenue"

"SE"

"Calgary"

"AB"

"T2A"

"OP9"

"To:"

"JANE"

"SMITH"

"85"

"JOHNSTON"

"ST"

"CALGARY"

"AL"

"T6M"

"983"

"Date"

"Item"

"Description"

"Qty"

"Total"

"Order"

"#"

"102"

"April"

"19,"

"2011"

"Tickets"

"Die"

"Fledermaus"

"on"

"October"

"7"

"2011"

"at"

"7:30"

"PM"

"-"

"10-FLE"

"4"

"$500.00"

"Tickets"

"Annie"

"Get"

"Your"

"Gun"

"on"

"December"

"2"

"2011"

"at"

"7:30"

"PM"

"-"

"11-AGG"

"4"

"$220.00"

"Big"

"Time"

"Rush"

"on"

"February"

"11"

"2012"

"at"

"2:00"

"PM"

"-"

"11-RSH"

"Stamp"

"Collectors"

"Convention"

"2011"

"on"

"January"

"10"

"2012"

"at"

"10:00"

"AM"

"-"

"11-STM"

"Tickets"

"6"

"$120.00"

"Tickets"

"2"

"$36.00"

"Total"

"Tickets"

"16"

"$876.00"

"APR"

"19"

"2011"

"APR"

"19"

"2011"

"Membership"

"Gift"

"Certificates"

"Donation"

"I"

"$100.00"

"Individual"

"Donations"

"1"

"$50.00"

"Total"

"Donations"

"$50.00"

"Fees"

"$5.00"

"Order"

"Total:"

"$1,031.00"

"APR"

"19"

"2011"

"APR"

"19"

"2011"

"Раyment"

"Раyment"

"Cheque"

"-"

"123845"

"Cheque"

"-"

"968"

"1"

"S-500.00"

"1"

"S-250.00"

"2"

"S-750.00"

"Total"

"Paid"

"Balance"

"Due:"

"$281.00"

"A"

"payment"

"is"

"now"

"due."

"Please"

"forward"

"your"

"payment"

"along"

"with"

"the"

"remittance"

"coupon"

"below."

"Please"

"Remit"

"this"

"Portion"

"with"

"your"

"Payment"

"Balance"

"Due:"

"$281.00"

"To:"

"Arts"

"Management"

"Systems"

"Ltd."

"Name:"

"JANE"

"SMITH"

"(File"

"#44)"

"Suite"

"300"

"2,"

"3012"

"-"

"17"

"Avenue"

"SE"

"Calgary"

"AB"

"T2A"

"OP9"




"""
HGExtractFromText(context)
