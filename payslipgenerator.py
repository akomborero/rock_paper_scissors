import pandas as pd
from fpdf import FPDF
import os
import yagmail

try:
    df = pd.read_excel("employees.xlsx")
except FileNotFoundError:
    print("Error: employees.xlsx not found. Please make sure it's in the same folder as this script.")
    exit()

# Your email and the app password you generated
email = "makomborerichidzviva@gmail.com"  # Replace with your email
app_password = "ukhi qubc aser lqfe"  # Replace with your app password

# Setting up yagmail
yag = yagmail.SMTP(email, app_password)

def generate_payslip(emp_id, name, basic, allowances, deductions, net_salary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Uncommon.org - Employee Payslip", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(100, 10, f"Employee ID: {emp_id}", ln=True)
    pdf.cell(100, 10, f"Name: {name}", ln=True)
    pdf.ln(5)
    pdf.cell(100, 10, f"Basic Salary: ${basic:.2f}", ln=True)
    pdf.cell(100, 10, f"Allowances: ${allowances:.2f}", ln=True)
    pdf.cell(100, 10, f"Deductions: ${deductions:.2f}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(100, 10, f"Net Salary: ${net_salary:.2f}", ln=True)

    if not os.path.exists("payslips"):
        os.makedirs("payslips")

    filename = f"payslips/{emp_id}.pdf"
    pdf.output(filename)
    print(f" Payslip saved: {filename}")
    
    return filename  # Returning the filename to send it via email

# Step 3: Loop through employees and generate payslips
for index, row in df.iterrows():
    try:
        emp_id = row["Employee ID"]
        name = row["Name"]
        email = row["Email"]
        basic = row["Basic Salary"]
        allowances = row["Allowances"]
        deductions = row["Deductions"]
        net_salary = basic + allowances - deductions

        payslip_filename = generate_payslip(emp_id, name, basic, allowances, deductions, net_salary)

        # Send the email with the payslip as an attachment
        subject = "Your Payslip"
        body = "Please find your payslip attached."
        yag.send(email, subject, body, payslip_filename)
        print(f" Payslip sent to {email} successfully!")

    except Exception as e:
        print(f" Error processing row {index + 1}: {e}")
