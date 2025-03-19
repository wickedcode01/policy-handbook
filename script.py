import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def convert_md_to_docx():
    # Get all markdown files in the markdown directory
    markdown_dir = 'markdown'
    for filename in os.listdir(markdown_dir):
        # Process all files and directories recursively
        for root, dirs, files in os.walk(markdown_dir):
            # Create corresponding directories in output
            rel_path = os.path.relpath(root, markdown_dir)
            docx_dir = os.path.join('', rel_path)
            os.makedirs(docx_dir, exist_ok=True)
            
            # Process markdown files
            for filename in files:
                if filename.endswith('.md'):
                    md_path = os.path.join(root, filename)
                    docx_path = os.path.join(docx_dir, filename.replace('.md', '.docx'))
                    
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
                            elif line.strip().startswith('* ') and not line.strip().startswith('**'):
                                # Remove only the leading bullet point marker
                                text = line[line.find('* ') + 2:].strip()
                                paragraph = doc.add_paragraph(style='List Bullet')
                                
                                # Process bold and italic text in bullet points
                                while '**' in text or '*' in text:
                                    # Handle bold text first (**text**)
                                    bold_start = text.find('**')
                                    if bold_start != -1:
                                        bold_end = text.find('**', bold_start + 2)
                                        if bold_end != -1:
                                            # Add text before bold
                                            if bold_start > 0:
                                                paragraph.add_run(text[:bold_start])
                                            # Add bold text
                                            bold_text = text[bold_start + 2:bold_end]
                                            run = paragraph.add_run(bold_text)
                                            run.bold = True
                                            # Continue with remaining text
                                            text = text[bold_end + 2:]
                                            continue
                                    
                                    # Handle italic text (*text*)
                                    italic_start = text.find('*')
                                    if italic_start != -1:
                                        italic_end = text.find('*', italic_start + 1)
                                        if italic_end != -1:
                                            # Add text before italic
                                            if italic_start > 0:
                                                paragraph.add_run(text[:italic_start])
                                            # Add italic text
                                            italic_text = text[italic_start + 1:italic_end]
                                            run = paragraph.add_run(italic_text)
                                            run.italic = True
                                            # Continue with remaining text
                                            text = text[italic_end + 1:]
                                            continue
                                    
                                    break  # Break if no more formatting found
                                
                                # Add any remaining text
                                if text:
                                    paragraph.add_run(text)
                                
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
                                    paragraph = doc.add_paragraph()
                                    text = line.strip()
                                    
                                    # Process bold and italic text
                                    while '**' in text or '*' in text:
                                        # Handle bold text first (**text**)
                                        bold_start = text.find('**')
                                        if bold_start != -1:
                                            bold_end = text.find('**', bold_start + 2)
                                            if bold_end != -1:
                                                # Add text before bold
                                                if bold_start > 0:
                                                    paragraph.add_run(text[:bold_start])
                                                # Add bold text
                                                bold_text = text[bold_start + 2:bold_end]
                                                run = paragraph.add_run(bold_text)
                                                run.bold = True
                                                # Continue with remaining text
                                                text = text[bold_end + 2:]
                                                continue
                                        
                                        # Handle italic text (*text*)
                                        italic_start = text.find('*')
                                        if italic_start != -1:
                                            italic_end = text.find('*', italic_start + 1)
                                            if italic_end != -1:
                                                # Add text before italic
                                                if italic_start > 0:
                                                    paragraph.add_run(text[:italic_start])
                                                # Add italic text
                                                italic_text = text[italic_start + 1:italic_end]
                                                run = paragraph.add_run(italic_text)
                                                run.italic = True
                                                # Continue with remaining text
                                                text = text[italic_end + 1:]
                                                continue
                                        
                                        break  # Break if no more formatting found
                                    
                                    # Add any remaining text
                                    if text:
                                        paragraph.add_run(text)
                    
                    # Save the Word document
                    doc.save(docx_path)
                    print(f'Converted {md_path} to Word format')
if __name__ == '__main__':
    convert_md_to_docx()
