# 🚀🤖 ScraperIO

<div align="center">

<a href="https://trendshift.io/repositories/11716" target="_blank"><img src="https://trendshift.io/api/badge/repositories/11716" alt="unclecode%2Fcrawl4ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai/network/members)

[![PyPI version](https://badge.fury.io/py/crawl4ai.svg)](https://badge.fury.io/py/crawl4ai)
[![Python Version](https://img.shields.io/pypi/pyversions/crawl4ai)](https://pypi.org/project/crawl4ai/)
[![Downloads](https://static.pepy.tech/badge/crawl4ai/month)](https://pepy.tech/project/crawl4ai)

<!-- [![Documentation Status](https://readthedocs.org/projects/crawl4ai/badge/?version=latest)](https://crawl4ai.readthedocs.io/) -->
[![License](https://img.shields.io/github/license/unclecode/crawl4ai)](https://github.com/unclecode/crawl4ai/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

</div>


<details>

# 🚀 Distributed Web Crawler on Azure with Airflow, FastAPI & Kubernetes

This project is a scalable and automated **distributed web crawling system** designed to run entirely on **Azure**, using:

- **Azure Kubernetes Service (AKS)** for orchestration
- **Apache Airflow (Community Edition)** with `KubernetesExecutor` for batch scheduling
- **FastAPI** for on-demand crawling (one-to-one)
- **Custom scraper containers** for crawling crawl4ai or Playwright
- **Azure Blob Storage** for storing scraped data

---

## 🧠 Project Overview

The system is built to support two key workflows:

- **One-to-One Crawling**: A user submits a single URL through a REST API. The system spins up a Kubernetes pod to crawl the URL and stores the result in Blob Storage.
- **Batch Crawling**: Airflow DAGs trigger jobs that launch multiple pods for large-scale crawling using `crawl4ai`.

Each crawler runs in its own Kubernetes pod, and the architecture is fully containerized and cloud-native.

---

## 🧱 Architecture Diagram



![alt text](<Captura desde 2025-04-27 21-15-59.png>)




## 🚀 Quick Start 

1. Install Crawl4AI:
```bash
# Install the package
pip install -U crawl4ai

# For pre release versions
pip install crawl4ai --pre

# Run post-installation setup
crawl4ai-setup

# Verify your installation
crawl4ai-doctor
```


