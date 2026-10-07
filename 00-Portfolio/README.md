# 00-Portfolio: Developer & DevOps Engineering Portfolio

This folder contains the source code for Arya Y P's Personal Portfolio & Engineering Showcase website.

---

## 🌐 Live Site & GitHub Pages Deployment

The portfolio is configured for **automated continuous deployment** via **GitHub Actions** to **GitHub Pages**.

- **Workflow File:** [`.github/workflows/deploy.yml`](../.github/workflows/deploy.yml)
- **Deployment Trigger:** Every push to the `main` branch.
- **Hosted Files:**
  - `index.html` (Main interactive portfolio interface)
  - `Arya_Y_P_Resume_linked.pdf` (Linked engineering resume)

---

## 🛠️ Portfolio Features

- **Interactive Project Filtering:** Dynamic JavaScript filtering for Web Development, Machine Learning, Networking, and Mobile applications.
- **Quick-Commerce & Systems Showcase:** Highlights real-time P2P WebRTC video conferencing, ML anomaly detection pipelines, and Kubernetes microservice deployments.
- **Light & Dark Theme Engine:** Responsive, CSS variable-driven UI supporting system preference and manual themes.
- **Direct Mail Contact Form:** Direct mailto integration targeting `arya1262023@gmail.com`.

---

## 🚀 Local Development

To run and preview the portfolio site locally:
```bash
# Using Python built-in HTTP server
python -m http.server 8000
```
Then open `http://localhost:8000` in your web browser.
