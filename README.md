# Claude Code Configuration Repository

A comprehensive collection of Claude Code configurations, including MCP servers, hooks, commands, and specialized agents to enhance your development workflow.

## Overview

This repository serves as a central hub for all useful Claude Code configuration resources:

- **🤖 Specialized Agents** - Domain-specific AI subagents for development tasks
- **🔌 MCP Servers** - Model Context Protocol server configurations and installation guides
- **🪝 Hooks** - Event-driven automation and workflow enhancements
- **⚙️ Commands** - Custom commands and utilities for Claude Code

## Repository Structure

```
├── agents/                     # Specialized AI subagents
│   ├── claude-code-agents/     # Production-ready agents (28 specialists)
│   └── vrac/                   # Extended agent collection
│       ├── engineering/        # Development & technical agents
│       ├── design/            # UI/UX and visual design agents
│       ├── marketing/         # Growth and marketing agents
│       ├── product/           # Product management agents
│       ├── project-management/ # Project coordination agents
│       ├── studio-operations/ # Operations and business agents
│       └── testing/           # Quality assurance agents
├── mcp/                       # MCP server configurations
│   └── README.md             # Installation commands and scope options
├── claude-code-hooks-mastery/ # Comprehensive hooks guide and examples
│   ├── apps/                 # Sample hook implementations
│   ├── ai_docs/              # Documentation and guides
│   └── images/               # Visual documentation
└── logs/                     # Hook execution logs and examples
```

## Getting Started

### 1. MCP Server Installation

Install MCP servers at different scopes based on your needs:

```bash
# User scope - Available across all projects (recommended for personal use)
claude mcp add --scope user context7 -- npx -y @upstash/context7-mcp
claude mcp add --scope user sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Project scope - Shared with team via .mcp.json
claude mcp add --scope project memory-bank -- npx -y @modelcontextprotocol/server-memory

# Local scope - Project-specific only (default)
claude mcp add mcp-compass -- npx -y @liuyoshio/mcp-compass
```

See [mcp/README.md](mcp/README.md) for complete installation guides.

### 2. Using Specialized Agents

Agents are automatically invoked based on context or can be explicitly called:

```bash
# Automatic delegation
"Optimize database performance"  # → triggers database-optimizer
"Review code for security issues" # → triggers security-auditor
"Design a REST API"             # → triggers backend-architect

# Explicit invocation
"Use performance-engineer to analyze bottlenecks"
"Have security-auditor scan for OWASP compliance"
"Get frontend-developer to create responsive layout"
```

### 3. Implementing Hooks

Explore comprehensive hook examples in `claude-code-hooks-mastery/`:

- **UserPromptSubmit**: Validate and enhance prompts
- **PreToolUse**: Control tool execution
- **PostToolUse**: Process tool results
- **PreResponse**: Filter responses
- **PostResponse**: Log and analyze outputs
- **SessionStart**: Initialize sessions

## Key Features

### 🎯 Multi-Agent Orchestration

Sophisticated coordination patterns:
- **Sequential Workflows**: `backend-architect` → `frontend-developer` → `test-automator`
- **Parallel Execution**: `performance-engineer` + `database-optimizer`
- **Conditional Routing**: `debugger` analyzes → routes to appropriate specialist
- **Review Validation**: Primary agent → review agent → final result

### 🔧 MCP Server Integration

Pre-configured servers for common needs:
- **Context7**: Up-to-date library documentation
- **Sequential Thinking**: Step-by-step problem solving
- **Memory Bank**: Persistent context across sessions
- **GitHub**: Repository management and automation

### 🚀 Hook-Driven Automation

Real-world examples for:
- Prompt validation and security filtering
- Automated logging and monitoring
- Context injection and session management
- Custom workflow triggers

## Contributing

We welcome contributions to expand and improve this configuration collection!

### Adding New Agents

1. **Choose the appropriate directory**:
   - `agents/claude-code-agents/` - Core development agents
   - `agents/vrac/` - Specialized or experimental agents

2. **Follow the agent format**:
```markdown
---
name: agent-name
description: Clear description of when this agent should be invoked
tools: tool1, tool2  # Optional - defaults to all tools
---

# Agent Role and Capabilities
Detailed system prompt defining the agent's expertise and behavior.
```

3. **Update documentation**:
   - Add agent to appropriate README section
   - Include usage examples
   - Document any special requirements

### Adding MCP Servers

1. **Add installation commands** to `mcp/README.md`:
```bash
# Include all three scopes
claude mcp add --scope local server-name -- npx -y package-name
claude mcp add --scope project server-name -- npx -y package-name  
claude mcp add --scope user server-name -- npx -y package-name
```

2. **Document configuration requirements**:
   - API keys or tokens needed
   - Environment variables
   - Usage examples

### Adding Hooks

1. **Create hook examples** in `claude-code-hooks-mastery/apps/`
2. **Document hook purpose** and lifecycle events
3. **Provide both Python and TypeScript examples** when applicable
4. **Include error handling** and logging patterns

### Adding Commands

1. **Document command usage** and parameters
2. **Provide working examples** with expected outputs
3. **Include troubleshooting** for common issues

## Submission Guidelines

### Pull Request Process

1. **Fork the repository** and create a feature branch
2. **Test your additions** in your local Claude Code setup
3. **Update relevant documentation** (README files, CLAUDE.md)
4. **Follow existing naming conventions** and file organization
5. **Include examples** demonstrating the new functionality
6. **Submit a pull request** with clear description of changes

### Quality Standards

- **Functionality**: All additions must work with current Claude Code versions
- **Documentation**: Include clear usage instructions and examples
- **Organization**: Follow existing directory structure and naming patterns
- **Testing**: Verify configurations work in different environments
- **Completeness**: Provide comprehensive information for users

### Areas of Interest

We're particularly interested in contributions for:

- **Industry-specific agents** (healthcare, finance, education, etc.)
- **Framework-specific agents** (React, Django, Rails, etc.)
- **Advanced hook patterns** (authentication, rate limiting, custom protocols)
- **MCP server integrations** for popular tools and services
- **Multi-language examples** beyond Python and TypeScript
- **Enterprise workflow patterns** and best practices

## Support and Resources

- **Claude Code Documentation**: https://docs.anthropic.com/en/docs/claude-code
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Hooks Guide**: [claude-code-hooks-mastery/README.md](claude-code-hooks-mastery/README.md)
- **Agent Patterns**: [agents/claude-code-agents/README.md](agents/claude-code-agents/README.md)

## License

This repository is open source and available under the MIT License. See individual components for specific licensing information.

---

**🚀 Start enhancing your Claude Code experience today!** Browse the agents, install useful MCP servers, and implement powerful hooks to supercharge your development workflow.