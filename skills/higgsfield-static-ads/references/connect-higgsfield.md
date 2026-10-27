# Connect Higgsfield to Claude

Higgsfield runs a hosted MCP server at `https://mcp.higgsfield.ai/mcp`. You sign in with your Higgsfield account. You need a paid Higgsfield plan and no API key.

Every generation through Claude spends Higgsfield credits. Higgsfield has no per-session cap, so tell Claude your limit.

## Claude.ai and Claude Desktop

1. Open Customize, then Connectors. Higgsfield's guide calls this Settings, then Connectors.
2. Click Add, then Add custom connector.
3. Name it Higgsfield and paste `https://mcp.higgsfield.ai/mcp`.
4. Click Connect. A Higgsfield sign-in window opens.
5. Sign in to Higgsfield and authorize.
6. In a chat, click + at the bottom left, open Connectors, and switch Higgsfield on.

On the Free plan you can add one custom connector. On Team and Enterprise plans, an owner adds the connector first, then each person connects.

## Claude Code

Option 1. If you log in to Claude Code with your claude.ai account, connectors you added on claude.ai show up in Claude Code. Type `/mcp` to check.

Option 2. Add the server yourself, then sign in:

```bash
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Then type `/mcp` in Claude Code, pick higgsfield, and finish the sign-in in your browser.

Higgsfield's own guide sets up Claude Code with the Higgsfield CLI instead. This skill needs the Ads Studio tools, which come from the MCP server.

## Cursor

Open Customize, then Marketplace, find Higgsfield, click Add, and sign in.

## Check it works

Start a new chat and ask: "What is my Higgsfield credit balance?" Claude should call the Higgsfield `balance` tool. If it answers without a tool call, check the connector is switched on in that chat.

## Sources

- [Higgsfield: connect to Claude, ChatGPT, or another agent](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent)
- [Claude Help Center: use connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Claude Help Center: custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code docs: connect to tools via MCP](https://code.claude.com/docs/en/mcp)
