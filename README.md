<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
</head>
<body>
    <h1>Healthcare Assistant Chatbot</h1>
    <p>A user-friendly Healthcare Assistant Chatbot application that leverages AI to provide quick responses to user queries. Built using <strong>Streamlit</strong>, <strong>NLTK</strong>, and <strong>Transformers</strong>, the chatbot can assist users with basic health-related queries, recommend consulting a doctor, and even provide general advice.</p>
    
<h2>Features</h2>
    <ul>
        <li><strong>Natural Language Processing:</strong> Utilizes a text-generation model (DistilGPT-2) for generating AI-based responses.</li>
        <li><strong>Streamlit Interface:</strong> An easy-to-use and interactive web interface for users.</li>
        <li><strong>Health Advice:</strong> Offers predefined responses for common healthcare-related queries.</li>
        <li><strong>Custom Responses:</strong> Uses a trained transformer model to respond to queries not covered by predefined answers.</li>
    </ul>

<h2>Prerequisites</h2>
    <p>Make sure you have the following installed:</p>
    <ul>
        <li>Python 3.8 or later</li>
        <li>Pip (Python package manager)</li>
    </ul>

<h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/your-username/healthcare-chatbot.git
cd healthcare-chatbot</code></pre>

<li>Install the required Python packages:</li>
<pre><code>pip install -r requirements.txt</code></pre>

<li>Download NLTK resources:</li>
<pre><code>import nltk
nltk.download('stopwords')
nltk.download('punkt')</code></pre>
    </ol>
<h2>Usage</h2>
<ol>
<li>Run the Streamlit application:</li>
<pre><code>streamlit run app.py</code></pre>

<li>Open your browser and navigate to:</li>
<pre><code>http://localhost:8501</code></pre>

<li>Interact with the chatbot by typing queries into the text input box and clicking the "Submit" button.</li>
</ol>

<h2>How It Works</h2>
    <ol>
<li><strong>User Input:</strong> The user provides a query through the Streamlit interface.</li>
<li><strong>Response Generation:</strong> The chatbot checks the query for specific keywords such as <code>symptom</code>, <code>appointment</code>, or <code>medication</code> to provide predefined responses.</li>
        <li><strong>AI-Powered Response:</strong> For other queries, the chatbot generates responses using the <code>distilgpt2</code> model.</li>
        <li><strong>Output:</strong> The chatbot displays the response back to the user in the Streamlit interface.</li>
    </ol>
    <h2>Key Technologies</h2>
    <ul>
        <li><strong>Streamlit:</strong> For building the web-based interface.</li>
        <li><strong>Transformers:</strong> The Hugging Face <code>distilgpt2</code> model is used for text generation.</li>
        <li><strong>NLTK:</strong> Used for tokenization and stopword handling.</li>
    </ul>

<h2>File Structure</h2>
    <pre><code>healthcare-chatbot/
|-- app.py            # Main application script
|-- requirements.txt  # Dependencies list
|-- README.md         # Project documentation (this file)
    </code></pre>

<h2>Dependencies</h2>
    <p>Listed in <code>requirements.txt</code>. Some key dependencies:</p>
    <ul>
        <li><code>streamlit</code></li>
        <li><code>transformers</code></li>
        <li><code>nltk</code></li>
    </ul>

<h2>Future Improvements</h2>
    <ul>
        <li><strong>Enhanced NLP:</strong> Improve response accuracy by fine-tuning a more domain-specific model.</li>
        <li><strong>Appointment Scheduling:</strong> Integrate with a calendar API to allow scheduling.</li>
        <li><strong>Medication Reminders:</strong> Add a feature to set reminders for taking medicines.</li>
    </ul>

<h2>Contributing</h2>
    <p>Contributions are welcome! Please fork the repository and submit a pull request.</p>

<h2>License</h2>
    <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>

<h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://huggingface.co/transformers/">Hugging Face Transformers</a></li>
        <li><a href="https://docs.streamlit.io/">Streamlit Documentation</a></li>
        <li><a href="https://www.nltk.org/">NLTK</a></li>
    </ul>
</body>
</html>
