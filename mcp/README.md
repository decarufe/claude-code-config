# MCP Server Installation Commands

This document contains the command line commands to install various MCP (Model Context Protocol) servers using Claude Code.

## Scope Options

- **local** (default): Available only in the current project directory
- **project**: Shared with team via `.mcp.json` file (can be checked into version control)
- **user**: Available across all projects on your workstation

## Installation Commands

### Context7
Provides up-to-date documentation and code examples for any library by dynamically injecting version-specific documentation into your prompts.

```bash
# Local scope (project-specific, default)
claude mcp add --scope local context7 -- npx -y @upstash/context7-mcp

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project context7 -- npx -y @upstash/context7-mcp

# User scope (available across all projects)
claude mcp add --scope user context7 -- npx -y @upstash/context7-mcp
```

### Sequential Thinking
Facilitates a detailed, step-by-step thinking process for problem-solving and analysis, breaking down complex problems into manageable steps.

```bash
# Local scope (project-specific, default)
claude mcp add --scope local sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# User scope (available across all projects)
claude mcp add --scope user sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
```

### GitHub
GitHub's official MCP Server for repository management, issue & PR automation, and code analysis. **Note**: The npm package `@modelcontextprotocol/server-github` is deprecated. Use the Docker image instead.

**Docker (recommended):**
```bash
# Use the official Docker image
docker run ghcr.io/github/github-mcp-server
```

**NPM package (deprecated):**
```bash
# Local scope (project-specific, default)
claude mcp add --scope local github -- npx -y @modelcontextprotocol/server-github

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project github -- npx -y @modelcontextprotocol/server-github

# User scope (available across all projects)
claude mcp add --scope user github -- npx -y @modelcontextprotocol/server-github
```

### Memory Bank
Provides persistent memory and context management across sessions, allowing AI assistants to store and retrieve information. Multiple implementations available:

**Option 1: @allpepper/memory-bank-mcp**
```bash
# Local scope (project-specific, default)
claude mcp add --scope local memory-bank -- npx -y @allpepper/memory-bank-mcp

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project memory-bank -- npx -y @allpepper/memory-bank-mcp

# User scope (available across all projects)
claude mcp add --scope user memory-bank -- npx -y @allpepper/memory-bank-mcp
```

**Option 2: @movibe/memory-bank-mcp**
```bash
# Local scope (project-specific, default)
claude mcp add --scope local memory-bank -- npx -y @movibe/memory-bank-mcp

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project memory-bank -- npx -y @movibe/memory-bank-mcp

# User scope (available across all projects)
claude mcp add --scope user memory-bank -- npx -y @movibe/memory-bank-mcp
```

**Option 3: @telagod/memory-bank-mcp-server**
```bash
# Local scope (project-specific, default)
claude mcp add --scope local memory-bank -- npx -y @telagod/memory-bank-mcp-server

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project memory-bank -- npx -y @telagod/memory-bank-mcp-server

# User scope (available across all projects)
claude mcp add --scope user memory-bank -- npx -y @telagod/memory-bank-mcp-server
```

**Option 4: Official basic memory implementation**
```bash
# Local scope (project-specific, default)
claude mcp add --scope local memory-bank -- npx -y @modelcontextprotocol/server-memory

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project memory-bank -- npx -y @modelcontextprotocol/server-memory

# User scope (available across all projects)
claude mcp add --scope user memory-bank -- npx -y @modelcontextprotocol/server-memory
```

### MCP Compass
MCP Discovery & Recommendation Service that helps you find the right MCP server for your needs through natural language queries.

```bash
# Local scope (project-specific, default)
claude mcp add --scope local mcp-compass -- npx -y @liuyoshio/mcp-compass

# Project scope (team-shared via .mcp.json)
claude mcp add --scope project mcp-compass -- npx -y @liuyoshio/mcp-compass

# User scope (available across all projects)
claude mcp add --scope user mcp-compass -- npx -y @liuyoshio/mcp-compass
```

## Usage Notes

1. **Context7**: Requires an API key. Add `use context7` to your prompts to access up-to-date documentation.

2. **Sequential Thinking**: Use for complex problem-solving that requires step-by-step analysis.

3. **GitHub**: Requires a GitHub Personal Access Token. The official implementation is now maintained by GitHub directly.

4. **Memory Bank**: Choose the implementation that best fits your needs. Each has different features and storage approaches.

5. **MCP Compass**: Acts as a discovery engine for other MCP servers. Ask it to recommend MCP tools based on your tasks.

## Configuration

After installation, these servers will be available in your Claude Code MCP configuration. You may need to provide additional configuration such as API keys or tokens depending on the specific server requirements.

## Additional Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Claude Code MCP Guide](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [MCP Server Directory](https://github.com/modelcontextprotocol/servers)