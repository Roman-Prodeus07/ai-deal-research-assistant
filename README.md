# AI Deal Research Assistant

AI Deal Research Assistant is a lightweight Python project focused on organising company information, summarising business signals, and generating structured decision-support outputs for company research workflows.

The project is designed as a small internal-tool style MVP for business research, workflow automation, and investment/origination-style use cases.

## Project idea

Investment and business teams often work with messy company information spread across spreadsheets, websites, notes, news, and CRM systems. This can make it difficult to quickly understand which companies are worth prioritising, what signals matter, and what the next action should be.

This project explores how a simple AI-powered assistant could help turn unstructured company information into clear and useful outputs.

## What the tool is designed to do

The MVP is designed to help users:

* upload or work with a list of companies
* organise company information into a structured format
* summarise key business signals
* identify possible priority levels
* generate next-action suggestions
* create short research notes or outreach-style summaries

## Example use cases

* Company research for business development or investment teams
* Internal workflow automation
* Market mapping and target prioritisation
* Summarising business signals from company notes
* Creating structured outputs from messy research data

## Planned MVP features

* CSV upload with company information
* Clean table view of companies and notes
* Simple company summary generation
* Business signal extraction
* Priority scoring logic
* Next-action suggestions
* Streamlit interface for quick interaction

## Tech stack

* Python
* pandas
* Streamlit
* CSV data handling
* LLM-based prompting
* Basic data cleaning and structuring

## Current status

This project is currently in development.

The first version will focus on a simple Streamlit interface where users can upload a CSV file containing company names, sectors, websites, countries, and notes. The app will then generate structured summaries, business signals, and next-action suggestions.

## Why I am building this

I am building this project to practise creating practical AI tools that are useful in real workflows, not just demos.

The focus is on product thinking as much as technical implementation: understanding the user problem, designing a simple workflow, generating useful outputs, and improving the tool through feedback.

## Project structure

```text
ai-deal-research-assistant/
├── app.py
├── sample_companies.csv
├── requirements.txt
└── README.md
```

## Sample input

```csv
company_name,sector,country,website,notes
FinTrack AI,FinTech,UK,https://example.com,"AI tool for financial reporting automation. Recently expanded into enterprise clients."
HealthOps Cloud,HealthTech,Germany,https://example.com,"Cloud platform for hospital workflow management. Hiring sales and product teams."
RetailFlow,Software,France,https://example.com,"B2B software for retail inventory optimisation. Recently launched analytics dashboard."
```

## Planned output

For each company, the tool should generate:

* short company summary
* relevant business signals
* priority level
* suggested next action
* optional outreach note

## Future improvements

* Web scraping for public company information
* News and trigger monitoring
* CRM-style company tagging
* LLM integration through OpenAI or Claude
* Export to CSV or Excel
* More advanced scoring logic
* Dashboard view for company segments and priorities

## Related skills

This project helps me develop skills in:

* Python
* AI workflow design
* LLM prompting
* data cleaning
* product thinking
* business automation
* internal tool development
* decision-support systems

## Author

Roman Prodeus
Computer Science (Artificial Intelligence) student at the University of Greenwich
London, UK

LinkedIn: https://linkedin.com/in/roman-prodeus-3726172b2
GitHub: https://github.com/Roman-Prodeus07
