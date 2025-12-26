"""
Note 1: to run the app
    > Terminal: streamlit run main.py
"""

# Import necessary libraries
import streamlit as st  # Main library used to build Streamlit apps
from pathlib import Path  # Helps manage file paths across different operating systems
import base64

# Configure the web page:
# - page_title sets the title shown in the browser tab
# - page_icon sets the favicon (small icon in the browser tab)
st.set_page_config(
    page_title="Abdul Salam Nassar",
    page_icon="🤠",  # Network emoji as icon
    initial_sidebar_state='collapsed'
)

# Sidebar language selection (radio buttons with Canadian flag emoji)
language = st.sidebar.radio(" 🍁 Language / Langue ", ["English", "Français"], index=0)

# Define file paths relative to this script's directory
# This ensures file references remain valid if the app is moved
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
profile_pic_path = current_dir / 'assets' / 'profile-pic.png'  # Profile picture file path
resume_path = current_dir / 'assets' / 'resume.pdf'            # Resume PDF file path

# Read the resume PDF file into memory so it can be downloaded by users
with open(resume_path, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

# English texts grouped in a dictionary for easy use
english_text = {
    "name": "Abdul Salam Nassar",
    "job_title": "Network & Systems Administrator",
    "resume_button": "📄 Resume",
    "intro": """
Our Prophet Muhammad peace be upon him said: “Whoever takes a path upon which to obtain knowledge, Allah makes the path to Paradise easy for him.”

For me, computer networking is not merely a vocation; it is a responsibility. From configuring my first home router 
to assisting others with their connectivity, I was drawn to understanding how systems interact and how trust is built through reliability. 
I approach every task with intention and discipline, whether optimizing enterprise networks or securing local systems. 
Seeking knowledge is a duty upon every Muslim, and applying it with honesty and excellence is a trust.
""",
    "skills_header": "🧠 Skills",
    "skills": {
        "🌐 Networking": {
            "Network Monitoring": 95,
            "Network Troubleshooting": 85,
            "Network Security": 85,
            "Network Design": 80,
            "Network Automation": 75,
            "Wireless Networking": 70,
            "Routing & Switching": 90
        },
        "🖥️ Systems Administration": {
            "Active Directory": 95,
            "Server Administration": 85,
            "Cloud Computing": 80,
            "Backup & Disaster Recovery": 80,
            "Virtualization": 60,
            "Patch Management": 75,
            "Database Administration": 90
        },
        "🔐 Security": {
            "Firewall Configuration": 90,
            "VPNs & Remote Access Security": 85,
            "Intrusion Detection & Prevention Systems": 65,
            "Network Access Control": 85,
            "SEIM/Log Analysis": 80,
            "Cryptography & PKI": 60,
            "Penetration Testing": 50,
        },
        "💻 Programming & Scripting": {
            "Python": 98,
            "Netmiko": 85,
            "SQL": 95,
            "Shell Scripting": 65,
            "Configuration as Code": 50,
            "Java": 90,
            "C++": 60,
        },
        "🧰 Tools & Utilities": {
            "Cisco Packet Tracer": 98,
            "Wireshark": 96,
            "Nmap": 92,
            "SolarWinds": 80,
            "Nagios": 65,
            "Ansible": 80,
            "PRTG": 65,
        }
    },
    "what_i_can_do_header": "🛠️ What I Can Do",
    "what_i_can_do": """
- Design, configure and secure business networks from scratch  
- Troubleshoot network and system outages with speed and precision  
- Automate infrastructure tasks with Python, PowerShell and Ansible  
- Perform basic penetration testing to identify and report  vulnerabilities    
- Explain complex technical issues clearly to non-technical users
""",
    "networking_tips_header": "💡 My Networking Tips",
    "networking_tips": [
        "Document everything. Predictability starts with records.",
        "Automate to worry less and do more.",
        "Keep networks simple and scalable.",
        "Monitor traffic to spot issues early.",
        "Think like an attacker. Anticipate weaknesses and close gaps before they’re exploited."
    ],
    "motto_header": "💬 Signature Quote",
    "motto": """
“Every good Network Admin should be part scientist, part artist, and part detective.”<br>
<span style="font-size:0.9em; color:#666;">— Abdul Salam Nassar, 2023</span>
""",
    "certification_header": '<a href="https://www.credly.com/badges/8ed85898-e494-4522-b4ba-e7fa4d63bb91/public_url" target="_blank" style="text-decoration:none; color:inherit;">🎖️ CompTIA Network+</a>',
    "contact_footer": "📬 Contact: abdusselam.nassar@gmail.com | [LinkedIn](https://www.linkedin.com/in/abdulsalam-nassar/) | [GitHub](https://github.com/abdelsalamalp)"
}

# French translations corresponding to the above English content
french_text = {
    "name": "Abdul Salam Nassar",
    "job_title": "Administrateur Réseau & Systèmes",
    "resume_button": "📄 CV",
    "intro": """
Le Prophète Muhammad (que la paix soit sur lui) a dit : « Celui qui emprunte un chemin en quête de savoir, Allah lui facilite un chemin vers le Paradis. »

Pour moi, les réseaux informatiques ne sont pas simplement une vocation ; c’est une responsabilité. De la configuration de mon premier routeur domestique à l’assistance apportée aux autres pour 
leurs problèmes de connectivité, j’ai été attiré par la compréhension du fonctionnement des systèmes et par la manière dont la confiance se construit par la fiabilité. 
J’aborde chaque tâche avec intention et discipline, qu’il s’agisse d’optimiser des réseaux d’entreprise ou de sécuriser des systèmes locaux. 
La quête du savoir est un devoir pour chaque musulman, et l’appliquer avec honnêteté et excellence est un dépôt de confiance.
""",
    "skills_header": "🧠 Compétences",
    "skills": {
        "🌐 Réseautage": {
            "Surveillance réseau": 95,
            "Dépannage réseau": 85,
            "Sécurité réseau": 85,
            "Conception réseau": 80,
            "Automatisation réseau": 75,
            "Réseau sans fil": 70,
            "Routage et commutation": 90
        },
        "🖥️ Administration Systèmes": {
            "Active Directory": 95,
            "Administration serveur": 85,
            "Infonuagique": 80,
            "Sauvegarde et reprise après sinistre": 80,
            "Virtualisation": 60,
            "Gestion des correctifs": 75,
            "Administration des bases de données": 90
        },
        "🔐 Sécurité": {
            "Configuration de pare-feu": 90,
            "VPN & sécurité accès distant": 85,
            "Systèmes de détection et prévention d'intrusion": 65,
            "Contrôle d'accès réseau": 85,
            "SEIM/Log Analysis": 80,
            "Cryptographie & PKI": 60,
            "Tests d’intrusion": 50,
        },
        "💻 Programmation & Scripts": {
            "Python": 98,
            "Netmiko": 85,
            "SQL": 95,
            "Shell scripting": 65,
            "Configuration as Code": 50,
            "Java": 90,
            "C++": 60,
        },
        "🧰 Outils & Utilitaires": {
            "Cisco Packet Tracer": 98,
            "Wireshark": 96,
            "Nmap": 92,
            "SolarWinds": 80,
            "Nagios": 65,
            "Ansible": 80,
            "PRTG": 65,
        }
    },
    "what_i_can_do_header": "🛠️ Ce Que Je Peux Faire",
    "what_i_can_do": """
- Concevoir, configurer et sécuriser des réseaux d’entreprise de A à Z  
- Diagnostiquer rapidement les pannes réseau et système  
- Automatiser les tâches d’infrastructure avec Python et Ansible  
- Réaliser des tests d’intrusion basiques pour identifier et signaler les vulnérabilités    
- Expliquer clairement des problèmes techniques aux non-techniciens
""",
    "networking_tips_header": "💡 Mes Conseils Réseautage",
    "networking_tips": [
        "Documentez tout. La prévisibilité commence par les dossiers.",
        "Automatisez pour vous inquiéter moins et faire plus.",
        "Gardez les réseaux simples et évolutifs.",
        "Surveillez le trafic pour détecter les problèmes tôt.",
        "Pensez comme un attaquant. Anticipez les faiblesses et colmatez les brèches avant qu’elles ne soient exploitées."
    ],
    "motto_header": "💬 Citation Signature",
    "motto": """
« Tout bon administrateur réseau devrait être en partie scientifique, en partie artiste, et en partie détective. »<br>
<span style="font-size:0.9em; color:#666;">— Abdul Salam Nassar, 2023</span>
""",
    "certification_header": '<a href="https://www.credly.com/badges/8ed85898-e494-4522-b4ba-e7fa4d63bb91/public_url" target="_blank" style="text-decoration:none; color:inherit;">🎖️ CompTIA Network+</a>',
    "contact_footer": "📬 Contact : abdusselam.nassar@gmail.com | [LinkedIn](https://www.linkedin.com/in/abdulsalam-nassar/) | [GitHub](https://github.com/abdelsalamalp)"
}

# Choose the text dictionary based on selected language
texts = english_text if language == "English" else french_text

# Create two columns to layout the profile section side-by-side
col1, col2 = st.columns(2, gap='small')

# Left column: display the profile image with ripple effect
with col1:
    with open(profile_pic_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    # CSS animation for ripple effect (same for both languages)
    st.markdown(
        f"""
        <style>
        @keyframes ripple {{
            0% {{ transform: scale(1) skew(0deg, 0deg); }}
            25% {{ transform: scale(1.05, 0.95) skew(1.5deg, -1.5deg); }}
            50% {{ transform: scale(1) skew(0deg, 0deg); }}
            75% {{ transform: scale(1.05, 0.95) skew(-1.5deg, 1.5deg); }}
            100% {{ transform: scale(1) skew(0deg, 0deg); }}
        }}

        .ripple-image {{
            width: 230px;
            animation: ripple 1.5s infinite ease-in-out;
            border-radius: 12px;
        }}
        </style>

        <img class="ripple-image" src="data:image/png;base64,{encoded_image}" />
        """,
        unsafe_allow_html=True
    )

# Right column: display name, job title, and resume download button (translated)
with col2:
    st.title(texts["name"], anchor=False)  # Name
    st.write(texts["job_title"])           # Job title

    # Resume download button uses English PDF but label translated
    st.download_button(
        label=texts["resume_button"],
        data=PDFbyte,
        file_name=resume_path.name,
        mime='application/pdf'
    )

st.write("######")  # Spacer

# Introduction text (translated)
st.write(texts["intro"])

# Vertical spacing
st.markdown("######")

# === SKILLS SECTION ===
# Horizontal divider
st.markdown("---")
st.header(texts["skills_header"], anchor=False)  # Header for skills

# Create tabs for each skill category (translated categories and skill names)
tabs = st.tabs(list(texts["skills"].keys()))

# Display each skill with a progress bar representing proficiency level
for i, category in enumerate(texts["skills"].keys()):
    with tabs[i]:
        for skill, level in texts["skills"][category].items():
            st.write(f"**{skill}**")  # Skill name in bold (translated)
            st.progress(level)         # Progress bar for skill level

# Horizontal divider
st.markdown("---")

# === WHAT I CAN DO SECTION ===
st.header(texts["what_i_can_do_header"], anchor=False)

# Task list translated
st.write(texts["what_i_can_do"])

# Horizontal divider
st.markdown("---")

# === NETWORKING TIPS SECTION ===
st.header(texts["networking_tips_header"], anchor=False)

# Show networking tips in info boxes (translated)
for tip in texts["networking_tips"]:
    st.info(f"{tip}")

# Horizontal divider
st.markdown("---")

# === SIGNATURE MOTTO SECTION ===
st.header(texts["motto_header"], anchor=False)

# Display motto in styled blockquote (translated)
st.markdown(
    f"""
    <blockquote style="font-size:1.4em; font-style:italic; color:#444; border-left:4px solid #ccc; padding-left:1em;">
    {texts["motto"]}
    """,
    unsafe_allow_html=True
)

# Horizontal divider
st.markdown("---")

# === CERTIFICATION SECTION ===
st.markdown(f"### {texts['certification_header']}", unsafe_allow_html=True)

# Horizontal divider
st.markdown("---")

# === CONTACT FOOTER ===
st.caption(texts["contact_footer"])
