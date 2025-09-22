import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

def create_custom_styles(doc):
    """Create custom styles for the document"""
    styles = doc.styles
    
    # Main Title Style
    try:
        main_title_style = styles['MainTitle']
    except KeyError:
        main_title_style = styles.add_style('MainTitle', WD_STYLE_TYPE.PARAGRAPH)
        main_title_font = main_title_style.font
        main_title_font.name = 'Arial'
        main_title_font.size = Pt(18)
        main_title_font.bold = True
        main_title_font.color.rgb = RGBColor(0, 51, 102)  # Dark blue
        main_title_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        main_title_style.paragraph_format.space_after = Pt(12)
    
    # Question Title Style
    try:
        question_style = styles['QuestionTitle']
    except KeyError:
        question_style = styles.add_style('QuestionTitle', WD_STYLE_TYPE.PARAGRAPH)
        question_font = question_style.font
        question_font.name = 'Arial'
        question_font.size = Pt(14)
        question_font.bold = True
        question_font.color.rgb = RGBColor(204, 0, 0)  # Red
        question_style.paragraph_format.space_before = Pt(16)
        question_style.paragraph_format.space_after = Pt(8)
    
    # Section Heading Style
    try:
        section_style = styles['SectionHeading']
    except KeyError:
        section_style = styles.add_style('SectionHeading', WD_STYLE_TYPE.PARAGRAPH)
        section_font = section_style.font
        section_font.name = 'Arial'
        section_font.size = Pt(12)
        section_font.bold = True
        section_font.color.rgb = RGBColor(0, 102, 51)  # Dark green
        section_style.paragraph_format.space_before = Pt(8)
        section_style.paragraph_format.space_after = Pt(4)
    
    # Subsection Style
    try:
        subsection_style = styles['Subsection']
    except KeyError:
        subsection_style = styles.add_style('Subsection', WD_STYLE_TYPE.PARAGRAPH)
        subsection_font = subsection_style.font
        subsection_font.name = 'Arial'
        subsection_font.size = Pt(11)
        subsection_font.bold = True
        subsection_font.color.rgb = RGBColor(51, 51, 153)  # Blue
        subsection_style.paragraph_format.space_before = Pt(6)
        subsection_style.paragraph_format.space_after = Pt(3)
    
    # Normal text style
    try:
        normal_style = styles['CustomNormal']
    except KeyError:
        normal_style = styles.add_style('CustomNormal', WD_STYLE_TYPE.PARAGRAPH)
        normal_font = normal_style.font
        normal_font.name = 'Calibri'
        normal_font.size = Pt(11)
        normal_style.paragraph_format.space_after = Pt(3)

def add_horizontal_line(doc):
    """Add a horizontal line separator"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Create a border
    p_fmt = p.paragraph_format
    p_fmt.space_before = Pt(6)
    p_fmt.space_after = Pt(6)
    
    # Add the line using underline
    run = p.add_run('_' * 80)
    run.font.color.rgb = RGBColor(128, 128, 128)  # Gray

def process_text_file(input_file, output_file):
    """Process the text file and convert to Word document"""
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Create a new document
    doc = Document()
    
    # Create custom styles
    create_custom_styles(doc)
    
    # Split content into lines
    lines = content.split('\n')
    
    # Process each line
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines at the beginning
        if not line and i < 10:
            i += 1
            continue
        
        # Main title
        if line == "Automation Mid Sem PYQ":
            p = doc.add_paragraph(line, style='MainTitle')
            add_horizontal_line(doc)
            i += 1
            continue
        
        # Question headers (Q1), Q2), etc.)
        if re.match(r'^Q\d+\)', line):
            if i > 0:  # Add space before new question (except first)
                doc.add_paragraph()
            p = doc.add_paragraph(line, style='QuestionTitle')
            i += 1
            continue
        
        # Main section headings (ALL CAPS or specific patterns)
        if (line.isupper() and len(line.split()) > 1 and 
            not line.startswith('*') and 
            not line.startswith('-') and
            len(line) > 10):
            p = doc.add_paragraph(line, style='SectionHeading')
            i += 1
            continue
        
        # Subsection headings (numbered or lettered)
        if (re.match(r'^\d+\.', line) or 
            re.match(r'^[A-Z]\.', line) or
            re.match(r'^\w+\s+\w+\s+CYLINDER', line)):
            p = doc.add_paragraph(line, style='Subsection')
            i += 1
            continue
        
        # Horizontal separators
        if line.startswith('---') and len(line) > 10:
            add_horizontal_line(doc)
            i += 1
            continue
        
        # Bullet points
        if line.startswith('*') or re.match(r'^\s*\*', line):
            # Clean up the bullet point
            clean_line = re.sub(r'^\s*\*\s*', '', line)
            p = doc.add_paragraph(clean_line, style='List Bullet')
            
            # Check for sub-bullets or additional content
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('*'):
                sub_line = lines[j].strip()
                clean_sub_line = re.sub(r'^\s*\*\s*', '', sub_line)
                doc.add_paragraph(clean_sub_line, style='List Bullet 2')
                j += 1
            i = j
            continue
        
        # Numbered lists
        if re.match(r'^\s*\d+\.', line):
            p = doc.add_paragraph(line, style='List Number')
            i += 1
            continue
        
        # Summary sections
        if line.startswith('Summary'):
            p = doc.add_paragraph(line, style='SectionHeading')
            i += 1
            continue
        
        # Definition sections
        if line == 'DEFINITION' or line.startswith('DEFINITION OF'):
            p = doc.add_paragraph(line, style='SectionHeading')
            i += 1
            continue
        
        # Regular text
        if line:
            # Handle special arrows and symbols
            line = line.replace('â†', '→').replace('â€"', '—').replace('Â°', '°')
            line = line.replace('â€™', "'").replace('â€œ', '"').replace('â€', '"')
            
            p = doc.add_paragraph(line, style='CustomNormal')
        
        i += 1
    
    # Save the document
    doc.save(output_file)
    print(f"Document saved as {output_file}")

def main():
    """Main function"""
    input_file = "TextToWord/Automation-Mid-Sem-PYQ.txt"  # Input text file
    output_file = "Automation-Mid-Sem-PYQ.docx"  # Output Word file
    
    try:
        process_text_file(input_file, output_file)
        print("Conversion completed successfully!")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        print("Please make sure the file exists in the same directory as this script.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
