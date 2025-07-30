Slang Transformer Web App

Transform informal slang sentences into formal English using this NLP-based Django web app.




## 📌 Features

- 🔤 Converts informal/slang sentences to formal English
- 📚 Uses a custom slang dictionary (1000+ entries)
- 💡 Simple UI with a dark neon-themed interface
- 🔐 User login/signup functionality
- 📬 Feedback form stored in DB (admin viewable)
- 🧠 Built with Django, Python, HTML/CSS, Bootstrap

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3 (default)
- **Version Control:** Git + GitHub
- **Deployment:** Render.com
- **Tools:** VS Code, Git Bash, Jupyter (for NLP logic)

---

## 🧪 NLP Logic

The slang transformation logic is handled by `transform.py` using:

- A large JSON-based slang dictionary
- String replacement + regex logic (expandable to context-aware NLP)

---

## 📂 Project Structure

```

slang-transformer-app/
├── slangweb/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── transformer/
│   ├── templates/
│   ├── static/
│   └── views.py
├── slang\_dict.json
├── transform.py
├── render.yaml
├── requirements.txt
├── manage.py
└── README.md

````

---

## 🧑‍💻 How to Run Locally

```bash
git clone https://github.com/yourusername/slang-transformer-app.git
cd slang-transformer-app
pip install -r requirements.txt
python manage.py runserver
````

---

## 🌐 Deployment (Render)

* Uses `gunicorn` + `render.yaml`
* Static files handled via `collectstatic`
* DB auto-migrated during deploy

---

## 🙋‍♂️ Author

**Manas Srivastava**
📧 [manasworks04@gmail.com](mailto:manasworks04@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/manas-srivastava/)
💻 [GitHub](https://github.com/manas-onGit)

---

## ⭐ Credits

* Inspired by real-world slang formalization challenges
* Thanks to Django, Bootstrap, and OpenAI support

```

