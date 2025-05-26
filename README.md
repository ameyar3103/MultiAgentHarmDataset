# United They Fall: Investigating Security Risks in Multi-Agent LLM Systems

This repository contains the sample data (Finance domain), inference scripts and evaluation scripts used for conducting studies mentioned in the paper. We will release the complete dataset upon acceptance of the paper.

## Project structure
```
.
├── data
│   ├── PNA_finance.json
│   ├── RAS_finance_contra.json
│   ├── RAS_finance_Coop.json
│   ├── RAS_finance_DPI.json
│   ├── RAS_finance_Imp.json
│   ├── RAS_finance_IPI.json
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
- ```data``` contains all the files for agent descriptions and tools corresponding to the agents.
  - ```PNA_finance.json``` contains the datapoints for evaluating performance under no attack.

  - ```RAS_finance_contra.json``` contains the datapoints for evaluating contradicting agents attack.

  - ```RAS_finance_Coop.json``` contains the datapoints for evaluating colluding agents attack.

  - ```RAS_finance_DPI.json``` contains the datapoints for evaluating DPI attack.

  - ```RAS_finance_Imp.json``` contains the datapoints for evaluating Impersonation attack.

  - ```RAS_finance_IPI.json``` contains the datapoints for evaluating IPI attack.

  - The rest of the files under ```data``` are tools for each of the agents.

- ```eval_scripts``` contains eval scripts for each of the attack types.

- ```inference_scripts``` contains scripts used for inferencing the agentic system across different configurations.

## Setup and Requirements

### Prerequisites

OpenAI and Gemini API keys are needed to run the eval scripts. 

We use GPT-4o for ARIA evaluations. For reproducing the results, an OpenAI API key is needed.

```Autogen``` library needs to be installed on your system.

## Evaluation

For evaluation, you can run the script using ```python3 eval_gemini.py```.
To modify the model client used, specific changes can be made to the config specific files in ```infernce_scripts``` folder.
