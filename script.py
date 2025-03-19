import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def convert_md_to_docx():
    # Get all markdown files in the markdown directory
    markdown_dir = 'markdown'
    for filename in os.listdir(markdown_dir):
        if filename.endswith('.md'):
            md_path = os.path.join(markdown_dir, filename)
            docx_path = os.path.join(markdown_dir, filename.replace('.md', '.docx'))
            
            # Create a new Word document
            doc = Document()
            
            # Read and process the markdown file
            with open(md_path, 'r', encoding='utf-8') as md_file:
                lines = md_file.readlines()
                
                for line in lines:
                    # Handle headers
                    if line.startswith('#'):
                        level = line.count('#')
                        text = line.strip('#').strip()
                        paragraph = doc.add_paragraph()
                        run = paragraph.add_run(text)
                        run.font.size = Pt(16 - level)  # Decrease size for deeper headers
                        run.bold = True
                        
                    # Handle bullet points
                    elif line.strip().startswith('*'):
                        text = line.strip('* ').strip()
                        doc.add_paragraph(text, style='List Bullet')
                        
                    # Handle tables
                    elif '|' in line:
                        # Skip table formatting lines
                        if ':---' in line:
                            continue
                        cells = [cell.strip() for cell in line.strip('|').split('|')]
                        if len(cells) > 1:
                            table = doc.add_table(rows=1, cols=len(cells))
                            for i, cell in enumerate(cells):
                                table.cell(0, i).text = cell
                                
                    # Regular text
                    else:
                        if line.strip():
                            doc.add_paragraph(line.strip())
            
            # Save the Word document
            doc.save(docx_path)
            print(f'Converted {filename} to Word format')

if __name__ == '__main__':
    convert_md_to_docx()
