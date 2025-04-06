from flask import Flask, render_template, request
from utils.ETS import extract_tables_to_markdown
from utils.utils_gemini import analyze_markdown_with_gemini
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'docs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    markdown_content = None
    analysis_result = None

    if request.method == 'POST':
        url = request.form['url']
        action = request.form.get('action')

        if not url:
            error = "Please enter a URL."
            return render_template('index.html', error=error)

        if action == 'analyze':
            markdown_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'tables.markdown')
            success = extract_tables_to_markdown(url, output_dir=app.config['UPLOAD_FOLDER'])

            if success:
                with open(markdown_filepath, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
                    analysis_result = analyze_markdown_with_gemini(markdown_content)
                os.remove(markdown_filepath)
            else:
                error = "Failed to extract tables for analysis."
        elif action == 'extract':
            markdown_filename = 'tables.markdown'
            markdown_filepath = os.path.join(app.config['UPLOAD_FOLDER'], markdown_filename)
            success = extract_tables_to_markdown(url, output_dir=app.config['UPLOAD_FOLDER'])
            if success:
                with open(markdown_filepath, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
            else:
                error = "Failed to extract tables to Markdown."

    return render_template('index.html', error=error, markdown_content=markdown_content,
                           analysis_result=analysis_result)


@app.route('/download/markdown')
def download_markdown():
    markdown_content = request.args.get('markdown_content')
    if markdown_content:
        from flask import send_file
        import io
        mem = io.BytesIO()
        mem.write(markdown_content.encode('utf-8'))
        mem.seek(0)
        return send_file(
            mem,
            mimetype='text/markdown',
            as_attachment=True,
            download_name='extracted_tables.md'
        )
    else:
        return "No markdown content to download.", 400


if __name__ == '__main__':
    app.run(debug=True)
