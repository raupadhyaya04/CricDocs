from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
def create_pdf(content):
    # Create a BytesIO object to hold the PDF in memory
    pdf_buffer = BytesIO()

    # Create the PDF with ReportLab
    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter

    # Define text settings
    pdf.setFont("Helvetica", 12)
    margin = 50
    line_height = 14
    max_width = width - 2 * margin

    # Split the large string into lines using \n (newlines)
    paragraphs = content.splitlines()

    # Set the initial y position for writing text
    y_position = height - margin

    # Iterate over each paragraph (split by newlines)
    for paragraph in paragraphs:
        # If the paragraph is empty (i.e., blank line), skip it but keep the spacing
        if not paragraph.strip():
            y_position -= line_height
            continue

        # Break paragraph into smaller chunks that fit within the page width
        while len(paragraph) > 0:
            # Check if we need to create a new page before writing the next chunk of text
            if y_position < margin + line_height:
                pdf.showPage()  # Start a new page when we run out of space
                y_position = height - margin
                pdf.setFont("Helvetica", 12)  # Reset font settings after new page

            # Fit as much text as possible within the page width
            text_chunk = paragraph[:95]  # Adjust to fit your desired text width

            # Draw the text chunk
            pdf.drawString(margin, y_position, text_chunk)

            # Move to the next line
            y_position -= line_height

            # Update paragraph to remove the written chunk
            paragraph = paragraph[95:]

        # Add additional spacing after the paragraph
        y_position -= line_height

    # Save the PDF
    pdf.save()

    # Move the buffer's position to the start
    pdf_buffer.seek(0)

    return pdf_buffer