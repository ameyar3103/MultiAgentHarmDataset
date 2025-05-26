# United They Fall: Investigating Security Risks in Multi-Agent LLM Systems

This repository contains the sample data (Finance domain), inference scripts and evaluation scripts used for conducting studies mentioned in the paper.

## Project structure
```
.
├── data
│   ├── PNA_finance.json
│   ├── RAS_finance_contra.json
│   ├── RAS_finance_Coop.json
│   ├── RAS_finance_DPI.json
│   ├── RAS_finance_Imp.json
│   ├── tools_identity_verification_agent.py
│   ├── tools_market_analysis_agent.py
│   ├── tools_risk_management_agent.py
│   └── tools_trade_execution_agent.py
├── eval_scripts
│   ├── eval_contra.py
│   ├── eval_coop.py
│   ├── eval_dpi.py
│   ├── eval_imp.py
│   └── eval_ipi.py
├── inference_scripts
│   ├── eval_gemini.py
│   ├── trapi_gemini.py
│   ├── trapi_gemini_roundr.py
│   └── trapi_gemini_swarm.py
└── README.md
```

```PNA_finance.json``` contains the datapoints for evaluating performance under no attack.

```RAS_finance_contra.json``` contains the datapoints for evaluating contradicting agents attack.

```RAS_finance_Coop.json``` contains the datapoints for evaluating colluding agents attack.

```RAS_finance_DPI.json``` contains the datapoints for evaluating DPI attack.

```RAS_finance_Imp.json``` contains the datapoints for evaluating Impersonation attack.
