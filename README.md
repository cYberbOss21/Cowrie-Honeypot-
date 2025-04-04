# 🐍 Cowrie Honeypot with Slack Alerts
A project that sets up [Cowrie](https://github.com/cowrie/cowrie), an SSH honeypot, on a Linux host and integrates it with Slack for real-time alerts on malicious activity.

## ⚠️ Disclaimer

This honeypot is for educational and monitoring purposes only. It should always be deployed in an isolated, non-production environment. Do not use honeypots in environments where they could be mistaken for real infrastructure, and ensure they comply with all local laws and regulations.

## 🔍 What Is a Honeypot?

A honeypot is a decoy system designed to lure cyber attackers. It simulates a vulnerable target, capturing and logging interactions to help analysts understand attacker behaviors, techniques, and motives.

---

## 🎯 Why Are Honeypots Important?

Honeypots are a proactive security tool that serve as a trap for attackers, offering insights that traditional detection systems may miss. They:

- Detect early threats before they impact production systems

- Log attacker behavior and tools in a controlled environment

- Support red team/blue team exercises

- Improve incident response readiness

---

# 📊 Recent Honeypot Stats

🚨 1,000% spike in honeypot activity occurred in the two weeks prior to the MOVEit vulnerability disclosure, showing how honeypots can provide early warnings of mass exploitation campaigns ([Coalition](https://www.coalitioninc.com/blog/2024-cyber-threat-index?utm_source=chatgpt.com))

🔍 42 million attacks were logged on honeypots between Jan–Sept 2022, including 5.5 million attempts using default credentials like root:root ([Outpost24](https://outpost24.com/blog/honeypot-findings-from-over-42-million-attacks/?utm_source=chatgpt.com))

📈 The honeypot market is projected to hit $1.4 billion by 2033, with a 13.5% CAGR, driven by demand for better threat detection ([Archive Market Research](https://www.archivemarketresearch.com/reports/cybersecurity-honeypot-12678?utm_source=chatgpt.com))

---

## 🛠 Project Features

- ✅ Cowrie SSH honeypot listening on port 22

- ✅ Slack integration to send real-time alerts

- ✅ Alerts on login attempts, command execution, downloads, session start/end

- ✅ Extendable Python script for integration with Discord, email, or a SIEM

---

## 👨‍💻 For Cybersecurity Analysts

This project provides practical hands-on experience for:

- Blue team monitoring

- Threat intelligence gathering

- Detection engineering

- Log analysis

- Developing Python automation for SOC workflows

- Use it to simulate attacks, gather attacker TTPs, and improve detection rules.

---

## 🤝 Contributing

Contributions, improvements, or integrations with other platforms are welcome. Fork the repo and open a pull request.

