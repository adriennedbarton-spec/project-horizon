# Project Horizon

**Building Nova: A Customer Education Assistant**

Project Horizon is an independent learning and portfolio project exploring the intersection of **Customer Education strategy, learning technology, and AI**.

I'm building Nova, a customer education assistant for Horizon Training & Certification, a fictional SaaS learning platform.

The project is grounded in a challenge I've encountered throughout my Customer Education career: delivering accurate, accessible learning resources at scale while maintaining a sustainable infrastructure behind them.

Through Project Horizon, I'm developing hands-on technical skills in Python, application development, and AI while applying my experience in learning systems architecture, knowledge management, and customer enablement.

## Meet Nova

Nova is an evolving customer education assistant designed to help users find relevant guidance about Horizon's training and certification platform.

![Nova's Streamlit interface](screenshots/nova-v0.5.png)

### Current Capabilities

- **Structured knowledge base:** Articles covering learning paths, certifications, enrollment, analytics, and user management.
- **Question recognition:** Rule-based keyword matching that accommodates common variations in customer questions.
- **Role-based access:** Different knowledge permissions for administrators and learners.
- **User experience:** A branded Streamlit interface designed around straightforward, self-service support.
- **Quality assurance:** Six automated pytest tests covering topic recognition and access permissions.

Nova currently uses rule-based matching rather than AI-generated responses. AI-powered retrieval, source citations, and evaluation are planned future enhancements.

## Technology

- Python
- Streamlit
- pytest
- Git and GitHub

## Getting Started

Clone the repository, then install the required dependencies:

```bash
python -m pip install streamlit pytest
```

Launch Nova:

```bash
python -m streamlit run app.py
```

Run the automated tests:

```bash
python -m pytest test_nova.py -v
```

## Development Roadmap

- [x] Build a structured knowledge base
- [x] Implement keyword-based question recognition
- [x] Add role-based article permissions
- [x] Build a branded Streamlit interface
- [x] Create automated tests
- [x] Establish Git version control
- [ ] Improve question matching and ambiguous-query handling
- [ ] Implement AI-powered retrieval with source citations
- [ ] Evaluate response accuracy and reliability
- [ ] Develop a portfolio case study documenting technical and strategic decisions

## Why This Project Matters

My professional background is in Customer Education leadership, instructional design, and learning systems management. I've built and scaled SaaS education programs, developed certification programs, and worked to connect learning infrastructure with product experiences.

I believe effective Customer Education leadership increasingly requires more than expertise in learning design. It requires an understanding of the systems, data, integrations, and emerging technologies that make education programs scalable and sustainable.

Project Horizon is my opportunity to deepen that technical fluency through practical application.

**My goal isn't to become a software engineer. It's to become a more technically capable Customer Education leader—one who can evaluate opportunities, collaborate effectively with engineering teams, and help design better learning systems.**

---

*Project Horizon is an independent learning and portfolio project. Horizon Training & Certification is a fictional platform.*