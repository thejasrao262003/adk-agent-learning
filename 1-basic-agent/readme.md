# Basic Agent Guide

## Overview
This guide covers the essential components and steps for building an agent using the ADK framework.

## Key Components
- Core attributes of building an agent
- Folder structure of creating an agent
- Installing proper dependencies
- Access and download API Key
- Running our agent

## Important Tips

### Root Agent Requirement
- Ensure inside ADK there is at least one root_agents

### Essential Properties
The following properties are crucial for agent configuration:

1. **name**
   - Must match exactly the directory name (e.g., `greeting_agent`)
   
2. **model**
   - Can use any model from any platform (Gemini, OpenAI, Claude, etc.)
   
3. **description**
   - High-level job overview of what the agent is specialized in
   
4. **instruction**
   - Specific instructions given to the agent on what it needs to do

## Running the Agent

To start the web interface, run:
```bash
adk web
```

## Available Commands

| Command | Description |
|---------|-------------|
| `api_server` | Starts a FastAPI server for agents |
| `create` | Creates a new app in the current directory |
| `deploy` | Deploys agent to hosted environment |
| `eval` | Evaluates an agent given the specified criteria |
| `run` | Runs an interactive CLI for the agent |
| `web` | Starts a FastAPI server with Web interface |
