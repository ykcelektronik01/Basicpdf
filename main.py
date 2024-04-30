from fpdf import FPDF
import pandas as pd

datas=pd.read_csv("topics.csv")

pdf=FPDF(orientation="P",unit="mm",format="a4")

for index,row in datas.iterrows():
    pdf.add_page()
    pdf.set_text_color(200, 20, 100)
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 27, 200, 27)



pdf.output("output.pdf")