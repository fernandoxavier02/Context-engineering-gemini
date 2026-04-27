<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/branding/01-horizontal-dark.png">
    <img src="assets/branding/02-horizontal-light.png" alt="FX Studio AI" width="600"/>
  </picture>
</div>

<h1 align="center">Context Engineering for Gemini</h1>

<p align="center">
  <strong>Professional port of the Context Engineering Kit to Google Gemini CLI</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Gemini%20CLI-4285F4" alt="Platform"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>
  <img src="https://img.shields.io/badge/language-Python-blue" alt="Language"/>
</p>

## What It Does

Context Engineering for Gemini brings the multi-agent development patterns from the Context Engineering Kit (CEK) into Google Gemini CLI. It includes a reflexion system, git workflow automation, code review agents, TDD workflows, and more -- all adapted to work natively within Gemini's ecosystem.

## Features

- **Reflexion System** -- Iterative self-refinement with `/reflect` for higher-quality outputs.
- **Git Workflow** -- Automated commit formatting (`/git:commit`) and pull request creation (`/git:pr`).
- **Code Review Agents** -- Multi-perspective review with specialized judges and consensus building.
- **TDD Workflow** -- Test-driven development patterns ported for Gemini CLI usage.
- **Multi-Agent Patterns** -- Subagent orchestration, parallel execution, and competitive generation adapted from CEK.

## Installation

```bash
git clone https://github.com/fernandoxavier02/Context-engineering-gemini.git
cd Context-engineering-gemini
```

Follow the setup guide in the repository to configure your Gemini CLI with the context engineering extensions.

## Usage

```bash
# Start a reflexion cycle on your last output
/reflect

# Create a well-formatted commit
/git:commit

# Open a pull request with structured description
/git:pr

# Run code review with multiple judge agents
/critique
```

## Architecture

```
Gemini CLI
  |
  +-- Reflexion System (/reflect, /critique, /memorize)
  |     Self-refinement loop with multi-judge evaluation
  |
  +-- Git Workflow (/git:commit, /git:pr)
  |     Conventional commits, PR templates, branch management
  |
  +-- Development Patterns
        TDD, subagent orchestration, parallel agents
```

## License

MIT

---

<div align="center">
  <strong>Built by <a href="https://github.com/fernandoxavier02">Fernando Xavier</a></strong>
  <br/>
  <a href="https://fxstudioai.com">FX Studio AI</a> — Business Automation with AI
</div>
