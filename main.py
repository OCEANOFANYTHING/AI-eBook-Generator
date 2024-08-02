import cohere
import pdfkit
import markdown
import config  # Import the config file
import os


co = cohere.Client(config.COHERE_API_KEY)

def generate_ebook(topic, chapters):
    prompt = f"Write an eBook about {topic} with {chapters} chapters. Each chapter should have a title and content. Format the output in Markdown."

    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=10000,  # Adjust the output as necessary based on expected length
        temperature=0.7,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )

    return str(response.generations[0].text).strip()

def save_markdown(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def markdown_to_html(markdown_content):
    html_content = markdown.markdown(markdown_content)
    return html_content

def embed_html_template(html_content, template_filename):
    # Read the selected template HTML file from the templates folder
    with open(os.path.join('templates', template_filename), 'r', encoding='utf-8') as file:
        template = file.read()

    # Replace the placeholder with actual HTML content
    styled_html_content = template.replace('{{MARKDOWN_CONTENT}}', html_content)

    return styled_html_content

def convert_html_to_pdf(html_content, pdf_filename):
    # Convert HTML to PDF using pdfkit
    pdfkit.from_string(html_content, pdf_filename, options={"encoding": "UTF-8"})

if __name__ == "__main__":
    topic = input("Enter the eBook topic: ")
    chapters = int(input("Enter the number of chapters: "))

    print("Available templates:")
    print("1. Classic")
    print("2. Modern")
    print("3. Minimalist")
    print("4. Elegant")
    print("5. Dark")

    template_choice = int(input("Choose a template (1-5): "))

    template_files = {
        1: 'classic.html',
        2: 'modern.html',
        3: 'minimalist.html',
        4: 'elegant.html',
        5: 'dark.html'
    }

    template_filename = template_files.get(template_choice, 'classic.html')

    print("Generating eBook content...")
    ebook_content = generate_ebook(topic, chapters)
    
    markdown_filename = topic.replace(" ", "-") + ".md"
    pdf_filename = topic.replace(" ", "-") + ".pdf"
    
    print(f"Saving eBook as Markdown ({markdown_filename})...")
    save_markdown(ebook_content, markdown_filename)
    
    print(f"Converting Markdown to HTML...")
    html_content = markdown_to_html(ebook_content)
    
    print(f"Embedding HTML content into HTML template ({template_filename})...")
    html_template_content = embed_html_template(html_content, template_filename)
    
    print(f"Converting HTML to PDF ({pdf_filename})...")
    convert_html_to_pdf(html_template_content, pdf_filename)
    
    print(f"eBook {pdf_filename} generation complete!")
