# Lab 2.10: Production Deployment

**Duration:** 60 minutes
**Level:** 2

## Objectives

Complete this lab to demonstrate production and serverless deployment skills.

## Prerequisites

- Completed previous Level 2 labs
- Python 3.10+ with signalwire-agents installed
- Docker installed (for L2.10)
- AWS CLI configured (for L2.11)

## Instructions

### 1. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Implement Your Solution

Edit `solution/agent.py` according to the lab requirements.

### 3. Test Locally

```bash
swaig-test solution/agent.py --list-tools
swaig-test solution/agent.py --dump-swml
```

### 4. Submit

```bash
git add solution/agent.py
git commit -m "Complete Lab 2.10: Production Deployment"
git push
```

## Grading

| Check | Points |
|-------|--------|
| Agent Instantiation | 15 |
| SWML Generation | 15 |
| get_status function | 20 |
| get_time function | 15 |
| get_help function | 15 |
| Environment Config | 20 |
| **Total** | **100** |

**Passing Score:** 70%

---

## Next Assignment

Ready to continue? [**Start Lab 2.11: Serverless Deployment**](https://classroom.github.com/a/fWdRTsEV)

---

*SignalWire AI Agents Certification*
